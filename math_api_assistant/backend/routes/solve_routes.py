from fastapi import APIRouter
from pydantic import BaseModel
from math_engine.solver import solve_problem

router = APIRouter()

class MathProblem(BaseModel):
    exercise: str

@router.post("/solve")
def solve(problem: MathProblem):

    result = solve_problem(problem.exercise)

    return result