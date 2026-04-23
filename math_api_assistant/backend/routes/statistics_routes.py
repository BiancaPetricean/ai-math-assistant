from fastapi import APIRouter

router = APIRouter()

statistics = {
    "solved": 0
}

@router.get("/statistics")
def get_stats():

    return statistics