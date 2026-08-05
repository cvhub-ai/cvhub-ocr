import os

from dotenv import load_dotenv

load_dotenv()


SERVICE_NAME = os.getenv("SERVICE_NAME", "ocr")

MAX_IMAGE_SIZE_BYTES = int(
    os.getenv(
        "MAX_IMAGE_SIZE_BYTES",
        str(20 * 1024 * 1024),
    )
)

MAX_BATCH_SIZE = int(
    os.getenv(
        "MAX_BATCH_SIZE",
        "10",
    )
)

MAX_IMAGE_WIDTH = int(
    os.getenv(
        "MAX_IMAGE_WIDTH",
        "10000",
    )
)

MAX_IMAGE_HEIGHT = int(
    os.getenv(
        "MAX_IMAGE_HEIGHT",
        "10000",
    )
)


if MAX_IMAGE_SIZE_BYTES <= 0:
    raise ValueError("MAX_IMAGE_SIZE_BYTES must be greater than 0.")

if MAX_BATCH_SIZE <= 0:
    raise ValueError("MAX_BATCH_SIZE must be greater than 0.")

if MAX_IMAGE_WIDTH <= 0:
    raise ValueError("MAX_IMAGE_WIDTH must be greater than 0.")

if MAX_IMAGE_HEIGHT <= 0:
    raise ValueError("MAX_IMAGE_HEIGHT must be greater than 0.")
