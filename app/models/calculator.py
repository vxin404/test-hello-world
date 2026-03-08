from pydantic import BaseModel

class CalcRequest(BaseModel):
    expression: str

class CalcResponse(BaseModel):
    result: str
    success: bool
    error: str = None
