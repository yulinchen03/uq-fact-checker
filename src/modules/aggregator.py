from .retriever import PipelineComponent

class EvidenceAggregator(PipelineComponent):
    def __init__(self):
        pass
    
    def process(self, sample):
        grouped_evidence = {}
        
        for doc in sample.retrieved_evidence:
            source_id = getattr(doc, 'source_id', "unknown")
            
            if source_id not in grouped_evidence:
                grouped_evidence[source_id] = doc.content
            else:
                # Strip redundant "Title: [X]\nContent: " prefix to save tokens
                raw_content = doc.content.split("Content: ", 1)[-1]
                # "[...]" signals to the LLM that there is a gap between non-contiguous chunks
                grouped_evidence[source_id] += f"\n[...] {raw_content}"
        
        context_parts = list(grouped_evidence.values())
        sample.aggregated_context = "\n\n---\n\n".join(context_parts)
        
        return sample