from io import BytesIO
from ultralytics import YOLO
from PIL import Image
import base64

from .constants import MODEL_PATH, CONF_THRESHOLD, SURGICAL_OBJECTS_NAMES
import numpy as np
import cv2


def detect(image_str: str):
    model = YOLO(MODEL_PATH)

    # Decode the image from base64
    image_bytes = base64.b64decode(image_str)
    nparr = np.fromstring(image_bytes, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Perform prediction
    results = model(img_np, conf=CONF_THRESHOLD, imgsz=1280)

    # Encode the result image to base64
    im_array = results[0].plot()
    im = Image.fromarray(im_array[..., ::-1])
    buffered = BytesIO()
    im.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())

    # Calculate the position of objects
    sorted_objs = [
        (
            SURGICAL_OBJECTS_NAMES.index(results[0].names[int(r[0])]),
            results[0].names[int(r[1].cls[0])],
        )
        for r in sorted(enumerate(results[0].boxes), key=lambda x: x[1].xyxy[0][0])
    ]

    # Save the image (optional)
    # im.save(OUTPUT_DIR + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg")

    return {"image": img_str, "objects": sorted_objs}
