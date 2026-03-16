from fastapi import APIRouter
from services.exercise_generator import generate_equation
# Ruta pentru generarea automată de exerciții
router = APIRouter()

@router.get("/generate-exercise")
def generate():

    exercise = generate_equation()

    return {"exercise": exercise}