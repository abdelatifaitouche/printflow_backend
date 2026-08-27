from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from src.api.routes import router as api
from src.infra.db.models import *
from src.infra.db.engine import engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(title="Printflow", lifespan=lifespan)

app.include_router(api)


@app.get("/health")
def health():
    return JSONResponse(
        content={"response": "healthing"},
        status_code=status.HTTP_200_OK,
    )
