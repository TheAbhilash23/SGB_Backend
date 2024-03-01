# from django.middleware
import grpc
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import GetMessageClass
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase


channel = grpc.insecure_channel("iam-service:50051")
GRPC_REFLECTION_INVOCATION_STRING = 'TokenVerificationRequest'
reflection_db = ProtoReflectionDescriptorDatabase(channel)

descriptor_pool = DescriptorPool(reflection_db)
request_desc = descriptor_pool.FindMessageTypeByName(GRPC_REFLECTION_INVOCATION_STRING)
service_descriptor = descriptor_pool.FindServiceByName('User')
method_descriptor = descriptor_pool.FindMethodByName('User.AuthenticateToken')

# request_class = MessageFactory(descriptor_pool).GetPrototype(request_desc)
request_class = GetMessageClass(request_desc)
response_desc = descriptor_pool.FindMessageTypeByName('TokenVerificationResponse')
# response_class = MessageFactory(descriptor_pool).GetPrototype(response_desc)
response_class = GetMessageClass(response_desc)

token_validation_response = channel.unary_unary(
    '/{}/{}'.format(service_descriptor.full_name, method_descriptor.name),
    request_serializer=request_class.SerializeToString,
    response_deserializer=response_class.FromString,
)


class IAMTokenAuthenticate(MiddlewareMixin):

    def process_request(self, request):
        if not request.path.startswith('/admin/'):
            print('Processing request for token authentication')
            is_valid_token = self.validate_token(request)
            print('Token is valid : {}'.format(is_valid_token))
            if is_valid_token is True:
                print('Token authentication successful')
                pass
            else:
                print('Token authentication failed')
                raise PermissionDenied('Token authentication failure')

    def validate_token(self, request):
        raw_token = request.headers.get('Authorization')
        grpc_response = token_validation_response(request_class(token=raw_token))
        if grpc_response.is_valid_token:
            return True
        else:
            return False
