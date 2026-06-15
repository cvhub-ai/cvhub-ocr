import numpy as np

class Utils:
    @staticmethod
    def extract_text_roi(corners: list[list[int]]) -> np.ndarray:
        text_roi = np.ones((3,3))
        return text_roi