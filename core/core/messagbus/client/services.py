import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from grpc._channel import Channel


def get_loaded_reflection_db(channel_address: str) -> (ProtoReflectionDescriptorDatabase, list, Channel):
    print(channel_address)
    channel = grpc.insecure_channel(channel_address)
    reflection_db = ProtoReflectionDescriptorDatabase(channel)
    try:  # sometimes grpc call would fail first time hence we need to catch the exception twice
        service_list = reflection_db.get_services()
    except grpc._channel._MultiThreadedRendezvous:
        try:
            service_list = reflection_db.get_services()
        except grpc._channel._MultiThreadedRendezvous:
            service_list = []

    for service in service_list:
        try:
            reflection_db.FindFileContainingSymbol(service)
        except Exception:
            continue
    return reflection_db, service_list, channel


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
