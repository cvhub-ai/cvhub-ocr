import pytest
import numpy as np
from src.engine.paddle_engine import PaddleOCREngine
from src.config.config_loader import get_paddleocr_config
from src.models import OCRResult

class TestPaddleEngine:
    def test_paddle_engine_build(self, engine):
        assert engine.detector is not None
        assert engine.recognizer is not None

    def test_paddle_engine_run(self, det_test_image, engine):
        orignial = det_test_image.copy()
        ocr_results = engine.run(det_test_image)
        assert isinstance(ocr_results, list)
        assert all(isinstance(res, OCRResult) for res in ocr_results)
        assert np.array_equal(orignial, det_test_image)
