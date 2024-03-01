"""
client = reflection.ReflectionServicer(['iam'], descriptor_pool)
client._list_services()


Goal : When we initialize client by  passing the addresses of services, we should get
client = GRPCClient(addresses)

the following should be the way to call a grpc server
client.<MICRO_SERVICE_NAME>.<RPC_SERVICE_NAME>.<METHOD_NAME>(REQUEST_CLASS(data))

the request class should be
"""

from google._upb._message import Descriptor
from google.protobuf.descriptor_pb2 import FileDescriptorProto
from google.protobuf.descriptor_pb2 import MethodDescriptorProto
from google.protobuf.descriptor_pb2 import ServiceDescriptorProto
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import GetMessageClass
from grpc._channel import Channel
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase

from core.messagbus.client.services import get_loaded_reflection_db


class Request:
    def __init__(self, message_type: Descriptor):
        self._message_type = message_type
        self._class = GetMessageClass(message_type)
        fields = message_type.fields_by_name
        self._fields = []
        for field in fields:
            setattr(self, field, fields[field])
            self._fields.append(field)

    @property
    def MessageClass(self):
        return self._class


class Response:
    def __init__(self, message_type: Descriptor):
        self._message_type = message_type
        self._class = GetMessageClass(message_type)
        fields = message_type.fields_by_name
        self._fields = []
        for field in fields:
            setattr(self, field, fields[field])
            self._fields.append(field)

    @property
    def MessageClass(self):
        return self._class


class Method:
    def __init__(
            self,
            service_name: str,
            method_descriptor_proto: MethodDescriptorProto,
            descriptor_pool: DescriptorPool,
            channel: Channel
    ):
        self.service_name = service_name
        self._method_descriptor_proto = method_descriptor_proto
        self._channel = channel
        self._add_request_class(method_descriptor_proto, descriptor_pool)
        self._add_response_class(method_descriptor_proto, descriptor_pool)
        self._contruct_caller(self._request_class.MessageClass, self._response_class.MessageClass)

    def __call__(self, **request_data):
        request_data = self._request_class.MessageClass(**request_data)
        print('request_data construction complete')
        print(request_data)
        print('request_data sening request')
        print(self.service_name, self._method_descriptor_proto.name, sep='/')
        return self._response_call(request_data)

    def _add_request_class(self, method_descriptor_proto: MethodDescriptorProto, descriptor_pool):
        request_str = method_descriptor_proto.input_type.split('.')[1]
        self._request_class = Request(descriptor_pool.FindMessageTypeByName(request_str))

    def _add_response_class(self, method_descriptor_proto: MethodDescriptorProto, descriptor_pool):
        response_str = method_descriptor_proto.output_type.split('.')[1]
        self._response_class = Response(descriptor_pool.FindMessageTypeByName(response_str))

    def _contruct_caller(
            self,
            request_class,
            response_class,
    ):
        """
        embeds self._response_call in the object which is a callable.
        """
        if (
                not self._method_descriptor_proto.client_streaming and
                not self._method_descriptor_proto.server_streaming
        ):
            self._response_call = self._channel.unary_unary(
                '/{}/{}'.format(self.service_name, self._method_descriptor_proto.name),
                request_serializer=request_class.SerializeToString,
                response_deserializer=response_class.FromString,
            )

        elif (
                not self._method_descriptor_proto.client_streaming and
                self._method_descriptor_proto.server_streaming
        ):
            self._response_call = self._channel.unary_stream(
                '/{}/{}'.format(self.service_name, self._method_descriptor_proto.name),
                request_serializer=request_class.SerializeToString,
                response_deserializer=response_class.FromString,
            )

        elif (
                self._method_descriptor_proto.client_streaming and
                not self._method_descriptor_proto.server_streaming
        ):
            self._response_call = self._channel.stream_unary(
                '/{}/{}'.format(self.service_name, self._method_descriptor_proto.name),
                request_serializer=request_class.SerializeToString,
                response_deserializer=response_class.FromString,
            )
        elif (
                self._method_descriptor_proto.client_streaming and
                self._method_descriptor_proto.server_streaming
        ):
            self._response_call = self._channel.stream_stream(
                '/{}/{}'.format(self.service_name, self._method_descriptor_proto.name),
                request_serializer=request_class.SerializeToString,
                response_deserializer=response_class.FromString,
            )


class RPCService:
    def __init__(
            self,
            service_descriptor_proto: ServiceDescriptorProto,
            descriptor_pool: DescriptorPool,
            channel,
    ):
        # self._service_proto = service_descriptor_proto
        i = 0
        while True:
            try:
                setattr(
                    self, service_descriptor_proto.method[i].name,
                    Method(
                        service_descriptor_proto.name,
                        service_descriptor_proto.method[i],
                        descriptor_pool,
                        channel
                    )
                )
                i += 1
            except IndexError:
                break


class Proto:
    def __init__(self, proto: FileDescriptorProto, descriptor_pool: DescriptorPool, channel: Channel):
        self._proto = proto
        i = 0
        while True:
            try:
                setattr(self, proto.service[i].name, RPCService(proto.service[i], descriptor_pool, channel))
                i += 1
            except IndexError:
                break


class Microservice:
    def __init__(
            self,
            reflection_descriptor_database: ProtoReflectionDescriptorDatabase,
            proto_service_names: [str],
            channel: Channel
    ):
        self._descriptor_pool = DescriptorPool(reflection_descriptor_database)
        for proto_name in proto_service_names:
            self._add_protos_to_this_class(reflection_descriptor_database, proto_name, channel)

    def _add_protos_to_this_class(
            self,
            reflection_descriptor_database: ProtoReflectionDescriptorDatabase,
            proto_name: str,
            channel) -> None:

        proto = reflection_descriptor_database._file_desc_protos_by_file.get(f'{proto_name.lower()}.proto')
        print('sdfsdfsdf', proto, proto_name)
        if proto:
            setattr(self, f'{proto_name}', Proto(proto, self._descriptor_pool, channel))


class GRPCClient:
    """

    """
    def __init__(self, microservices: dict):
        self._microservices = microservices
        for microservice_name in microservices.keys():
            # ipdb.set_trace()
            rdb, proto_service_names, channel = self._add_service(microservices[microservice_name])
            print(rdb, proto_service_names, channel, sep=' ** ')
            setattr(self, f'_{microservice_name}_rdb', rdb)
            setattr(self, f'{microservice_name}', Microservice(rdb, proto_service_names, channel))

    def _add_service(self, service_address: str) -> (ProtoReflectionDescriptorDatabase, list, Channel):
        return get_loaded_reflection_db(service_address)

