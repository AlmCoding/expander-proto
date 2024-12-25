# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: i2c.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'i2c.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ti2c.proto\x12\ti2c_proto\"\xcb\x01\n\x10I2cConfigRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x12\n\nclock_freq\x18\x02 \x01(\r\x12\x12\n\nslave_addr\x18\x03 \x01(\r\x12\x31\n\x10slave_addr_width\x18\x04 \x01(\x0e\x32\x17.i2c_proto.AddressWidth\x12/\n\x0emem_addr_width\x18\x05 \x01(\x0e\x32\x17.i2c_proto.AddressWidth\x12\x17\n\x0fpullups_enabled\x18\x06 \x01(\x08\"Z\n\x0fI2cConfigStatus\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x33\n\x0bstatus_code\x18\x02 \x01(\x0e\x32\x1e.i2c_proto.I2cConfigStatusCode\"\x8c\x01\n\x10I2cMasterRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x12\n\nslave_addr\x18\x02 \x01(\r\x12\x12\n\nwrite_data\x18\x03 \x01(\x0c\x12\x11\n\tread_size\x18\x04 \x01(\r\x12\x13\n\x0bsequence_id\x18\x05 \x01(\r\x12\x14\n\x0csequence_idx\x18\x06 \x01(\r\"\xbc\x01\n\x0fI2cMasterStatus\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12-\n\x0bstatus_code\x18\x02 \x01(\x0e\x32\x18.i2c_proto.I2cStatusCode\x12\x11\n\tread_data\x18\x03 \x01(\x0c\x12\x10\n\x08nack_idx\x18\x04 \x01(\r\x12\x13\n\x0bqueue_space\x18\x05 \x01(\r\x12\x15\n\rbuffer_space1\x18\x06 \x01(\r\x12\x15\n\rbuffer_space2\x18\x07 \x01(\r\"s\n\x0fI2cSlaveRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x12\n\nwrite_data\x18\x02 \x01(\x0c\x12\x11\n\tread_size\x18\x03 \x01(\r\x12\x12\n\nwrite_addr\x18\x04 \x01(\r\x12\x11\n\tread_addr\x18\x05 \x01(\r\"{\n\x0eI2cSlaveStatus\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12-\n\x0bstatus_code\x18\x02 \x01(\x0e\x32\x18.i2c_proto.I2cStatusCode\x12\x11\n\tread_data\x18\x03 \x01(\x0c\x12\x13\n\x0bqueue_space\x18\x04 \x01(\r\"\x94\x01\n\x14I2cSlaveNotification\x12\x11\n\taccess_id\x18\x01 \x01(\r\x12-\n\x0bstatus_code\x18\x02 \x01(\x0e\x32\x18.i2c_proto.I2cStatusCode\x12\x12\n\nwrite_data\x18\x04 \x01(\x0c\x12\x11\n\tread_data\x18\x05 \x01(\x0c\x12\x13\n\x0bqueue_space\x18\x06 \x01(\r\"\xc9\x03\n\x06I2cMsg\x12 \n\x06i2c_id\x18\x01 \x01(\x0e\x32\x10.i2c_proto.I2cId\x12\x17\n\x0fsequence_number\x18\x02 \x01(\r\x12\x35\n\x0e\x63onfig_request\x18\x03 \x01(\x0b\x32\x1b.i2c_proto.I2cConfigRequestH\x00\x12\x33\n\rconfig_status\x18\x04 \x01(\x0b\x32\x1a.i2c_proto.I2cConfigStatusH\x00\x12\x35\n\x0emaster_request\x18\x05 \x01(\x0b\x32\x1b.i2c_proto.I2cMasterRequestH\x00\x12\x33\n\rmaster_status\x18\x06 \x01(\x0b\x32\x1a.i2c_proto.I2cMasterStatusH\x00\x12\x33\n\rslave_request\x18\x07 \x01(\x0b\x32\x1a.i2c_proto.I2cSlaveRequestH\x00\x12\x31\n\x0cslave_status\x18\x08 \x01(\x0b\x32\x19.i2c_proto.I2cSlaveStatusH\x00\x12=\n\x12slave_notification\x18\t \x01(\x0b\x32\x1f.i2c_proto.I2cSlaveNotificationH\x00\x42\x05\n\x03msg*\x1b\n\x05I2cId\x12\x08\n\x04I2C0\x10\x00\x12\x08\n\x04I2C1\x10\x01*<\n\x0c\x41\x64\x64ressWidth\x12\t\n\x05\x42its7\x10\x00\x12\t\n\x05\x42its8\x10\x01\x12\n\n\x06\x42its10\x10\x02\x12\n\n\x06\x42its16\x10\x03*\xe0\x01\n\x13I2cConfigStatusCode\x12\x10\n\x0c\x43\x46G_NOT_INIT\x10\x00\x12\x0f\n\x0b\x43\x46G_SUCCESS\x10\x01\x12\x13\n\x0f\x43\x46G_BAD_REQUEST\x10\x02\x12\x1a\n\x16\x43\x46G_INVALID_CLOCK_FREQ\x10\x03\x12\x1a\n\x16\x43\x46G_INVALID_SLAVE_ADDR\x10\x04\x12 \n\x1c\x43\x46G_INVALID_SLAVE_ADDR_WIDTH\x10\x05\x12\x1e\n\x1a\x43\x46G_INVALID_MEM_ADDR_WIDTH\x10\x06\x12\x17\n\x13\x43\x46G_INTERFACE_ERROR\x10\x07*\x9a\x01\n\rI2cStatusCode\x12\x10\n\x0cSTS_NOT_INIT\x10\x00\x12\x0f\n\x0bSTS_SUCCESS\x10\x01\x12\x13\n\x0fSTS_BAD_REQUEST\x10\x02\x12\x10\n\x0cSTS_NO_SPACE\x10\x03\x12\x12\n\x0eSTS_SLAVE_BUSY\x10\x04\x12\x12\n\x0eSTS_SLAVE_NACK\x10\x05\x12\x17\n\x13STS_INTERFACE_ERROR\x10\x06\x42\x02H\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'i2c_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\003'
  _globals['_I2CID']._serialized_start=1509
  _globals['_I2CID']._serialized_end=1536
  _globals['_ADDRESSWIDTH']._serialized_start=1538
  _globals['_ADDRESSWIDTH']._serialized_end=1598
  _globals['_I2CCONFIGSTATUSCODE']._serialized_start=1601
  _globals['_I2CCONFIGSTATUSCODE']._serialized_end=1825
  _globals['_I2CSTATUSCODE']._serialized_start=1828
  _globals['_I2CSTATUSCODE']._serialized_end=1982
  _globals['_I2CCONFIGREQUEST']._serialized_start=25
  _globals['_I2CCONFIGREQUEST']._serialized_end=228
  _globals['_I2CCONFIGSTATUS']._serialized_start=230
  _globals['_I2CCONFIGSTATUS']._serialized_end=320
  _globals['_I2CMASTERREQUEST']._serialized_start=323
  _globals['_I2CMASTERREQUEST']._serialized_end=463
  _globals['_I2CMASTERSTATUS']._serialized_start=466
  _globals['_I2CMASTERSTATUS']._serialized_end=654
  _globals['_I2CSLAVEREQUEST']._serialized_start=656
  _globals['_I2CSLAVEREQUEST']._serialized_end=771
  _globals['_I2CSLAVESTATUS']._serialized_start=773
  _globals['_I2CSLAVESTATUS']._serialized_end=896
  _globals['_I2CSLAVENOTIFICATION']._serialized_start=899
  _globals['_I2CSLAVENOTIFICATION']._serialized_end=1047
  _globals['_I2CMSG']._serialized_start=1050
  _globals['_I2CMSG']._serialized_end=1507
# @@protoc_insertion_point(module_scope)
