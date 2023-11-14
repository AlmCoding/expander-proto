# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: i2c.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ti2c.proto\x12\ti2c_proto\"4\n\tI2cConfig\x12\x12\n\nclock_rate\x18\x01 \x01(\r\x12\x13\n\x0b\x64\x65vice_addr\x18\x02 \x01(\r\"\x8c\x01\n\x10I2cMasterRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x12\n\nslave_addr\x18\x02 \x01(\r\x12\x12\n\nwrite_data\x18\x03 \x01(\x0c\x12\x11\n\tread_size\x18\x04 \x01(\r\x12\x13\n\x0bsequence_id\x18\x05 \x01(\r\x12\x14\n\x0csequence_idx\x18\x06 \x01(\r\"\xb0\x01\n\x0fI2cMasterStatus\x12\x33\n\x0bstatus_code\x18\x01 \x01(\x0e\x32\x1e.i2c_proto.I2cMasterStatusCode\x12\x12\n\nrequest_id\x18\x02 \x01(\r\x12\x11\n\tread_data\x18\x03 \x01(\x0c\x12\x13\n\x0bqueue_space\x18\x04 \x01(\r\x12\x15\n\rbuffer_space1\x18\x05 \x01(\r\x12\x15\n\rbuffer_space2\x18\x06 \x01(\r\"\xdb\x01\n\x06I2cMsg\x12 \n\x06i2c_id\x18\x01 \x01(\x0e\x32\x10.i2c_proto.I2cId\x12\x17\n\x0fsequence_number\x18\x02 \x01(\r\x12#\n\x03\x63\x66g\x18\x03 \x01(\x0b\x32\x14.i2c_proto.I2cConfigH\x00\x12\x35\n\x0emaster_request\x18\x04 \x01(\x0b\x32\x1b.i2c_proto.I2cMasterRequestH\x00\x12\x33\n\rmaster_status\x18\x05 \x01(\x0b\x32\x1a.i2c_proto.I2cMasterStatusH\x00\x42\x05\n\x03msg*\x1b\n\x05I2cId\x12\x08\n\x04I2C0\x10\x00\x12\x08\n\x04I2C1\x10\x01*~\n\x13I2cMasterStatusCode\x12\x0c\n\x08NOT_INIT\x10\x00\x12\x0c\n\x08NO_SPACE\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07ONGOING\x10\x03\x12\x0c\n\x08\x43OMPLETE\x10\x04\x12\x0e\n\nSLAVE_BUSY\x10\x05\x12\x13\n\x0fINTERFACE_ERROR\x10\x06\x42\x02H\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'i2c_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\003'
  _globals['_I2CID']._serialized_start=622
  _globals['_I2CID']._serialized_end=649
  _globals['_I2CMASTERSTATUSCODE']._serialized_start=651
  _globals['_I2CMASTERSTATUSCODE']._serialized_end=777
  _globals['_I2CCONFIG']._serialized_start=24
  _globals['_I2CCONFIG']._serialized_end=76
  _globals['_I2CMASTERREQUEST']._serialized_start=79
  _globals['_I2CMASTERREQUEST']._serialized_end=219
  _globals['_I2CMASTERSTATUS']._serialized_start=222
  _globals['_I2CMASTERSTATUS']._serialized_end=398
  _globals['_I2CMSG']._serialized_start=401
  _globals['_I2CMSG']._serialized_end=620
# @@protoc_insertion_point(module_scope)
