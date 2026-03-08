"""
API route modules.
"""
from app.api.calculator import router as calculator_router
from app.api.pages import router as pages_router
from app.api.gomoku import router as gomoku_router

__all__ = ["calculator_router", "pages_router", "gomoku_router"]
