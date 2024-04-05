from app.instruments.constants import *


def get_image_path(id: str):
    return IMAGE_PATH_PREFIX + id + IMAGE_SUFFIX
