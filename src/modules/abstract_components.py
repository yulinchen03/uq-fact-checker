from abc import ABC, abstractmethod


class PipelineComponent(ABC):
    """Abstract base class for pipeline components."""

    @abstractmethod
    def process(self, sample) -> "FactCheckSample":
        """Process a fact-check sample in-place and return it."""
        pass