"""
Module to create a class that uses the project's settings to create handlers for the project.

This class for registering the handlers for the project should be a runtime object so that it can be available for
use by the project.

The Server will be the Server object, serving handler (the routes).



Client side will be the instance of the registry that holds all the handlers registered.
The servre will be running on separate process, but will be installed on the project.
The server instance will be unique for each project hence making it a microservice reflection object.


To interact with the project and its componenets, the server will use the 'BaseCommand' handle to process requests
such as interacting with the database.
"""
from django.utils.module_loading import import_string
from grpc_health.v1 import health_pb2_grpc, health
from grpc_health.v1.health_pb2 import HealthCheckResponse
from grpc_reflection.v1alpha import reflection


# Write a mechanism such that when we install the app it should read the handlers registered,
# and then those handlers should be collected and served


class RuntimeGRPCRegistry:
    """
    The service class must be of Service class instance inherited from BaseAbstractService.
    used to register all rpc methods of a registry
    """

    def __init__(self, service):
        self._service_class = import_string(service)()
        setattr(self, f'{self._service_class.label}', None)

    @property
    def service_class(self):
        return self._service_class

    def register_to_server(self, server):
        return self._service_class.get_add_servicer_method(server)


class RegistryCollection:
    """
    Name of the microservice of a project.
    goal is to use the dot operator to generate at initialization and call rpc methods.
    """

    def __init__(self, micro_service_name):
        self._micro_service_name = micro_service_name
        setattr(self, f'{micro_service_name}', set())  # all registered service views
        # will be added here for the microservice

    @property
    def micro_service_name(self):
        return self._micro_service_name

    def register(self, service: str):
        runtime_registry = RuntimeGRPCRegistry(service)
        return getattr(self, f'{self.micro_service_name}').add(runtime_registry)

    def registry_collection(self, server) -> None:
        service_names = [
            reflection.SERVICE_NAME,
            health.SERVICE_NAME,
        ]
        health_servicer = health.HealthServicer(experimental_non_blocking=True)
        health_servicer.set('', HealthCheckResponse.SERVING)

        for service in getattr(self, f'{self.micro_service_name}'):
            service.register_to_server(server)
            service_name = service.service_class.label
            print(service_name)
            service_names.append(
                service.service_class.pb2_module.DESCRIPTOR.services_by_name[service_name].full_name
            )
            status = HealthCheckResponse.SERVING
            health_servicer.set(service_name, status)
        health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
        reflection.enable_server_reflection(service_names, server)
