from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from tortoise.exceptions import DoesNotExist, IntegrityError

from app.config import settings
from app.api.api_v1.api import api_router


app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_PATH)


@app.exception_handler(DoesNotExist)
async def http_exception_handler(request: Request, exc: DoesNotExist):
    return JSONResponse(
        status_code=404,
        content={"error": str(exc)},
    )


@app.exception_handler(IntegrityError)
async def integrityerror_exception_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=422,
        content={"error": str(exc)}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"error": str(exc)},
    )
