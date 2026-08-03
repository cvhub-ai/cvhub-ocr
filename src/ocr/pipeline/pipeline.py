import numpy as np

from src.models.ocr_result import OcrResult
from src.ocr.engine.ocr_engine import OcrEngine
from src.ocr.preprocess.image_processor import Preprocessor


class OcrPipeline:
    def __init__(self, ocrEngine: OcrEngine) -> None:
        self._preProcessor = Preprocessor()
        self._ocrEngine = ocrEngine

    def process(self, image: np.ndarray) -> list[OcrResult]:
        # step 1: pre processing
        self._preProcessor.set_image(image)
        imageProcessed = (
            self._preProcessor.gaussian_denoise().laplacian_sharpen().result()
        )

        # setp 2: ocr engine run
        ocrResults = self._ocrEngine.run(imageProcessed)

        return ocrResults
