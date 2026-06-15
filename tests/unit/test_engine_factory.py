import pytest

from src.engine.engine_factory import EngineFactory
from src.engine.paddle_engine import PaddleOCREngine
from src.models import EngineType

def test_factory_returns_paddle_engine(mocker):
    mocker.patch.object(PaddleOCREngine, "build")
    engine = EngineFactory.create_engine(EngineType.PADDLE_OCR, config_data={})
    assert isinstance(engine, PaddleOCREngine)

def test_factory_invalid_type():
    with pytest.raises(ValueError):
        EngineType("INVALID")