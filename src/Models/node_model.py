from pydantic import BaseModel
from typing import Optional

class PotiModel(BaseModel):
    id: str
    inputPin: str
    resistance: float
    maxValue: float

class NodeModel(BaseModel):
    id: str
    type: str
    Poti: Optional[PotiModel] = None
    parameter: Optional[float] = None