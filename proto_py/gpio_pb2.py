# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gpio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngpio.proto\x12\ngpio_proto\"\xa0\x01\n\nGpioConfig\x12#\n\x05gpio1\x18\x01 \x01(\x0e\x32\x14.gpio_proto.GpioMode\x12#\n\x05gpio2\x18\x02 \x01(\x0e\x32\x14.gpio_proto.GpioMode\x12#\n\x05gpio3\x18\x03 \x01(\x0e\x32\x14.gpio_proto.GpioMode\x12#\n\x05gpio4\x18\x04 \x01(\x0e\x32\x14.gpio_proto.GpioMode\"F\n\x08GpioData\x12\r\n\x05gpio1\x18\x01 \x01(\x08\x12\r\n\x05gpio2\x18\x02 \x01(\x08\x12\r\n\x05gpio3\x18\x03 \x01(\x08\x12\r\n\x05gpio4\x18\x04 \x01(\x08\"~\n\x07GpioMsg\x12\x17\n\x0fsequence_number\x18\x01 \x01(\r\x12)\n\x07\x63\x66g_msg\x18\x02 \x01(\x0b\x32\x16.gpio_proto.GpioConfigH\x00\x12(\n\x08\x64\x61ta_msg\x18\x03 \x01(\x0b\x32\x14.gpio_proto.GpioDataH\x00\x42\x05\n\x03msg*\x1f\n\x07MsgType\x12\n\n\x06\x43ONFIG\x10\x00\x12\x08\n\x04\x44\x41TA\x10\x01*m\n\x08GpioMode\x12\x12\n\x0eINPUT_PULLDOWN\x10\x00\x12\x10\n\x0cINPUT_PULLUP\x10\x01\x12\x10\n\x0cINPUT_NOPULL\x10\x02\x12\x13\n\x0fOUTPUT_PUSHPULL\x10\x03\x12\x14\n\x10OUTPUT_OPENDRAIN\x10\x04\x42\x02H\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gpio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _globals['_MSGTYPE']._serialized_start=389
  _globals['_MSGTYPE']._serialized_end=420
  _globals['_GPIOMODE']._serialized_start=422
  _globals['_GPIOMODE']._serialized_end=531
  _globals['_GPIOCONFIG']._serialized_start=27
  _globals['_GPIOCONFIG']._serialized_end=187
  _globals['_GPIODATA']._serialized_start=189
  _globals['_GPIODATA']._serialized_end=259
  _globals['_GPIOMSG']._serialized_start=261
  _globals['_GPIOMSG']._serialized_end=387
# @@protoc_insertion_point(module_scope)
