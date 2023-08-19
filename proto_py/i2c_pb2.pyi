from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class I2cId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    I2C0: _ClassVar[I2cId]
    I2C1: _ClassVar[I2cId]
I2C0: I2cId
I2C1: I2cId

class I2cConfig(_message.Message):
    __slots__ = ["clock_rate"]
    CLOCK_RATE_FIELD_NUMBER: _ClassVar[int]
    clock_rate: int
    def __init__(self, clock_rate: _Optional[int] = ...) -> None: ...

class I2cMasterData(_message.Message):
    __slots__ = ["request_id", "slave_addr", "read_size", "data"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_ADDR_FIELD_NUMBER: _ClassVar[int]
    READ_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    slave_addr: int
    read_size: int
    data: bytes
    def __init__(self, request_id: _Optional[int] = ..., slave_addr: _Optional[int] = ..., read_size: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class I2cStatus(_message.Message):
    __slots__ = ["master_queue_space", "master_buffer_space", "master_overflow"]
    MASTER_QUEUE_SPACE_FIELD_NUMBER: _ClassVar[int]
    MASTER_BUFFER_SPACE_FIELD_NUMBER: _ClassVar[int]
    MASTER_OVERFLOW_FIELD_NUMBER: _ClassVar[int]
    master_queue_space: int
    master_buffer_space: int
    master_overflow: bool
    def __init__(self, master_queue_space: _Optional[int] = ..., master_buffer_space: _Optional[int] = ..., master_overflow: bool = ...) -> None: ...

class I2cMsg(_message.Message):
    __slots__ = ["i2c_id", "sequence_number", "cfg_msg", "data_msg", "status_msg"]
    I2C_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CFG_MSG_FIELD_NUMBER: _ClassVar[int]
    DATA_MSG_FIELD_NUMBER: _ClassVar[int]
    STATUS_MSG_FIELD_NUMBER: _ClassVar[int]
    i2c_id: I2cId
    sequence_number: int
    cfg_msg: I2cConfig
    data_msg: I2cMasterData
    status_msg: I2cStatus
    def __init__(self, i2c_id: _Optional[_Union[I2cId, str]] = ..., sequence_number: _Optional[int] = ..., cfg_msg: _Optional[_Union[I2cConfig, _Mapping]] = ..., data_msg: _Optional[_Union[I2cMasterData, _Mapping]] = ..., status_msg: _Optional[_Union[I2cStatus, _Mapping]] = ...) -> None: ...
