from fastapi import APIRouter
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
    res = detect(body.image.encode())

    # return the image as base64
    return {"image": res["image"], "objects": res["objects"]}
