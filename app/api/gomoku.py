from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/gomoku", tags=["gomoku"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def gomoku_page(request: Request):
    """五子棋游戏页面"""
    return templates.TemplateResponse("gomoku.html", {"request": request})
