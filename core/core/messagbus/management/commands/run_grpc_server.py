# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.management.base import BaseCommand

from ...server import Server


class Command(BaseCommand):
    help = 'Starts a gRPC server. Requires complete address in the argument'

    # Validation is called explicitly each time the server is reloaded.
    # requires_system_checks = False

    def add_arguments(self, parser):
        parser.add_argument(
            'address', type=str,
        )
        parser.add_argument(
            '--max-workers', type=int, default=10, dest='max_workers',
            help='Number of maximum worker threads.'
        )

    def handle(self, *args, **options):
        print(f"Starting gRPC server at {options['address']}")
        handler = settings.HANDLER
        grpc_server_object = Server()
        handler.registry_collection(grpc_server_object._server())
        grpc_server_object.run(f"{options['address']}")

