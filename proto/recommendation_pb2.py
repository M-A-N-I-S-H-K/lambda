# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/recommendation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/recommendation.proto',
  package='news_recommendation',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1aproto/recommendation.proto\x12\x13news_recommendation\"<\n\rUpdateRequest\x12\x14\n\x0cVariableName\x18\x01 \x01(\t\x12\x15\n\rVariableValue\x18\x02 \x01(\t\"+\n\x0bUpdateReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\"\x8f\x01\n\x15RecommendationRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12\x1a\n\x12preferred_keywords\x18\x03 \x01(\t\x12\x1c\n\x14preferred_categories\x18\x04 \x01(\t\x12\x18\n\x10max_items_in_row\x18\x05 \x01(\x05\"#\n\x13RecommendationReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x08\".\n\x0bStatusReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\"\x1e\n\rStatusRequest\x12\r\n\x05\x63heck\x18\x01 \x01(\t\"E\n\x0eSimilarRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\"R\n\x0cSimilarReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\ntime_taken\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t2\xee\x02\n\x0eRecommendation\x12\x63\n\tRecommend\x12*.news_recommendation.RecommendationRequest\x1a(.news_recommendation.RecommendationReply\"\x00\x12P\n\x06Update\x12\".news_recommendation.UpdateRequest\x1a .news_recommendation.UpdateReply\"\x00\x12S\n\x07Similar\x12#.news_recommendation.SimilarRequest\x1a!.news_recommendation.SimilarReply\"\x00\x12P\n\x06Status\x12\".news_recommendation.StatusRequest\x1a .news_recommendation.StatusReply\"\x00\x62\x06proto3'
)




_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='news_recommendation.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='VariableName', full_name='news_recommendation.UpdateRequest.VariableName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VariableValue', full_name='news_recommendation.UpdateRequest.VariableValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=111,
)


_UPDATEREPLY = _descriptor.Descriptor(
  name='UpdateReply',
  full_name='news_recommendation.UpdateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='news_recommendation.UpdateReply.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='news_recommendation.UpdateReply.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=156,
)


_RECOMMENDATIONREQUEST = _descriptor.Descriptor(
  name='RecommendationRequest',
  full_name='news_recommendation.RecommendationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='news_recommendation.RecommendationRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='news_recommendation.RecommendationRequest.country_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preferred_keywords', full_name='news_recommendation.RecommendationRequest.preferred_keywords', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preferred_categories', full_name='news_recommendation.RecommendationRequest.preferred_categories', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_items_in_row', full_name='news_recommendation.RecommendationRequest.max_items_in_row', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=302,
)


_RECOMMENDATIONREPLY = _descriptor.Descriptor(
  name='RecommendationReply',
  full_name='news_recommendation.RecommendationReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='news_recommendation.RecommendationReply.data', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=339,
)


_STATUSREPLY = _descriptor.Descriptor(
  name='StatusReply',
  full_name='news_recommendation.StatusReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='news_recommendation.StatusReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='news_recommendation.StatusReply.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=387,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='news_recommendation.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='check', full_name='news_recommendation.StatusRequest.check', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=419,
)


_SIMILARREQUEST = _descriptor.Descriptor(
  name='SimilarRequest',
  full_name='news_recommendation.SimilarRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='news_recommendation.SimilarRequest.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='news_recommendation.SimilarRequest.size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='news_recommendation.SimilarRequest.country_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=490,
)


_SIMILARREPLY = _descriptor.Descriptor(
  name='SimilarReply',
  full_name='news_recommendation.SimilarReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='news_recommendation.SimilarReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='news_recommendation.SimilarReply.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_taken', full_name='news_recommendation.SimilarReply.time_taken', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='news_recommendation.SimilarReply.data', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=574,
)

DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateReply'] = _UPDATEREPLY
DESCRIPTOR.message_types_by_name['RecommendationRequest'] = _RECOMMENDATIONREQUEST
DESCRIPTOR.message_types_by_name['RecommendationReply'] = _RECOMMENDATIONREPLY
DESCRIPTOR.message_types_by_name['StatusReply'] = _STATUSREPLY
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['SimilarRequest'] = _SIMILARREQUEST
DESCRIPTOR.message_types_by_name['SimilarReply'] = _SIMILARREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateReply = _reflection.GeneratedProtocolMessageType('UpdateReply', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREPLY,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.UpdateReply)
  })
_sym_db.RegisterMessage(UpdateReply)

RecommendationRequest = _reflection.GeneratedProtocolMessageType('RecommendationRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONREQUEST,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.RecommendationRequest)
  })
_sym_db.RegisterMessage(RecommendationRequest)

RecommendationReply = _reflection.GeneratedProtocolMessageType('RecommendationReply', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONREPLY,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.RecommendationReply)
  })
_sym_db.RegisterMessage(RecommendationReply)

StatusReply = _reflection.GeneratedProtocolMessageType('StatusReply', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREPLY,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.StatusReply)
  })
_sym_db.RegisterMessage(StatusReply)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

SimilarRequest = _reflection.GeneratedProtocolMessageType('SimilarRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIMILARREQUEST,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.SimilarRequest)
  })
_sym_db.RegisterMessage(SimilarRequest)

SimilarReply = _reflection.GeneratedProtocolMessageType('SimilarReply', (_message.Message,), {
  'DESCRIPTOR' : _SIMILARREPLY,
  '__module__' : 'proto.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:news_recommendation.SimilarReply)
  })
_sym_db.RegisterMessage(SimilarReply)



_RECOMMENDATION = _descriptor.ServiceDescriptor(
  name='Recommendation',
  full_name='news_recommendation.Recommendation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=577,
  serialized_end=943,
  methods=[
  _descriptor.MethodDescriptor(
    name='Recommend',
    full_name='news_recommendation.Recommendation.Recommend',
    index=0,
    containing_service=None,
    input_type=_RECOMMENDATIONREQUEST,
    output_type=_RECOMMENDATIONREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='news_recommendation.Recommendation.Update',
    index=1,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Similar',
    full_name='news_recommendation.Recommendation.Similar',
    index=2,
    containing_service=None,
    input_type=_SIMILARREQUEST,
    output_type=_SIMILARREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='news_recommendation.Recommendation.Status',
    index=3,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDATION)

DESCRIPTOR.services_by_name['Recommendation'] = _RECOMMENDATION

# @@protoc_insertion_point(module_scope)
