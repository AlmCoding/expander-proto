from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UartId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UART1: _ClassVar[UartId]
    UART2: _ClassVar[UartId]

class MsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONFIG: _ClassVar[MsgType]
    DATA: _ClassVar[MsgType]
UART1: UartId
UART2: UartId
CONFIG: MsgType
DATA: MsgType

class UartConfig(_message.Message):
    __slots__ = ["id", "baudrate"]
    ID_FIELD_NUMBER: _ClassVar[int]
    BAUDRATE_FIELD_NUMBER: _ClassVar[int]
    id: UartId
    baudrate: int
    def __init__(self, id: _Optional[_Union[UartId, str]] = ..., baudrate: _Optional[int] = ...) -> None: ...

class UartData(_message.Message):
    __slots__ = ["id", "data"]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: UartId
    data: bytes
    def __init__(self, id: _Optional[_Union[UartId, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class UartMsg(_message.Message):
    __slots__ = ["type", "cfg", "data"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CFG_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: MsgType
    cfg: UartConfig
    data: UartData
    def __init__(self, type: _Optional[_Union[MsgType, str]] = ..., cfg: _Optional[_Union[UartConfig, _Mapping]] = ..., data: _Optional[_Union[UartData, _Mapping]] = ...) -> None: ...
