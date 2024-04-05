from fastapi import Depends, FastAPI

from .internal import admin
from .predicts import router as predicts
from .status import router as status
from .instruments import router as instruments

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(status.router)
app.include_router(predicts.router)
app.include_router(instruments.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Noting to see here"}
