# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chariott/common/v1/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63hariott/common/v1/common.proto\x12\x12\x63hariott.common.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\"\xd0\x02\n\x06Intent\x12\x36\n\x08\x64iscover\x18\x01 \x01(\x0b\x32\".chariott.common.v1.DiscoverIntentH\x00\x12\x32\n\x06invoke\x18\x02 \x01(\x0b\x32 .chariott.common.v1.InvokeIntentH\x00\x12.\n\x04read\x18\x03 \x01(\x0b\x32\x1e.chariott.common.v1.ReadIntentH\x00\x12\x30\n\x05write\x18\x04 \x01(\x0b\x32\x1f.chariott.common.v1.WriteIntentH\x00\x12\x34\n\x07inspect\x18\x05 \x01(\x0b\x32!.chariott.common.v1.InspectIntentH\x00\x12\x38\n\tsubscribe\x18\x06 \x01(\x0b\x32#.chariott.common.v1.SubscribeIntentH\x00\x42\x08\n\x06intent\"\x19\n\nReadIntent\x12\x0b\n\x03key\x18\x01 \x01(\t\";\n\x0fReadFulfillment\x12(\n\x05value\x18\x01 \x01(\x0b\x32\x19.chariott.common.v1.Value\"D\n\x0bWriteIntent\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.chariott.common.v1.Value\"\x12\n\x10WriteFulfillment\"6\n\x0fSubscribeIntent\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x0f\n\x07sources\x18\x02 \x03(\t\"\x16\n\x14SubscribeFulfillment\"\xf8\x02\n\x0b\x46ulfillment\x12;\n\x08\x64iscover\x18\x01 \x01(\x0b\x32\'.chariott.common.v1.DiscoverFulfillmentH\x00\x12\x39\n\x07inspect\x18\x02 \x01(\x0b\x32&.chariott.common.v1.InspectFulfillmentH\x00\x12\x33\n\x04read\x18\x03 \x01(\x0b\x32#.chariott.common.v1.ReadFulfillmentH\x00\x12\x35\n\x05write\x18\x04 \x01(\x0b\x32$.chariott.common.v1.WriteFulfillmentH\x00\x12\x37\n\x06invoke\x18\x05 \x01(\x0b\x32%.chariott.common.v1.InvokeFulfillmentH\x00\x12=\n\tsubscribe\x18\x06 \x01(\x0b\x32(.chariott.common.v1.SubscribeFulfillmentH\x00\x42\r\n\x0b\x66ulfillment\"\x10\n\x0e\x44iscoverIntent\"\xbd\x02\n\x13\x44iscoverFulfillment\x12\x41\n\x08services\x18\x01 \x03(\x0b\x32/.chariott.common.v1.DiscoverFulfillment.Service\x1a\xe2\x01\n\x07Service\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0bschema_kind\x18\x02 \x01(\t\x12\x18\n\x10schema_reference\x18\x03 \x01(\t\x12O\n\x08metadata\x18\x04 \x03(\x0b\x32=.chariott.common.v1.DiscoverFulfillment.Service.MetadataEntry\x1aJ\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.chariott.common.v1.Value:\x02\x38\x01\"\x1e\n\rInspectIntent\x12\r\n\x05query\x18\x01 \x01(\t\"\xfc\x01\n\x12InspectFulfillment\x12=\n\x07\x65ntries\x18\x01 \x03(\x0b\x32,.chariott.common.v1.InspectFulfillment.Entry\x1a\xa6\x01\n\x05\x45ntry\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x46\n\x05items\x18\x02 \x03(\x0b\x32\x37.chariott.common.v1.InspectFulfillment.Entry.ItemsEntry\x1aG\n\nItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.chariott.common.v1.Value:\x02\x38\x01\"H\n\x0cInvokeIntent\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\'\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x19.chariott.common.v1.Value\">\n\x11InvokeFulfillment\x12)\n\x06return\x18\x01 \x01(\x0b\x32\x19.chariott.common.v1.Value\"\xfb\x02\n\x05Value\x12-\n\x04null\x18\x01 \x01(\x0e\x32\x1d.chariott.common.v1.NullValueH\x00\x12#\n\x03\x61ny\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x0e\n\x04\x62ool\x18\x03 \x01(\x08H\x00\x12\x0f\n\x05int32\x18\x04 \x01(\x11H\x00\x12\x0f\n\x05int64\x18\x05 \x01(\x12H\x00\x12\x11\n\x07\x66loat32\x18\x06 \x01(\x02H\x00\x12\x11\n\x07\x66loat64\x18\x07 \x01(\x01H\x00\x12\x10\n\x06string\x18\x08 \x01(\tH\x00\x12/\n\ttimestamp\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12(\n\x04list\x18\n \x01(\x0b\x32\x18.chariott.common.v1.ListH\x00\x12&\n\x03map\x18\x0b \x01(\x0b\x32\x17.chariott.common.v1.MapH\x00\x12(\n\x04\x62lob\x18\x0c \x01(\x0b\x32\x18.chariott.common.v1.BlobH\x00\x42\x07\n\x05value\")\n\x04\x42lob\x12\x12\n\nmedia_type\x18\x01 \x01(\t\x12\r\n\x05\x62ytes\x18\x02 \x01(\x0c\"0\n\x04List\x12(\n\x05value\x18\x01 \x03(\x0b\x32\x19.chariott.common.v1.Value\"{\n\x03Map\x12-\n\x03map\x18\x01 \x03(\x0b\x32 .chariott.common.v1.Map.MapEntry\x1a\x45\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.chariott.common.v1.Value:\x02\x38\x01*\'\n\tNullValue\x12\x1a\n\x16NULL_VALUE_UNSPECIFIED\x10\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chariott.common.v1.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DISCOVERFULFILLMENT_SERVICE_METADATAENTRY._options = None
  _DISCOVERFULFILLMENT_SERVICE_METADATAENTRY._serialized_options = b'8\001'
  _INSPECTFULFILLMENT_ENTRY_ITEMSENTRY._options = None
  _INSPECTFULFILLMENT_ENTRY_ITEMSENTRY._serialized_options = b'8\001'
  _MAP_MAPENTRY._options = None
  _MAP_MAPENTRY._serialized_options = b'8\001'
  _NULLVALUE._serialized_start=2454
  _NULLVALUE._serialized_end=2493
  _INTENT._serialized_start=116
  _INTENT._serialized_end=452
  _READINTENT._serialized_start=454
  _READINTENT._serialized_end=479
  _READFULFILLMENT._serialized_start=481
  _READFULFILLMENT._serialized_end=540
  _WRITEINTENT._serialized_start=542
  _WRITEINTENT._serialized_end=610
  _WRITEFULFILLMENT._serialized_start=612
  _WRITEFULFILLMENT._serialized_end=630
  _SUBSCRIBEINTENT._serialized_start=632
  _SUBSCRIBEINTENT._serialized_end=686
  _SUBSCRIBEFULFILLMENT._serialized_start=688
  _SUBSCRIBEFULFILLMENT._serialized_end=710
  _FULFILLMENT._serialized_start=713
  _FULFILLMENT._serialized_end=1089
  _DISCOVERINTENT._serialized_start=1091
  _DISCOVERINTENT._serialized_end=1107
  _DISCOVERFULFILLMENT._serialized_start=1110
  _DISCOVERFULFILLMENT._serialized_end=1427
  _DISCOVERFULFILLMENT_SERVICE._serialized_start=1201
  _DISCOVERFULFILLMENT_SERVICE._serialized_end=1427
  _DISCOVERFULFILLMENT_SERVICE_METADATAENTRY._serialized_start=1353
  _DISCOVERFULFILLMENT_SERVICE_METADATAENTRY._serialized_end=1427
  _INSPECTINTENT._serialized_start=1429
  _INSPECTINTENT._serialized_end=1459
  _INSPECTFULFILLMENT._serialized_start=1462
  _INSPECTFULFILLMENT._serialized_end=1714
  _INSPECTFULFILLMENT_ENTRY._serialized_start=1548
  _INSPECTFULFILLMENT_ENTRY._serialized_end=1714
  _INSPECTFULFILLMENT_ENTRY_ITEMSENTRY._serialized_start=1643
  _INSPECTFULFILLMENT_ENTRY_ITEMSENTRY._serialized_end=1714
  _INVOKEINTENT._serialized_start=1716
  _INVOKEINTENT._serialized_end=1788
  _INVOKEFULFILLMENT._serialized_start=1790
  _INVOKEFULFILLMENT._serialized_end=1852
  _VALUE._serialized_start=1855
  _VALUE._serialized_end=2234
  _BLOB._serialized_start=2236
  _BLOB._serialized_end=2277
  _LIST._serialized_start=2279
  _LIST._serialized_end=2327
  _MAP._serialized_start=2329
  _MAP._serialized_end=2452
  _MAP_MAPENTRY._serialized_start=2383
  _MAP_MAPENTRY._serialized_end=2452
# @@protoc_insertion_point(module_scope)