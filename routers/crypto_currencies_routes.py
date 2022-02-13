from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/bitcoin", response_class=HTMLResponse)
async def bitcoin(request: Request):
    img = "static/assets/img/bitcoin.png"
    return templates.TemplateResponse("bitcoin.html", {"request": request, "img": img})
