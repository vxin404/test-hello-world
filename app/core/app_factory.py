from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import calculator_router, pages_router, gomoku_router

def create_app() -> FastAPI:
    """Application factory pattern."""
    app = FastAPI(
        title="Advanced Calculator Service",
        description="A full-featured web calculator with scientific functions",
        version="1.0.0"
    )
    
    # Mount static files
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    
    # Register routers
    app.include_router(pages_router)
    app.include_router(calculator_router)
    app.include_router(gomoku_router)
    
    return app
