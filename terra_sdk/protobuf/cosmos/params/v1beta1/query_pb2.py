# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/params/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.params.v1beta1 import (
    params_pb2 as cosmos_dot_params_dot_v1beta1_dot_params__pb2,
)
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/params/v1beta1/query.proto",
    package="cosmos.params.v1beta1",
    syntax="proto3",
    serialized_options=b"Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n!cosmos/params/v1beta1/query.proto\x12\x15\x63osmos.params.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a"cosmos/params/v1beta1/params.proto"3\n\x12QueryParamsRequest\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t"N\n\x13QueryParamsResponse\x12\x37\n\x05param\x18\x01 \x01(\x0b\x32".cosmos.params.v1beta1.ParamChangeB\x04\xc8\xde\x1f\x00\x32\x90\x01\n\x05Query\x12\x86\x01\n\x06Params\x12).cosmos.params.v1beta1.QueryParamsRequest\x1a*.cosmos.params.v1beta1.QueryParamsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/params/v1beta1/paramsB6Z4github.com/cosmos/cosmos-sdk/x/params/types/proposalb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        cosmos_dot_params_dot_v1beta1_dot_params__pb2.DESCRIPTOR,
    ],
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
    name="QueryParamsRequest",
    full_name="cosmos.params.v1beta1.QueryParamsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="subspace",
            full_name="cosmos.params.v1beta1.QueryParamsRequest.subspace",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="key",
            full_name="cosmos.params.v1beta1.QueryParamsRequest.key",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=148,
    serialized_end=199,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
    name="QueryParamsResponse",
    full_name="cosmos.params.v1beta1.QueryParamsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="param",
            full_name="cosmos.params.v1beta1.QueryParamsResponse.param",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=201,
    serialized_end=279,
)

_QUERYPARAMSRESPONSE.fields_by_name[
    "param"
].message_type = cosmos_dot_params_dot_v1beta1_dot_params__pb2._PARAMCHANGE
DESCRIPTOR.message_types_by_name["QueryParamsRequest"] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name["QueryParamsResponse"] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType(
    "QueryParamsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPARAMSREQUEST,
        "__module__": "cosmos.params.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.params.v1beta1.QueryParamsRequest)
    },
)
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType(
    "QueryParamsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPARAMSRESPONSE,
        "__module__": "cosmos.params.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.params.v1beta1.QueryParamsResponse)
    },
)
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR._options = None
_QUERYPARAMSRESPONSE.fields_by_name["param"]._options = None

_QUERY = _descriptor.ServiceDescriptor(
    name="Query",
    full_name="cosmos.params.v1beta1.Query",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=282,
    serialized_end=426,
    methods=[
        _descriptor.MethodDescriptor(
            name="Params",
            full_name="cosmos.params.v1beta1.Query.Params",
            index=0,
            containing_service=None,
            input_type=_QUERYPARAMSREQUEST,
            output_type=_QUERYPARAMSRESPONSE,
            serialized_options=b"\202\323\344\223\002\037\022\035/cosmos/params/v1beta1/params",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name["Query"] = _QUERY

# @@protoc_insertion_point(module_scope)
