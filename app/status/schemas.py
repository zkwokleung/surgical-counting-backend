from fastapi import FastAPI
from pydantic import BaseModel, Field


class StatusResponseBody(BaseModel):
    status: str = Field(title="The status of the application", examples=["ok"])
