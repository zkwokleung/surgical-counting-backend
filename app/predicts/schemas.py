from fastapi import FastAPI
from pydantic import BaseModel, Field


class PredictRequestBody(BaseModel):
    image: str = Field(
        title="The string of a base64 encoded image file", examples=["Y3Voaw=="]
    )


class PredictResponseBody(BaseModel):
    image: str = Field(
        title="The string of a base64 encoded image file", examples=["Y3Voaw=="]
    )
    objects: list = Field(
        title="The list of objects found in the image in order from left to right",
        examples=[
            [
                [6, "suction_cannula"],
                [4, "cap_fx"],
                [7, "spatula"],
                [8, "con_scissor"],
                [0, "speculum"],
                [5, "curved_cannula"],
                [1, "bip_fx"],
                [2, "iris_scissor"],
                [3, "needle_holder"],
            ]
        ],
    )
