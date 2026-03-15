from fastapi import FastAPI
from backend.routes.solve_routes import router as solve_router
from backend.routes.exercise_routes import router as exercise_router
from backend.routes.statistics_routes import router as statistics_router

app = FastAPI(title="AI Math Learning Platform")

app.include_router(solve_router)
app.include_router(exercise_router)
app.include_router(statistics_router)

@app.get("/")
def home():
    return {"message": "AI Math Platform API running"}