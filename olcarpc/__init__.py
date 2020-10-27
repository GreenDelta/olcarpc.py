import grpc

from .olca_pb2 import *
from .services_pb2 import *
import olcarpc.services_pb2_grpc as services

from typing import Iterable


class Client:

    def __init__(self, port=8080):
        self.chan = grpc.insecure_channel('localhost:%i' % port)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.chan.close()

    @property
    def data(self) -> services.DataServiceStub:
        return services.DataServiceStub(self.chan)

    @property
    def actors(self) -> Iterable[Actor]:
        for a in self.data.actors(Empty()):
            yield a
