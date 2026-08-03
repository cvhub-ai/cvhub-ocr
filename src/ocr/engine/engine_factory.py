from src.models.ocr_input import DetectorType, RecognizerType
from src.ocr.engine.ocr_engine import OCREngine


class EngineFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_engine(
        detector_type: DetectorType, recognizer_type: RecognizerType, config_data: dict
    ) -> OCREngine:
        detector_config = config_data.get("detector", None)
        recognizer_config = config_data.get("recognizer", None)

        if detector_config is None:
            raise ValueError("Detector config is missing")

        if recognizer_config is None:
            raise ValueError("Recognizer config is missing")

        engine = OCREngine()

        EngineFactory._create_engine_detector(engine, detector_type, detector_config)
        EngineFactory._create_engine_recognizer(
            engine, recognizer_type, recognizer_config
        )

        return engine

    @staticmethod
    def _create_engine_detector(
        engine: OCREngine, detector_type: DetectorType, detector_config: dict
    ):
        if detector_type == DetectorType.PADDLE:
            from src.ocr.detector.paddle_detector import PaddleDetector

            engine.detector = PaddleDetector(detector_config)
            engine.detector.load_model()

    @staticmethod
    def _create_engine_recognizer(
        engine: OCREngine, recognizer_type: RecognizerType, recognizer_config: dict
    ):
        if recognizer_type == RecognizerType.PADDLE:
            from src.ocr.recognizer.paddle_recognizer import PaddleRecognizer

            engine.recognizer = PaddleRecognizer(recognizer_config)
            engine.recognizer.load_model()
