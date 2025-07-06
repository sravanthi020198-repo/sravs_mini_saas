from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, issues, dashboard
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(issues.router, prefix="/api/issues")
app.include_router(dashboard.router, prefix="/api/dashboard")

@app.get("/")
def read_root():
    return {"status": "Mini SaaS Tracker Running"}

@app.get("/api/docs", include_in_schema=False)
def custom_openapi():
    return get_openapi(
        title="Issues & Insights Tracker API",
        version="1.0.0",
        routes=app.routes
    )

