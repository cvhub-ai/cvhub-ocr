# CvHub OCR

## Module Pipeline Process
```
Client
  ↓ gRPC request (image path / PDF path)
server.py
  ↓
preprocessor.py → convert to numpy array
  ↓
engine.py → PaddleOCR recognition
  ↓
schema.py → structured result
  ↓ gRPC response
Client
```