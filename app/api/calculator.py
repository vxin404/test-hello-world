from fastapi import APIRouter
from app.models import CalcRequest, CalcResponse
from app.services import evaluate_expression

router = APIRouter(prefix="/api", tags=["calculator"])

@router.post("/calculate", response_model=CalcResponse)
async def calculate(request: CalcRequest):
    """Calculate mathematical expression."""
    try:
        result = evaluate_expression(request.expression)
        return CalcResponse(result=str(result), success=True)
    except Exception as e:
        return CalcResponse(result="", success=False, error=str(e))

@router.get("/hello")
async def api_hello():
    """Health check endpoint."""
    return {"message": "Hello World", "service": "OpenClaw FastAPI Calculator"}
