from abc import ABC, abstractmethod
import numpy as np

from src.models import OCRResult


class BaseEngine(ABC):
    def __init__(self) -> None:
        self.detector = None
        self.recognizer = None

    @abstractmethod
    def build(self, config_data: dict) -> None:
        """Initialize and load all components (detector, recognizer, etc.)."""
        ...

    @abstractmethod
    def run(self, image: np.ndarray) -> list[OCRResult]:
        """
        Run the full OCR pipeline on a single image.

        Args:
            image: Input image as numpy array (H, W, C) in BGR format.

        Returns:
            List of OCRResult (DetectionResult + RecognitionResult) containing text, confidence, and bounding box.
        """
        ...