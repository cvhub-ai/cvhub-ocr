import pytest
import numpy as np
import cv2

from src.config.config_loader import get_paddleocr_config
from src.engine.paddle_engine import PaddleOCREngine


@pytest.fixture
def det_test_image():
    return cv2.imread("tests/assets/images/det_test.png")

@pytest.fixture
def rec_test_image():
    return cv2.imread("tests/assets/images/rec_test.png")

@pytest.fixture
def engine():
    engine = PaddleOCREngine()
    engine.build(get_paddleocr_config())
    return engine