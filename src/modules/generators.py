from .base import PipelineComponent


class IdentityGenerator(PipelineComponent):
    def process(self, sample):
        sample.search_queries = [sample.claim]
        return sample