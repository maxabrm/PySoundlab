from pydantic import BaseModel
from typing import Dict, Any

class PotiModel(BaseModel):
    id: str
    inputPin: str
    resistance: float
    maxValue: float

class NodeModel(BaseModel):
    id: str
    type: str
    Poti: PotiModel
    config: Dict[str, Any]