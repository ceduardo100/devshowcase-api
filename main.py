from fastapi import FastAPI

from app.routers.profile_router import router as profile_router
from app.routers.technology_router import router as technology_router
from app.routers.project_router import router as project_router

app = FastAPI(
    title="DevShowcase API",
    description="API da plataforma DevShowcase",
    version="1.0.0"
)


app.include_router(profile_router)
app.include_router(technology_router)
app.include_router(project_router)

@app.get("/")
def root():
    return {
        "message": "DevShowcase API está funcionando!"
    }