import grpc
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import GetMessageClass
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from grpc_reflection.v1alpha.reflection import ReflectionServicer


def get_loaded_reflection_db(channel_address: str):
    channel = grpc.insecure_channel(channel_address)
    reflection_db = ProtoReflectionDescriptorDatabase(channel)
    # descriptor_pool = DescriptorPool(reflection_db)
    service_list = reflection_db.get_services()
    # descriptor_pool.FindServiceByName('User')
    for service in service_list:
        try:
            reflection_db.FindFileContainingSymbol(service)
        except Exception:
            continue
    return reflection_db
