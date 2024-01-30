import logging

import uvicorn
from fastapi import FastAPI, Request, WebSocket,Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

        
templates = Jinja2Templates(directory="/opt/app/templates")

# Create logger
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
)
logger = logging.getLogger()

app = FastAPI(
    title="FASTAPI - API",
    description="Documentação API ",
    redoc_url=None,
    openapi_url=None,
    docs_url=None,
)

app.mount("/static", StaticFiles(directory="/opt/app/static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def alive():
    return {"message": "api alive"}

@app.get("/ping")
async def health():
    return {"message": "healthcheck api alive"}

if __name__ == "__main__":
    uvicorn.run(app, port=8082)
