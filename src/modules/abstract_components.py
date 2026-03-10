from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class FactCheckSample:
    """Sample data structure for fact-checking pipeline."""
    pass


class PipelineComponent(ABC):
    """Abstract base class for pipeline components."""
    
    @abstractmethod
    def process(self, sample: FactCheckSample) -> FactCheckSample:
        """
        Process a fact-check sample in-place and return it.
        
        Args:
            sample: The sample to process
            
        Returns:
            The modified sample
        """
        pass