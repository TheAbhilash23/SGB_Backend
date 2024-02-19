"""
client = reflection.ReflectionServicer(['iam'], descriptor_pool)
client._list_services()

"""


import grpc
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import GetMessageClass
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from grpc_reflection.v1alpha.reflection import ReflectionServicer


class GRPCClientFactory:

    pass
