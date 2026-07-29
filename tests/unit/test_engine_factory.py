import pytest

from src.ocr.engine.engine_factory import EngineFactory
from src.ocr.engine.paddle_engine import PaddleOCREngine
from src.models.ocr_input import EngineType

def test_factory_returns_paddle_engine(mocker):
    mocker.patch.object(PaddleOCREngine, "build")
    engine = EngineFactory.create_engine(EngineType.PADDLE_OCR, config_data={})
    assert isinstance(engine, PaddleOCREngine)

def test_factory_invalid_type():
    with pytest.raises(ValueError):
        EngineType("INVALID")