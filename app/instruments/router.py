from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.instruments.constants import INSTRUMENT_DATA

router = APIRouter(
    prefix="/instrument",
    tags=["instrument"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get/{id}")
async def get_single(id: str):
    if INSTRUMENT_DATA.get(id) is None:
        raise HTTPException(status_code=404, detail="Instrument not found")

    return {"data": INSTRUMENT_DATA[id]}


@router.get("/get_all")
async def get_all():
    return {"data": INSTRUMENT_DATA}


@router.get(
    "/image/{id}",
    response_class=FileResponse,
)
async def get_image(id: str):
    # Check if the instrument exists
    if INSTRUMENT_DATA.get(id) is None:
        raise HTTPException(status_code=404, detail="Instrument not found")

    return FileResponse("./app/instruments/images/" + id + ".jpg")
