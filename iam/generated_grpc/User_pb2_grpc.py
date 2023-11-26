# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import User_pb2 as User__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_stream(
                '/User/list',
                request_serializer=User__pb2.ListRequest.SerializeToString,
                response_deserializer=User__pb2.UserData.FromString,
                )
        self.retrieve = channel.unary_unary(
                '/User/retrieve',
                request_serializer=User__pb2.UserRetrieveRequest.SerializeToString,
                response_deserializer=User__pb2.UserData.FromString,
                )
        self.authenticate_token = channel.unary_unary(
                '/User/authenticate_token',
                request_serializer=User__pb2.TokenVerificationRequest.SerializeToString,
                response_deserializer=User__pb2.TokenVerificationResponse.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def authenticate_token(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_stream_rpc_method_handler(
                    servicer.list,
                    request_deserializer=User__pb2.ListRequest.FromString,
                    response_serializer=User__pb2.UserData.SerializeToString,
            ),
            'retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.retrieve,
                    request_deserializer=User__pb2.UserRetrieveRequest.FromString,
                    response_serializer=User__pb2.UserData.SerializeToString,
            ),
            'authenticate_token': grpc.unary_unary_rpc_method_handler(
                    servicer.authenticate_token,
                    request_deserializer=User__pb2.TokenVerificationRequest.FromString,
                    response_serializer=User__pb2.TokenVerificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/User/list',
            User__pb2.ListRequest.SerializeToString,
            User__pb2.UserData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/retrieve',
            User__pb2.UserRetrieveRequest.SerializeToString,
            User__pb2.UserData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def authenticate_token(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/authenticate_token',
            User__pb2.TokenVerificationRequest.SerializeToString,
            User__pb2.TokenVerificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
