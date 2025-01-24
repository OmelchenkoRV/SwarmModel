from pydantic import BaseModel
from typing import List


class SimulationRequest(BaseModel):
    transition_matrix: List[List[float]]
    steps: int
