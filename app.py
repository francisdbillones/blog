from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index():
    return HTMLResponse(content=Path("index.html").read_text())

# @app.get("/articles/{article_name}")
# async def read_article(article_name: str):
#     context = get_context()

#     return templates.TemplateResponse("article.html", context)