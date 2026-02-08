from .retrievers import PipelineComponent


class SimpleConcatAggregator(PipelineComponent):
    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
    
    def process(self, sample):
        context_parts = [doc.content for doc in sample.retrieved_evidence]
        aggregated_context = "\n\n".join(context_parts)
        
        if len(aggregated_context) > self.max_tokens:
            aggregated_context = aggregated_context[:self.max_tokens]
        
        sample.aggregated_context = aggregated_context
        return sample