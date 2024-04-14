from fastapi import APIRouter, HTTPException
from .schemas import PredictRequestBody, PredictResponseBody
from .utils import detect

router = APIRouter(
    prefix="/predict",
    tags=["predict"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def predict(body: PredictRequestBody) -> PredictResponseBody:
    # run the model
    try:
        res = detect(body.image.encode())
    except ValueError as e:
        # response with 422 if the image is invalid
        raise HTTPException(status_code=422, detail=e.args[0]) from None

    # return the image as base64
    return {"image": res["image"], "objects": res["objects"]}
