from fastapi import FastAPI

from app.routers.profile_router import router as profile_router
from app.routers.technology_router import router as technology_router
from app.routers.project_router import router as project_router
from app.routers.feedback_router import router as feedback_router
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException

from app.handlers.exception_handlers import (
    validation_exception_handler,
    http_exception_handler,
)

app = FastAPI(
    title="DevShowcase API",
    description="API da plataforma DevShowcase",
    version="1.0.0"
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

app.include_router(profile_router)
app.include_router(technology_router)
app.include_router(project_router)
app.include_router(feedback_router)


@app.get("/")
def root():
    return {
        "message": "DevShowcase API está funcionando!"
    }