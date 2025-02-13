from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.docker import docker_router
from app.kubernetes import kubernetes_router
app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(docker_router.router)
app.include_router(kubernetes_router.router)