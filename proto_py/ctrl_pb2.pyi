from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CtrlMsg(_message.Message):
    __slots__ = ("sequence_number", "system_reset")
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESET_FIELD_NUMBER: _ClassVar[int]
    sequence_number: int
    system_reset: bool
    def __init__(self, sequence_number: _Optional[int] = ..., system_reset: bool = ...) -> None: ...
