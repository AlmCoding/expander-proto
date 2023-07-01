from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONFIG: _ClassVar[MsgType]
    DATA: _ClassVar[MsgType]

class GpioMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INPUT_PULLDOWN: _ClassVar[GpioMode]
    INPUT_PULLUP: _ClassVar[GpioMode]
    INPUT_NOPULL: _ClassVar[GpioMode]
    OUTPUT_PUSHPULL: _ClassVar[GpioMode]
    OUTPUT_OPENDRAIN: _ClassVar[GpioMode]
CONFIG: MsgType
DATA: MsgType
INPUT_PULLDOWN: GpioMode
INPUT_PULLUP: GpioMode
INPUT_NOPULL: GpioMode
OUTPUT_PUSHPULL: GpioMode
OUTPUT_OPENDRAIN: GpioMode

class GpioConfig(_message.Message):
    __slots__ = ["gpio1", "gpio2", "gpio3", "gpio4"]
    GPIO1_FIELD_NUMBER: _ClassVar[int]
    GPIO2_FIELD_NUMBER: _ClassVar[int]
    GPIO3_FIELD_NUMBER: _ClassVar[int]
    GPIO4_FIELD_NUMBER: _ClassVar[int]
    gpio1: GpioMode
    gpio2: GpioMode
    gpio3: GpioMode
    gpio4: GpioMode
    def __init__(self, gpio1: _Optional[_Union[GpioMode, str]] = ..., gpio2: _Optional[_Union[GpioMode, str]] = ..., gpio3: _Optional[_Union[GpioMode, str]] = ..., gpio4: _Optional[_Union[GpioMode, str]] = ...) -> None: ...

class GpioData(_message.Message):
    __slots__ = ["gpio1", "gpio2", "gpio3", "gpio4"]
    GPIO1_FIELD_NUMBER: _ClassVar[int]
    GPIO2_FIELD_NUMBER: _ClassVar[int]
    GPIO3_FIELD_NUMBER: _ClassVar[int]
    GPIO4_FIELD_NUMBER: _ClassVar[int]
    gpio1: bool
    gpio2: bool
    gpio3: bool
    gpio4: bool
    def __init__(self, gpio1: bool = ..., gpio2: bool = ..., gpio3: bool = ..., gpio4: bool = ...) -> None: ...

class GpioMsg(_message.Message):
    __slots__ = ["sequence_number", "cfg_msg", "data_msg"]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CFG_MSG_FIELD_NUMBER: _ClassVar[int]
    DATA_MSG_FIELD_NUMBER: _ClassVar[int]
    sequence_number: int
    cfg_msg: GpioConfig
    data_msg: GpioData
    def __init__(self, sequence_number: _Optional[int] = ..., cfg_msg: _Optional[_Union[GpioConfig, _Mapping]] = ..., data_msg: _Optional[_Union[GpioData, _Mapping]] = ...) -> None: ...
