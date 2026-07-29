import pytest
import numpy as np
import cv2

from src.ocr.engine.ocr_engine import OCREngine
from src.models.ocr_input import DetectorType, RecognizerType
from src.ocr.engine.engine_factory import EngineFactory
from src.config.config_loader import get_paddleocr_config


@pytest.fixture
def det_test_image():
    return cv2.imread("tests/assets/images/det_test.png")

@pytest.fixture
def rec_test_image():
    return cv2.imread("tests/assets/images/rec_test.png")

@pytest.fixture
def engine() -> OCREngine:
    config_data = get_paddleocr_config()
    engine = EngineFactory.create_engine(
        DetectorType.PADDLE, 
        RecognizerType.PADDLE, 
        config_data
    )
    return engine