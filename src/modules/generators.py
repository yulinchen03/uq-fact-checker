from .base import PipelineComponent


class QueryGenerator(PipelineComponent):
    def process(self, sample):
        sample.search_queries = [sample.claim]
        return sample