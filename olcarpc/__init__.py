import grpc
import google.protobuf.json_format as jf

from .olca_pb2 import *
from .services_pb2 import *
import olcarpc.services_pb2_grpc as services

from typing import Iterable


def to_json(entity, indent: int = 2) -> str:
    return jf.MessageToJson(entity, indent=indent)


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
        for actor in self.data.actors(Empty()):
            yield actor

    @property
    def categories(self) -> Iterable[Category]:
        for category in self.data.categories(Empty()):
            yield category

    @property
    def currencies(self) -> Iterable[Currency]:
        for currency in self.data.currencies(Empty()):
            yield currency

    @property
    def dq_systems(self) -> Iterable[DqSystem]:
        for dqSystem in self.data.dq_systems(Empty()):
            yield dqSystem

    @property
    def flows(self) -> Iterable[Flow]:
        for flow in self.data.flows(Empty()):
            yield flow

    @property
    def flow_properties(self) -> Iterable[FlowProperty]:
        for p in self.data.flow_properties(Empty()):
            yield p

    @property
    def impact_categories(self) -> Iterable[ImpactCategory]:
        for impact in self.data.impact_categories(Empty()):
            yield impact

    @property
    def impact_methods(self) -> Iterable[ImpactMethod]:
        for method in self.data.impact_methods(Empty()):
            yield method

    @property
    def locations(self) -> Iterable[Location]:
        for location in self.data.locations(Empty()):
            yield location

    @property
    def parameters(self) -> Iterable[Parameter]:
        for parameter in self.data.parameters(Empty()):
            yield parameter

    @property
    def processes(self) -> Iterable[Process]:
        for process in self.data.processes(Empty()):
            yield process

    @property
    def product_systems(self) -> Iterable[ProductSystem]:
        for system in self.data.product_systems(Empty()):
            yield system

    @property
    def projects(self) -> Iterable[Project]:
        for project in self.data.projects(Empty()):
            yield project

    @property
    def social_indicators(self) -> Iterable[SocialIndicator]:
        for indicator in self.data.social_indicators(Empty()):
            yield indicator

    @property
    def sources(self) -> Iterable[Source]:
        for source in self.data.sources(Empty()):
            yield source

    @property
    def unit_groups(self) -> Iterable[UnitGroup]:
        for group in self.data.unit_groups(Empty()):
            yield group
