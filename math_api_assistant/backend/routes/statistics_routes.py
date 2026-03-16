from fastapi import APIRouter
# Structură simplă pentru statisticile aplicației
router = APIRouter()

statistics = {
    "solved": 0
}

@router.get("/statistics")
def get_stats():

    return statistics