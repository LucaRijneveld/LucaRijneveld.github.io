from pydantic import BaseModel
from typing import Optional
from typing import List


class SurveyInput(BaseModel):
    q1: List[int]
    q2: List[int]
    q3: List[int]
    q4: List[int]
    q5: List[int]
    q6: Optional[str] = None
    declined: bool = False
