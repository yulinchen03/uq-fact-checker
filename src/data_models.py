from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

class Document(BaseModel):
    content: str
    source_id: str
    score: float = 0.0
    metadata: Dict[str, Any] = Field(default_factory=dict)


class FactCheckMetrics(BaseModel):
    latency_seconds: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0


class FactCheckSample(BaseModel):
    id: str
    claim: str
    gold_label: Optional[str] = None
    gold_evidence: List[str] = Field(default_factory=list) 
    mode: Literal["always_retrieve", "never_retrieve", "uq_aware"]
    search_queries: List[str] = Field(default_factory=list)
    retrieved_evidence: List[Document] = Field(default_factory=list)
    aggregated_context: str = ""
    predicted_verdict: Optional[str] = None
    explanation: Optional[str] = None
    metrics: FactCheckMetrics = Field(default_factory=FactCheckMetrics)

    # --- UQ SPECIFIC FIELDS ---
    uncertainty_score: Optional[float] = None
    parametric_response: Optional[str] = None
    parametric_verdict: Optional[str] = None
    retrieval_triggered: bool = False
    rag_prediction: Optional[str] = None