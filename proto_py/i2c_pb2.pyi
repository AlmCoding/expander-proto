from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class I2cId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    I2C0: _ClassVar[I2cId]
    I2C1: _ClassVar[I2cId]

class I2cMasterStatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MST_NOT_INIT: _ClassVar[I2cMasterStatusCode]
    MST_NO_SPACE: _ClassVar[I2cMasterStatusCode]
    MST_PENDING: _ClassVar[I2cMasterStatusCode]
    MST_ONGOING: _ClassVar[I2cMasterStatusCode]
    MST_COMPLETE: _ClassVar[I2cMasterStatusCode]
    MST_SLAVE_BUSY: _ClassVar[I2cMasterStatusCode]
    MST_INTERFACE_ERROR: _ClassVar[I2cMasterStatusCode]

class I2cSlaveStatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLV_NOT_INIT: _ClassVar[I2cSlaveStatusCode]
    SLV_NO_SPACE: _ClassVar[I2cSlaveStatusCode]
    SLV_PENDING: _ClassVar[I2cSlaveStatusCode]
    SLV_COMPLETE: _ClassVar[I2cSlaveStatusCode]
    SLV_SLAVE_BUSY: _ClassVar[I2cSlaveStatusCode]
    SLV_BAD_REQUEST: _ClassVar[I2cSlaveStatusCode]
    SLV_INTERFACE_ERROR: _ClassVar[I2cSlaveStatusCode]
I2C0: I2cId
I2C1: I2cId
MST_NOT_INIT: I2cMasterStatusCode
MST_NO_SPACE: I2cMasterStatusCode
MST_PENDING: I2cMasterStatusCode
MST_ONGOING: I2cMasterStatusCode
MST_COMPLETE: I2cMasterStatusCode
MST_SLAVE_BUSY: I2cMasterStatusCode
MST_INTERFACE_ERROR: I2cMasterStatusCode
SLV_NOT_INIT: I2cSlaveStatusCode
SLV_NO_SPACE: I2cSlaveStatusCode
SLV_PENDING: I2cSlaveStatusCode
SLV_COMPLETE: I2cSlaveStatusCode
SLV_SLAVE_BUSY: I2cSlaveStatusCode
SLV_BAD_REQUEST: I2cSlaveStatusCode
SLV_INTERFACE_ERROR: I2cSlaveStatusCode

class I2cConfig(_message.Message):
    __slots__ = ("clock_rate", "device_addr", "pullups_enabled")
    CLOCK_RATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ADDR_FIELD_NUMBER: _ClassVar[int]
    PULLUPS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    clock_rate: int
    device_addr: int
    pullups_enabled: bool
    def __init__(self, clock_rate: _Optional[int] = ..., device_addr: _Optional[int] = ..., pullups_enabled: bool = ...) -> None: ...

class I2cMasterRequest(_message.Message):
    __slots__ = ("request_id", "slave_addr", "write_data", "read_size", "sequence_id", "sequence_idx")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_ADDR_FIELD_NUMBER: _ClassVar[int]
    WRITE_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_SIZE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_IDX_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    slave_addr: int
    write_data: bytes
    read_size: int
    sequence_id: int
    sequence_idx: int
    def __init__(self, request_id: _Optional[int] = ..., slave_addr: _Optional[int] = ..., write_data: _Optional[bytes] = ..., read_size: _Optional[int] = ..., sequence_id: _Optional[int] = ..., sequence_idx: _Optional[int] = ...) -> None: ...

class I2cMasterStatus(_message.Message):
    __slots__ = ("request_id", "status_code", "read_data", "queue_space", "buffer_space1", "buffer_space2")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    READ_DATA_FIELD_NUMBER: _ClassVar[int]
    QUEUE_SPACE_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SPACE1_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SPACE2_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    status_code: I2cMasterStatusCode
    read_data: bytes
    queue_space: int
    buffer_space1: int
    buffer_space2: int
    def __init__(self, request_id: _Optional[int] = ..., status_code: _Optional[_Union[I2cMasterStatusCode, str]] = ..., read_data: _Optional[bytes] = ..., queue_space: _Optional[int] = ..., buffer_space1: _Optional[int] = ..., buffer_space2: _Optional[int] = ...) -> None: ...

class I2cSlaveRequest(_message.Message):
    __slots__ = ("request_id", "write_data", "read_size", "write_addr", "read_addr")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    WRITE_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_SIZE_FIELD_NUMBER: _ClassVar[int]
    WRITE_ADDR_FIELD_NUMBER: _ClassVar[int]
    READ_ADDR_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    write_data: bytes
    read_size: int
    write_addr: int
    read_addr: int
    def __init__(self, request_id: _Optional[int] = ..., write_data: _Optional[bytes] = ..., read_size: _Optional[int] = ..., write_addr: _Optional[int] = ..., read_addr: _Optional[int] = ...) -> None: ...

class I2cSlaveStatus(_message.Message):
    __slots__ = ("request_id", "access_id", "status_code", "write_size", "read_size", "write_addr", "read_addr", "mem_data", "queue_space")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    WRITE_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_SIZE_FIELD_NUMBER: _ClassVar[int]
    WRITE_ADDR_FIELD_NUMBER: _ClassVar[int]
    READ_ADDR_FIELD_NUMBER: _ClassVar[int]
    MEM_DATA_FIELD_NUMBER: _ClassVar[int]
    QUEUE_SPACE_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    access_id: int
    status_code: I2cSlaveStatusCode
    write_size: int
    read_size: int
    write_addr: int
    read_addr: int
    mem_data: bytes
    queue_space: int
    def __init__(self, request_id: _Optional[int] = ..., access_id: _Optional[int] = ..., status_code: _Optional[_Union[I2cSlaveStatusCode, str]] = ..., write_size: _Optional[int] = ..., read_size: _Optional[int] = ..., write_addr: _Optional[int] = ..., read_addr: _Optional[int] = ..., mem_data: _Optional[bytes] = ..., queue_space: _Optional[int] = ...) -> None: ...

class I2cMsg(_message.Message):
    __slots__ = ("i2c_id", "sequence_number", "cfg", "master_request", "master_status", "slave_request", "slave_status")
    I2C_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CFG_FIELD_NUMBER: _ClassVar[int]
    MASTER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MASTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SLAVE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SLAVE_STATUS_FIELD_NUMBER: _ClassVar[int]
    i2c_id: I2cId
    sequence_number: int
    cfg: I2cConfig
    master_request: I2cMasterRequest
    master_status: I2cMasterStatus
    slave_request: I2cSlaveRequest
    slave_status: I2cSlaveStatus
    def __init__(self, i2c_id: _Optional[_Union[I2cId, str]] = ..., sequence_number: _Optional[int] = ..., cfg: _Optional[_Union[I2cConfig, _Mapping]] = ..., master_request: _Optional[_Union[I2cMasterRequest, _Mapping]] = ..., master_status: _Optional[_Union[I2cMasterStatus, _Mapping]] = ..., slave_request: _Optional[_Union[I2cSlaveRequest, _Mapping]] = ..., slave_status: _Optional[_Union[I2cSlaveStatus, _Mapping]] = ...) -> None: ...
