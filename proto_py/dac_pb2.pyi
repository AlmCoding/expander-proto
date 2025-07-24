from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DacMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DAC_MODE_STATIC: _ClassVar[DacMode]
    DAC_MODE_PERIODIC: _ClassVar[DacMode]
    DAC_MODE_STREAMING: _ClassVar[DacMode]

class DacConfigStatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CFG_NOT_INIT: _ClassVar[DacConfigStatusCode]
    CFG_SUCCESS: _ClassVar[DacConfigStatusCode]
    CFG_INVALID_MODE: _ClassVar[DacConfigStatusCode]
    CFG_INVALID_SAMPLING_RATE: _ClassVar[DacConfigStatusCode]
    CFG_INVALID_PERIODIC_SAMPLES: _ClassVar[DacConfigStatusCode]
    CFG_INTERFACE_ERROR: _ClassVar[DacConfigStatusCode]

class DacDataStatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_NOT_INIT: _ClassVar[DacDataStatusCode]
    DATA_SUCCESS: _ClassVar[DacDataStatusCode]
    DATA_BAD_REQUEST: _ClassVar[DacDataStatusCode]
    DATA_BUFFER_OVERFLOW: _ClassVar[DacDataStatusCode]
    DATA_INTERFACE_ERROR: _ClassVar[DacDataStatusCode]
DAC_MODE_STATIC: DacMode
DAC_MODE_PERIODIC: DacMode
DAC_MODE_STREAMING: DacMode
CFG_NOT_INIT: DacConfigStatusCode
CFG_SUCCESS: DacConfigStatusCode
CFG_INVALID_MODE: DacConfigStatusCode
CFG_INVALID_SAMPLING_RATE: DacConfigStatusCode
CFG_INVALID_PERIODIC_SAMPLES: DacConfigStatusCode
CFG_INTERFACE_ERROR: DacConfigStatusCode
DATA_NOT_INIT: DacDataStatusCode
DATA_SUCCESS: DacDataStatusCode
DATA_BAD_REQUEST: DacDataStatusCode
DATA_BUFFER_OVERFLOW: DacDataStatusCode
DATA_INTERFACE_ERROR: DacDataStatusCode

class DacConfigRequest(_message.Message):
    __slots__ = ("request_id", "mode", "sampling_rate", "periodic_samples")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_RATE_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    mode: DacMode
    sampling_rate: int
    periodic_samples: int
    def __init__(self, request_id: _Optional[int] = ..., mode: _Optional[_Union[DacMode, str]] = ..., sampling_rate: _Optional[int] = ..., periodic_samples: _Optional[int] = ...) -> None: ...

class DacConfigStatus(_message.Message):
    __slots__ = ("request_id", "status_code")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    status_code: DacConfigStatusCode
    def __init__(self, request_id: _Optional[int] = ..., status_code: _Optional[_Union[DacConfigStatusCode, str]] = ...) -> None: ...

class DacDataRequest(_message.Message):
    __slots__ = ("request_id", "run", "data_ch1", "data_ch2")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    DATA_CH1_FIELD_NUMBER: _ClassVar[int]
    DATA_CH2_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    run: bool
    data_ch1: bytes
    data_ch2: bytes
    def __init__(self, request_id: _Optional[int] = ..., run: bool = ..., data_ch1: _Optional[bytes] = ..., data_ch2: _Optional[bytes] = ...) -> None: ...

class DacDataStatus(_message.Message):
    __slots__ = ("request_id", "status_code", "queue_space", "buffer_space_ch1", "buffer_space_ch2")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    QUEUE_SPACE_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SPACE_CH1_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SPACE_CH2_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    status_code: DacDataStatusCode
    queue_space: int
    buffer_space_ch1: int
    buffer_space_ch2: int
    def __init__(self, request_id: _Optional[int] = ..., status_code: _Optional[_Union[DacDataStatusCode, str]] = ..., queue_space: _Optional[int] = ..., buffer_space_ch1: _Optional[int] = ..., buffer_space_ch2: _Optional[int] = ...) -> None: ...

class DacMsg(_message.Message):
    __slots__ = ("sequence_number", "config_request", "config_status", "data_request", "data_status")
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONFIG_STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATA_STATUS_FIELD_NUMBER: _ClassVar[int]
    sequence_number: int
    config_request: DacConfigRequest
    config_status: DacConfigStatus
    data_request: DacDataRequest
    data_status: DacDataStatus
    def __init__(self, sequence_number: _Optional[int] = ..., config_request: _Optional[_Union[DacConfigRequest, _Mapping]] = ..., config_status: _Optional[_Union[DacConfigStatus, _Mapping]] = ..., data_request: _Optional[_Union[DacDataRequest, _Mapping]] = ..., data_status: _Optional[_Union[DacDataStatus, _Mapping]] = ...) -> None: ...
