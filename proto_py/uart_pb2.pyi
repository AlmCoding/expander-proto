from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Peripheral(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UART1: _ClassVar[Peripheral]
    UART2: _ClassVar[Peripheral]
UART1: Peripheral
UART2: Peripheral

class UartConfig(_message.Message):
    __slots__ = ["peripheral", "baud_rate"]
    PERIPHERAL_FIELD_NUMBER: _ClassVar[int]
    BAUD_RATE_FIELD_NUMBER: _ClassVar[int]
    peripheral: Peripheral
    baud_rate: int
    def __init__(self, peripheral: _Optional[_Union[Peripheral, str]] = ..., baud_rate: _Optional[int] = ...) -> None: ...

class UartTransmit(_message.Message):
    __slots__ = ["peripheral"]
    PERIPHERAL_FIELD_NUMBER: _ClassVar[int]
    peripheral: Peripheral
    def __init__(self, peripheral: _Optional[_Union[Peripheral, str]] = ...) -> None: ...

class UartReceive(_message.Message):
    __slots__ = ["peripheral"]
    PERIPHERAL_FIELD_NUMBER: _ClassVar[int]
    peripheral: Peripheral
    def __init__(self, peripheral: _Optional[_Union[Peripheral, str]] = ...) -> None: ...
