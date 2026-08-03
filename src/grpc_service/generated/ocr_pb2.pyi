from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ItemErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ITEM_ERROR_CODE_UNSPECIFIED: _ClassVar[ItemErrorCode]
    INVALID_IMAGE: _ClassVar[ItemErrorCode]
    UNSUPPORTED_FORMAT: _ClassVar[ItemErrorCode]
    IMAGE_TOO_LARGE: _ClassVar[ItemErrorCode]
    PROCESSING_FAILED: _ClassVar[ItemErrorCode]

ITEM_ERROR_CODE_UNSPECIFIED: ItemErrorCode
INVALID_IMAGE: ItemErrorCode
UNSUPPORTED_FORMAT: ItemErrorCode
IMAGE_TOO_LARGE: ItemErrorCode
PROCESSING_FAILED: ItemErrorCode

class RequestContext(_message.Message):
    __slots__ = ("clientId", "requestId")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    CLIENTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    clientId: str
    def __init__(
        self, requestId: str | None = ..., clientId: str | None = ...
    ) -> None: ...

class ResponseContext(_message.Message):
    __slots__ = ("clientId", "requestId")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    CLIENTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    clientId: str
    def __init__(
        self, requestId: str | None = ..., clientId: str | None = ...
    ) -> None: ...

class OcrSingleProcessRequest(_message.Message):
    __slots__ = ("context", "image", "options")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    context: RequestContext
    image: ImageInput
    options: OcrOptions
    def __init__(
        self,
        context: RequestContext | _Mapping | None = ...,
        image: ImageInput | _Mapping | None = ...,
        options: OcrOptions | _Mapping | None = ...,
    ) -> None: ...

class OcrSingleProcessResponse(_message.Message):
    __slots__ = ("context", "result")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    context: ResponseContext
    result: ImageResult
    def __init__(
        self,
        context: ResponseContext | _Mapping | None = ...,
        result: ImageResult | _Mapping | None = ...,
    ) -> None: ...

class OcrBatchProcessRequest(_message.Message):
    __slots__ = ("context", "images", "options")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    context: RequestContext
    images: _containers.RepeatedCompositeFieldContainer[ImageInput]
    options: OcrOptions
    def __init__(
        self,
        context: RequestContext | _Mapping | None = ...,
        images: _Iterable[ImageInput | _Mapping] | None = ...,
        options: OcrOptions | _Mapping | None = ...,
    ) -> None: ...

class OcrBatchProcessResponse(_message.Message):
    __slots__ = ("context", "results")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    context: ResponseContext
    results: _containers.RepeatedCompositeFieldContainer[BatchItemResult]
    def __init__(
        self,
        context: ResponseContext | _Mapping | None = ...,
        results: _Iterable[BatchItemResult | _Mapping] | None = ...,
    ) -> None: ...

class BatchItemResult(_message.Message):
    __slots__ = ("error", "imageId", "result")
    IMAGEID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    imageId: str
    result: ImageResult
    error: ItemError
    def __init__(
        self,
        imageId: str | None = ...,
        result: ImageResult | _Mapping | None = ...,
        error: ItemError | _Mapping | None = ...,
    ) -> None: ...

class ImageInput(_message.Message):
    __slots__ = ("data", "filename", "imageId", "mimeType")
    IMAGEID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    imageId: str
    data: bytes
    mimeType: str
    filename: str
    def __init__(
        self,
        imageId: str | None = ...,
        data: bytes | None = ...,
        mimeType: str | None = ...,
        filename: str | None = ...,
    ) -> None: ...

class OcrOptions(_message.Message):
    __slots__ = ("language",)
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: str
    def __init__(self, language: str | None = ...) -> None: ...

class ImageResult(_message.Message):
    __slots__ = ("imageHeight", "imageWidth", "metadata", "regions")
    IMAGEWIDTH_FIELD_NUMBER: _ClassVar[int]
    IMAGEHEIGHT_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    imageWidth: int
    imageHeight: int
    regions: _containers.RepeatedCompositeFieldContainer[TextRegion]
    metadata: ProcessingMetadata
    def __init__(
        self,
        imageWidth: int | None = ...,
        imageHeight: int | None = ...,
        regions: _Iterable[TextRegion | _Mapping] | None = ...,
        metadata: ProcessingMetadata | _Mapping | None = ...,
    ) -> None: ...

