from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Erro de validação",
            "message": "Verifique os dados enviados.",
            "details": exc.errors(),
        },
    )


async def http_exception_handler(
    request: Request,
    exc,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "Erro na requisição",
            "message": exc.detail,
        },
    )