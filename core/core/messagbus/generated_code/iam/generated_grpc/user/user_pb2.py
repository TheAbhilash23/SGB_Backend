# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"\r\n\x0bListRequest\"!\n\x13UserRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\")\n\x18TokenVerificationRequest\x12\r\n\x05token\x18\x01 \x01(\t\"3\n\x19TokenVerificationResponse\x12\x16\n\x0eis_valid_token\x18\x01 \x01(\x08\"7\n\x08UserData\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t2\xa8\x01\n\x04User\x12#\n\x04List\x12\x0c.ListRequest\x1a\t.UserData\"\x00\x30\x01\x12-\n\x08Retrieve\x12\x14.UserRetrieveRequest\x1a\t.UserData\"\x00\x12L\n\x11\x41uthenticateToken\x12\x19.TokenVerificationRequest\x1a\x1a.TokenVerificationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LISTREQUEST']._serialized_start=14
  _globals['_LISTREQUEST']._serialized_end=27
  _globals['_USERRETRIEVEREQUEST']._serialized_start=29
  _globals['_USERRETRIEVEREQUEST']._serialized_end=62
  _globals['_TOKENVERIFICATIONREQUEST']._serialized_start=64
  _globals['_TOKENVERIFICATIONREQUEST']._serialized_end=105
  _globals['_TOKENVERIFICATIONRESPONSE']._serialized_start=107
  _globals['_TOKENVERIFICATIONRESPONSE']._serialized_end=158
  _globals['_USERDATA']._serialized_start=160
  _globals['_USERDATA']._serialized_end=215
  _globals['_USER']._serialized_start=218
  _globals['_USER']._serialized_end=386
# @@protoc_insertion_point(module_scope)
