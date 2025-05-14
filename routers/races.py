from fastapi import APIRouter, HTTPException, Request
import models.race as Race

router = APIRouter()


@router.get("/races/years", tags=["Race"])
async def get_years():
    return Race.get_races_years()


@router.get("/races/years/{year}", tags=["Race"])
async def get_races_by_year(year: int):
    return Race.get_races_by_year(year)


@router.get("/races/positions/{raceId}", tags=["Race"])
async def get_positions_by_race(raceId: int):
    return Race.get_positions_by_race(raceId)
