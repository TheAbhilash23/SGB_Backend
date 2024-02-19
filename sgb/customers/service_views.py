from google.protobuf.json_format import ParseDict

from core.messagbus.server import BaseAbstractService
from core.messagbus.generated_code.sgb.generated_grpc import customers_pb2
from core.messagbus.generated_code.sgb.generated_grpc import customers_pb2_grpc


class CustomerServiceView(BaseAbstractService):
    grpc_module = customers_pb2_grpc
    pb2_module = customers_pb2

    class Servicer(customers_pb2_grpc.CustomerServicer):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.model = None

        def get_model(self):
            if self.model is None:
                from customers.models import Customer
                self.model = Customer
            return self.model

        def get_queryset(self):
            return self.get_model().objects.all()

        def List(self, request, context):
            queryset = self.get_queryset()
            for obj in queryset:
                data = {
                    "user_id": obj.user_id,
                    "name": obj.name,
                    "id": obj.id,
                    "email": obj.email,
                }
                yield ParseDict(data or {}, customers_pb2.CustomerData())

        def Retrieve(self, request, context):
            """Missing associated documentation comment in .proto file."""
            obj = self.get_queryset().get(customer_id=request.id)
            data = {
                "user_id": obj.user_id,
                "name": obj.name,
                "id": obj.id,
                "email": obj.email,
            }
            response = ParseDict(data or {}, customers_pb2.CustomerData())
            return response

        def UserIdRetrieve(self, request, context):
            obj = self.get_queryset().get(id=request.user_id)
            data = {
                "user_id": obj.user_id,
                "name": obj.name,
                "id": obj.id,
                "email": obj.email,
            }
            return ParseDict(data or {}, customers_pb2.CustomerData())

        def Create(self, request, context):
            obj = self.get_model()()
            obj.name = request.name
            obj.user_id = request.user_id
            obj.email = request.email
            obj.save()
            data = {
                "user_id": obj.user_id,
                "name": obj.name,
                "id": obj.id,
                "email": obj.email,
            }
            return ParseDict(data or {}, customers_pb2.CustomerData())

    __servicer = Servicer()

    @classmethod
    def get_add_servicer_method(cls, server, servicer=None):
        return cls.grpc_module.add_CustomerServicer_to_server(cls.__servicer, server)

    def servicer(self) -> Servicer:
        return self.__servicer

    @property
    def label(self) -> str:
        return 'Customer'

