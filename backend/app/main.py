from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from app.routers import auth, issues, users, stats
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Issues & Insights Tracker API",
    description="Mini SaaS Issue Tracker",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix='/api/auth', tags=["auth"])
app.include_router(issues.router, prefix='/api/issues', tags=["issues"])
app.include_router(users.router, prefix='/api/users', tags=["users"])
app.include_router(stats.router, prefix='/api/stats', tags=["stats"])

Instrumentator().instrument(app).expose(app, include_in_schema=False, endpoint="/metrics")
