import time
import functools


class MetricsRecorder:
    """Class to record and manage metrics."""
    
    @staticmethod
    def measure_latency(func):
        """Decorator to measure function execution latency and inject into sample.metrics.latency_seconds."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            latency_seconds = end - start
            
            # Inject latency into result if it has a metrics attribute
            if hasattr(result, 'metrics'):
                result.metrics.latency_seconds = latency_seconds
            
            return result
        
        return wrapper
    
    @staticmethod
    def record_token_usage(sample, input_tokens: int, output_tokens: int, step: str = "generation"):
        """
        Safely increments token counts in the sample metrics.
        Use += to support multi-step pipelines (e.g. Iterative Retrieval).
        """
        if hasattr(sample, 'metrics'):
            # Always increment the total for backward compatibility
            sample.metrics.input_tokens += input_tokens
            sample.metrics.output_tokens += output_tokens
            
            # Route to specific buckets based on the step parameter
            if step == "uq":
                sample.metrics.uq_input_tokens += input_tokens
                sample.metrics.uq_output_tokens += output_tokens
            elif step == "generation":
                sample.metrics.gen_input_tokens += input_tokens
                sample.metrics.gen_output_tokens += output_tokens
            elif step == "decompose":
                sample.metrics.decomp_input_tokens += input_tokens
                sample.metrics.decomp_output_tokens += output_tokens    

            # print(f"1.  Total Input Tokens   : {sample.metrics.input_tokens} tokens")
            # print(f"   ├─ UQ Tokens          : {sample.metrics.uq_input_tokens} tokens")
            # print(f"   └─ RAG Tokens         : {sample.metrics.gen_input_tokens:.0f} tokens")
            # print(f"2.  Total Output Tokens  : {sample.metrics.output_tokens} tokens")
            # print(f"   ├─ UQ Tokens          : {sample.metrics.uq_output_tokens} tokens")
            # print(f"   └─ RAG Tokens         : {sample.metrics.gen_output_tokens:.0f} tokens")

    @staticmethod
    def record_retrieval_call(sample, count: int = 1):
        """Records a call to the retrieval system."""
        if hasattr(sample, 'metrics'):
            sample.metrics.num_retrieval_calls += count

    @staticmethod
    def record_llm_call(sample, count: int = 1):
        """Records a call to the LLM generation."""
        if hasattr(sample, 'metrics'):
            sample.metrics.num_llm_calls += count