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
    def record_token_usage(sample, input_tokens: int, output_tokens: int):
        """
        Safely increments token counts in the sample metrics.
        Use += to support multi-step pipelines (e.g. Iterative Retrieval).
        """
        if hasattr(sample, 'metrics'):
            sample.metrics.input_tokens += input_tokens
            sample.metrics.output_tokens += output_tokens

        # print(f"Input: {input_tokens} tokens")
        # print(f"Output: {output_tokens} tokens")