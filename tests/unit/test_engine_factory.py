import pytest

from ocr.engine.engine_factory import EngineFactory
from ocr.engine.paddle_engine import PaddleOCREngine
from models.ocr_result import EngineType

def test_factory_returns_paddle_engine(mocker):
    mocker.patch.object(PaddleOCREngine, "build")
    engine = EngineFactory.create_engine(EngineType.PADDLE_OCR, config_data={})
    assert isinstance(engine, PaddleOCREngine)

def test_factory_invalid_type():
    with pytest.raises(ValueError):
        EngineType("INVALID")