class TextRegion(_message.Message):
    __slots__ = ("boundingBox", "detectionConfidence", "recognitionConfidence", "text")
    BOUNDINGBOX_FIELD_NUMBER: _ClassVar[int]
    DETECTIONCONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RECOGNITIONCONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    boundingBox: DetectionRegion
    detectionConfidence: float
    text: str
    recognitionConfidence: float
    def __init__(
        self,
        boundingBox: DetectionRegion | _Mapping | None = ...,
        detectionConfidence: float | None = ...,
        text: str | None = ...,
        recognitionConfidence: float | None = ...,
    ) -> None: ...

class DetectionRegion(_message.Message):
    __slots__ = ("bottomLeft", "bottomRight", "topLeft", "topRight")
    TOPLEFT_FIELD_NUMBER: _ClassVar[int]
    TOPRIGHT_FIELD_NUMBER: _ClassVar[int]
    BOTTOMRIGHT_FIELD_NUMBER: _ClassVar[int]
    BOTTOMLEFT_FIELD_NUMBER: _ClassVar[int]
    topLeft: Point
    topRight: Point
    bottomRight: Point
    bottomLeft: Point
    def __init__(
        self,
        topLeft: Point | _Mapping | None = ...,
        topRight: Point | _Mapping | None = ...,
        bottomRight: Point | _Mapping | None = ...,
        bottomLeft: Point | _Mapping | None = ...,
    ) -> None: ...

class Point(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: int | None = ..., y: int | None = ...) -> None: ...

class ProcessingMetadata(_message.Message):
    __slots__ = ("pipelineVersion", "processingTimeMs")
    PROCESSINGTIMEMS_FIELD_NUMBER: _ClassVar[int]
    PIPELINEVERSION_FIELD_NUMBER: _ClassVar[int]
    processingTimeMs: int
    pipelineVersion: str
    def __init__(
        self, processingTimeMs: int | None = ..., pipelineVersion: str | None = ...
    ) -> None: ...

class ItemError(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: ItemErrorCode
    message: str
    def __init__(
        self, code: ItemErrorCode | str | None = ..., message: str | None = ...
    ) -> None: ...

class GetCapabilitiesRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: RequestContext
    def __init__(self, context: RequestContext | _Mapping | None = ...) -> None: ...

class GetCapabilitiesResponse(_message.Message):
    __slots__ = (
        "context",
        "maxBatchSize",
        "maxImageHeight",
        "maxImageSizeBytes",
        "maxImageWidth",
        "pipelineVersion",
        "serviceName",
        "serviceVersion",
        "supportedMimeTypes",
        "supportsBatchProcessing",
    )
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    SERVICEVERSION_FIELD_NUMBER: _ClassVar[int]
    PIPELINEVERSION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTEDMIMETYPES_FIELD_NUMBER: _ClassVar[int]
    MAXIMAGEWIDTH_FIELD_NUMBER: _ClassVar[int]
    MAXIMAGEHEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAXIMAGESIZEBYTES_FIELD_NUMBER: _ClassVar[int]
    MAXBATCHSIZE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTSBATCHPROCESSING_FIELD_NUMBER: _ClassVar[int]
    context: ResponseContext
    serviceName: str
    serviceVersion: str
    pipelineVersion: str
    supportedMimeTypes: _containers.RepeatedScalarFieldContainer[str]
    maxImageWidth: int
    maxImageHeight: int
    maxImageSizeBytes: int
    maxBatchSize: int
    supportsBatchProcessing: bool
    def __init__(
        self,
        context: ResponseContext | _Mapping | None = ...,
        serviceName: str | None = ...,
        serviceVersion: str | None = ...,
        pipelineVersion: str | None = ...,
        supportedMimeTypes: _Iterable[str] | None = ...,
        maxImageWidth: int | None = ...,
        maxImageHeight: int | None = ...,
        maxImageSizeBytes: int | None = ...,
        maxBatchSize: int | None = ...,
        supportsBatchProcessing: bool | None = ...,
    ) -> None: ...
