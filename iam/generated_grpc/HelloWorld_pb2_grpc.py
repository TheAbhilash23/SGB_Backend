# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import HelloWorld_pb2 as HelloWorld__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.personal = channel.unary_unary(
                '/Greeter/personal',
                request_serializer=HelloWorld__pb2.HelloRequest.SerializeToString,
                response_deserializer=HelloWorld__pb2.HelloReply.FromString,
                )
        self.parrot = channel.unary_stream(
                '/Greeter/parrot',
                request_serializer=HelloWorld__pb2.HelloRequest.SerializeToString,
                response_deserializer=HelloWorld__pb2.HelloReply.FromString,
                )
        self.chatty = channel.stream_unary(
                '/Greeter/chatty',
                request_serializer=HelloWorld__pb2.HelloRequest.SerializeToString,
                response_deserializer=HelloWorld__pb2.HelloReply.FromString,
                )
        self.bidirectional = channel.stream_stream(
                '/Greeter/bidirectional',
                request_serializer=HelloWorld__pb2.HelloRequest.SerializeToString,
                response_deserializer=HelloWorld__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def personal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def parrot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def chatty(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def bidirectional(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'personal': grpc.unary_unary_rpc_method_handler(
                    servicer.personal,
                    request_deserializer=HelloWorld__pb2.HelloRequest.FromString,
                    response_serializer=HelloWorld__pb2.HelloReply.SerializeToString,
            ),
            'parrot': grpc.unary_stream_rpc_method_handler(
                    servicer.parrot,
                    request_deserializer=HelloWorld__pb2.HelloRequest.FromString,
                    response_serializer=HelloWorld__pb2.HelloReply.SerializeToString,
            ),
            'chatty': grpc.stream_unary_rpc_method_handler(
                    servicer.chatty,
                    request_deserializer=HelloWorld__pb2.HelloRequest.FromString,
                    response_serializer=HelloWorld__pb2.HelloReply.SerializeToString,
            ),
            'bidirectional': grpc.stream_stream_rpc_method_handler(
                    servicer.bidirectional,
                    request_deserializer=HelloWorld__pb2.HelloRequest.FromString,
                    response_serializer=HelloWorld__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def personal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/personal',
            HelloWorld__pb2.HelloRequest.SerializeToString,
            HelloWorld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def parrot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Greeter/parrot',
            HelloWorld__pb2.HelloRequest.SerializeToString,
            HelloWorld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def chatty(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Greeter/chatty',
            HelloWorld__pb2.HelloRequest.SerializeToString,
            HelloWorld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def bidirectional(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Greeter/bidirectional',
            HelloWorld__pb2.HelloRequest.SerializeToString,
            HelloWorld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
