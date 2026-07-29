import pytest

from src.config.config_loader import get_paddleocr_config
from src.ocr.recognizer.paddle_recognizer import PaddleRecognizer
from src.ocr.detector.paddle_detector import PaddleDetector
from src.ocr.engine.engine_factory import EngineFactory
from src.ocr.engine.ocr_engine import OCREngine
from src.models.ocr_input import DetectorType, RecognizerType

def test_factory_returns_paddle_engine():
    # Arrange
    config_data = get_paddleocr_config()

    # Act
    engine = EngineFactory.create_engine(
        DetectorType.PADDLE, 
        RecognizerType.PADDLE, 
        config_data
    )

    # Assert
    assert isinstance(engine, OCREngine)
    assert isinstance(engine.detector, PaddleDetector)
    assert isinstance(engine.recognizer, PaddleRecognizer)

def test_detector_invalid_type() -> None:
    with pytest.raises(ValueError):
        DetectorType("INVALID")

def test_recognizer_invalid_type() -> None:
    with pytest.raises(ValueError):
        RecognizerType("INVALID")