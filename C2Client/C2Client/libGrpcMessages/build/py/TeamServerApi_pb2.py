# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TeamServerApi.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13TeamServerApi.proto\x12\rteamserverapi\"\x07\n\x05\x45mpty\"B\n\x08Response\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.teamserverapi.Status\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"\xa5\x01\n\x08Listener\x12\x14\n\x0clistenerHash\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\r\n\x05token\x18\x07 \x01(\t\x12\x0e\n\x06\x64omain\x18\x08 \x01(\t\x12\x17\n\x0fnumberOfSession\x18\x05 \x01(\x05\x12\x12\n\nbeaconHash\x18\t \x01(\t\"\xad\x01\n\x07Session\x12\x12\n\nbeaconHash\x18\x01 \x01(\t\x12\x14\n\x0clistenerHash\x18\x02 \x01(\t\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x0c\n\x04\x61rch\x18\x05 \x01(\t\x12\x11\n\tprivilege\x18\x06 \x01(\t\x12\n\n\x02os\x18\x07 \x01(\t\x12\x17\n\x0flastProofOfLife\x18\x08 \x01(\t\x12\x0e\n\x06killed\x18\t \x01(\x08\"@\n\x07\x43ommand\x12\x12\n\nbeaconHash\x18\x01 \x01(\t\x12\x14\n\x0clistenerHash\x18\x02 \x01(\t\x12\x0b\n\x03\x63md\x18\x03 \x01(\t\"Y\n\x0f\x43ommandResponse\x12\x12\n\nbeaconHash\x18\x01 \x01(\t\x12\x13\n\x0binstruction\x18\x02 \x01(\t\x12\x0b\n\x03\x63md\x18\x03 \x01(\t\x12\x10\n\x08response\x18\x04 \x01(\x0c\"8\n\x0bTermCommand\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c*\x18\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x06\n\x02KO\x10\x01\x32\x87\x05\n\rTeamServerApi\x12\x41\n\x0cGetListeners\x12\x14.teamserverapi.Empty\x1a\x17.teamserverapi.Listener\"\x00\x30\x01\x12\x41\n\x0b\x41\x64\x64Listener\x12\x17.teamserverapi.Listener\x1a\x17.teamserverapi.Response\"\x00\x12\x42\n\x0cStopListener\x12\x17.teamserverapi.Listener\x1a\x17.teamserverapi.Response\"\x00\x12?\n\x0bGetSessions\x12\x14.teamserverapi.Empty\x1a\x16.teamserverapi.Session\"\x00\x30\x01\x12@\n\x0bStopSession\x12\x16.teamserverapi.Session\x1a\x17.teamserverapi.Response\"\x00\x12\x43\n\x07GetHelp\x12\x16.teamserverapi.Command\x1a\x1e.teamserverapi.CommandResponse\"\x00\x12\x45\n\x10SendCmdToSession\x12\x16.teamserverapi.Command\x1a\x17.teamserverapi.Response\"\x00\x12T\n\x16GetResponseFromSession\x12\x16.teamserverapi.Session\x1a\x1e.teamserverapi.CommandResponse\"\x00\x30\x01\x12G\n\x0bSendTermCmd\x12\x1a.teamserverapi.TermCommand\x1a\x1a.teamserverapi.TermCommand\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TeamServerApi_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATUS._serialized_start=674
  _STATUS._serialized_end=698
  _EMPTY._serialized_start=38
  _EMPTY._serialized_end=45
  _RESPONSE._serialized_start=47
  _RESPONSE._serialized_end=113
  _LISTENER._serialized_start=116
  _LISTENER._serialized_end=281
  _SESSION._serialized_start=284
  _SESSION._serialized_end=457
  _COMMAND._serialized_start=459
  _COMMAND._serialized_end=523
  _COMMANDRESPONSE._serialized_start=525
  _COMMANDRESPONSE._serialized_end=614
  _TERMCOMMAND._serialized_start=616
  _TERMCOMMAND._serialized_end=672
  _TEAMSERVERAPI._serialized_start=701
  _TEAMSERVERAPI._serialized_end=1348
# @@protoc_insertion_point(module_scope)
