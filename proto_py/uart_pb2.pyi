from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UartId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UART1: _ClassVar[UartId]
    UART2: _ClassVar[UartId]
UART1: UartId
UART2: UartId

class UartConfig(_message.Message):
    __slots__ = ["uart_id", "baud_rate"]
    UART_ID_FIELD_NUMBER: _ClassVar[int]
    BAUD_RATE_FIELD_NUMBER: _ClassVar[int]
    uart_id: UartId
    baud_rate: int
    def __init__(self, uart_id: _Optional[_Union[UartId, str]] = ..., baud_rate: _Optional[int] = ...) -> None: ...

class UartData(_message.Message):
    __slots__ = ["uart_id", "size", "data"]
    UART_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    uart_id: UartId
    size: int
    data: bytes
    def __init__(self, uart_id: _Optional[_Union[UartId, str]] = ..., size: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
