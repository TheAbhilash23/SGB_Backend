from google.protobuf.json_format import ParseDict
from rest_framework_simplejwt.exceptions import TokenError

from core.messagbus.server import BaseAbstractService
from generated_grpc.user import user_pb2
from generated_grpc.user import user_pb2_grpc


class UserServiceView(BaseAbstractService):
    grpc_module = user_pb2_grpc
    pb2_module = user_pb2

    class Servicer(grpc_module.UserServicer):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.model = None

        def get_model(self):
            if self.model is None:
                from users.models import User
                self.model = User
            return self.model

        def get_queryset(self):
            return self.get_model().objects.all()

        def List(self, request, context):
            queryset = self.get_queryset()
            for user_data in queryset:
                data = {
                    "id": user_data.id,
                    "username": user_data.username,
                    "email": user_data.email,
                }
                yield ParseDict(data or {}, user_pb2.UserData())

        def Retrieve(self, request, context):
            print(f'Retrieve Context {context}\n\n')
            print(f'Retrieve request {request}')
            queryset = self.get_queryset().get(id=request.id)
            data = {
                "id": queryset.id,
                "username": queryset.username,
                "email": queryset.email,
            }
            response = ParseDict(data, user_pb2.UserData())
            print(f'response ::: \n {response}')
            return response

        def AuthenticateToken(self, request, context):
            from authentication import GRPCAuthentication
            try:
                is_valid = GRPCAuthentication(request.Token)
            except TokenError:
                is_valid = False
            response = ParseDict({'is_valid_token': is_valid}, user_pb2.TokenVerificationResponse())
            return response

    __servicer = Servicer()

    @classmethod
    def get_add_servicer_method(cls, server, servicer=None):
        return cls.grpc_module.add_UserServicer_to_server(cls.__servicer, server)

    def servicer(self) -> Servicer:
        return self.__servicer

    @property
    def label(self) -> str:
        return 'User'


# class GreetingService(BaseAbstractService):
#     grpc_module = HelloWorld_pb2_grpc
#     pb2_module = HelloWorld_pb2
#
#     class Servicer(grpc_module.GreeterServicer):
#
#         def personal(self, request, context):
#             reply = f'Your message was {request.message}, to that i would say Hello'
#             data = {
#                 "ReturnGreeting": reply,
#             }
#             response = ParseDict(data, HelloWorld_pb2.HelloReply())
#             return response
#
#         # def parrot(self, request, context):
#         #     """Missing associated documentation comment in .proto file."""
#         #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
#         #     context.set_details('Method not implemented!')
#         #     raise NotImplementedError('Method not implemented!')
#         #
#         # def chatty(self, request_iterator, context):
#         #     """Missing associated documentation comment in .proto file."""
#         #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
#         #     context.set_details('Method not implemented!')
#         #     raise NotImplementedError('Method not implemented!')
#         #
#         # def bidirectional(self, request_iterator, context):
#         #     """Missing associated documentation comment in .proto file."""
#         #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
#         #     context.set_details('Method not implemented!')
#         #     raise NotImplementedError('Method not implemented!')
#
#     __servicer = Servicer()
#
#     @classmethod
#     def get_add_servicer_method(cls, server, servicer=None):
#         return cls.grpc_module.add_GreeterServicer_to_server(cls.__servicer, server)
#
#     def servicer(self) -> Servicer:
#         return self.__servicer
#
#     @property
#     def label(self) -> str:
#         return 'Greeter'

