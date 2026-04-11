from .retriever import PipelineComponent

class EvidenceAggregator(PipelineComponent):
    def __init__(self):
        pass
    
    def process(self, sample):
        # Dictionary to group chunks by their parent document ID
        grouped_evidence = {}
        
        for doc in sample.retrieved_evidence:
            # Note: Ensure your Document data model has source_id defined!
            source_id = getattr(doc, 'source_id', "unknown")
            
            if source_id not in grouped_evidence:
                # First time seeing this document, keep the Title formatting intact
                grouped_evidence[source_id] = doc.content
            else:
                # We already have a chunk from this document! 
                # strip the redundant "Title: [X]\nContent: " prefix to save tokens
                raw_content = doc.content.split("Content: ", 1)[-1]
                
                # Append the new chunk to the existing parent context
                # We use "[...]" to indicate to the LLM that there is a jump/overlap between chunks
                grouped_evidence[source_id] += f"\n[...] {raw_content}"
        
        # Join the final, deduplicated parent documents together
        # If top_k=1, this just returns the single chunk
        context_parts = list(grouped_evidence.values())
        sample.aggregated_context = "\n\n---\n\n".join(context_parts)
        
        return sample