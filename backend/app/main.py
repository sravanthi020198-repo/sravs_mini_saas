from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, issues, dashboard

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
