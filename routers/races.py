from fastapi import APIRouter, HTTPException
import models.race as Race

router = APIRouter()


@router.get("/races/years")
async def get_years():
    return Race.get_races_years()


@router.get("/races/years/{year}")
async def get_races_by_year(year: int):
    return Race.get_races_by_year(year)


@router.get("/races/positions/{raceId}")
async def get_positions_by_race(raceId: int):
    return Race.get_positions_by_race(raceId)
