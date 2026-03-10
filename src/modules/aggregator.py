from .retriever import PipelineComponent

class EvidenceAggregator(PipelineComponent):
    def __init__(self, max_tokens: int, tokenizer=None):
        self.max_tokens = max_tokens
        self.tokenizer = tokenizer
    
    def process(self, sample):
        context_parts = [doc.content for doc in sample.retrieved_evidence]
        aggregated_context = "\n\n".join(context_parts)
        
        # use tokenizer precise token-based truncation
        if self.tokenizer:
            # Encode text to tokens (without adding BOS/EOS tokens yet)
            tokens = self.tokenizer.encode(aggregated_context, add_special_tokens=False)
            
            if len(tokens) > self.max_tokens:
                # 1. Do the precise token slice
                truncated_tokens = tokens[:self.max_tokens]
                
                # 2. Decode back into a string
                truncated_text = self.tokenizer.decode(truncated_tokens, skip_special_tokens=True)
                
                # 3. Find the index of the last sentence-ending punctuation
                last_period = truncated_text.rfind('.')
                last_question = truncated_text.rfind('?')
                last_exclamation = truncated_text.rfind('!')
                last_punctuation = max(last_period, last_question, last_exclamation)
                
                # 4. Slice cleanly at the end of that sentence
                if last_punctuation != -1:
                    aggregated_context = truncated_text[:last_punctuation + 1]
                else:
                    last_space = truncated_text.rfind(' ')
                    aggregated_context = truncated_text[:last_space] if last_space != -1 else truncated_text

        # character based fallback (if tokenizer is missing)
        else:
            # A standard rule of thumb is ~4 characters per token
            char_limit = self.max_tokens * 4 
            if len(aggregated_context) > char_limit:
                truncated = aggregated_context[:char_limit]
                last_period = truncated.rfind('.')
                last_punctuation = max(truncated.rfind('.'), truncated.rfind('?'), truncated.rfind('!'))
                
                if last_punctuation != -1:
                    aggregated_context = truncated[:last_punctuation + 1]
                else:
                    last_space = truncated.rfind(' ')
                    aggregated_context = truncated[:last_space] if last_space != -1 else truncated
        
        sample.aggregated_context = aggregated_context
        return sample