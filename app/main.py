from fastapi import Depends, FastAPI

from .internal import admin
from .predicts import router as predicts

app = FastAPI()


app.include_router(predicts.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Noting to see here"}
