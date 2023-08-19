from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UartId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UART0: _ClassVar[UartId]
    UART1: _ClassVar[UartId]
UART0: UartId
UART1: UartId

class UartConfig(_message.Message):
    __slots__ = ["baud_rate"]
    BAUD_RATE_FIELD_NUMBER: _ClassVar[int]
    baud_rate: int
    def __init__(self, baud_rate: _Optional[int] = ...) -> None: ...

class UartData(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class UartStatus(_message.Message):
    __slots__ = ["rx_overflow", "tx_overflow", "tx_complete", "rx_space", "tx_space"]
    RX_OVERFLOW_FIELD_NUMBER: _ClassVar[int]
    TX_OVERFLOW_FIELD_NUMBER: _ClassVar[int]
    TX_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    RX_SPACE_FIELD_NUMBER: _ClassVar[int]
    TX_SPACE_FIELD_NUMBER: _ClassVar[int]
    rx_overflow: bool
    tx_overflow: bool
    tx_complete: bool
    rx_space: int
    tx_space: int
    def __init__(self, rx_overflow: bool = ..., tx_overflow: bool = ..., tx_complete: bool = ..., rx_space: _Optional[int] = ..., tx_space: _Optional[int] = ...) -> None: ...

class UartMsg(_message.Message):
    __slots__ = ["uart_id", "sequence_number", "cfg_msg", "data_msg", "status_msg"]
    UART_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CFG_MSG_FIELD_NUMBER: _ClassVar[int]
    DATA_MSG_FIELD_NUMBER: _ClassVar[int]
    STATUS_MSG_FIELD_NUMBER: _ClassVar[int]
    uart_id: UartId
    sequence_number: int
    cfg_msg: UartConfig
    data_msg: UartData
    status_msg: UartStatus
    def __init__(self, uart_id: _Optional[_Union[UartId, str]] = ..., sequence_number: _Optional[int] = ..., cfg_msg: _Optional[_Union[UartConfig, _Mapping]] = ..., data_msg: _Optional[_Union[UartData, _Mapping]] = ..., status_msg: _Optional[_Union[UartStatus, _Mapping]] = ...) -> None: ...
