import numpy as np

from src.recognizer.paddle_recognizer import PaddleRecognizer
from src.detector.paddle_detector import PaddleDetector
from src.models import DetectionResult, OCRResult, RecognitionResult
from src.engine.base_engine import BaseEngine
from src.utils.utils import Utils

class PaddleOCREngine(BaseEngine):
    def __init__(self) -> None:
        super().__init__()

    def build(self, config_data: dict) -> None:
        """Initialize and load all components (detector, recognizer, etc.)."""
        config_detector = config_data.get('detector', None)
        config_recognizer = config_data.get('recognizer', None)

        if (config_detector is None or config_recognizer is None):
            return;

        self.detector = PaddleDetector(config_detector)
        self.detector.load_model()

        self.recognizer = PaddleRecognizer(config_recognizer)
        self.recognizer.load_model()


    def run(self, image: np.ndarray) -> list[OCRResult]:
        """
        Run the full OCR pipeline on a single image.

        Args:
            image: Input image as numpy array (H, W, C) in BGR format.

        Returns:
            List of OCRResult (DetectionResult + RecognitionResult) containing text, confidence, and bounding box.
        """
        ocr_results: list[OCRResult] = []

        detection_results: list[DetectionResult] = self.detector.detect(image)
    
        for detection_result in detection_results:
            if detection_result.confidence < 0.5:
                continue

            text_roi = Utils.extract_text_roi(image, detection_result.bbox)
            recognition_result: RecognitionResult|None = self.recognizer.recognize(text_roi)
            if recognition_result is None:
                continue

            ocr_results.append(OCRResult(
                det_result=detection_result,
                rec_result=recognition_result
            ))
        return ocr_results