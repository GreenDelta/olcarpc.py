import grpc
import google.protobuf.json_format as jf

from .olca_pb2 import *
from .services_pb2 import *
import olcarpc.services_pb2_grpc as services

import inspect
from typing import Any, Iterable, Union


__pdoc__ = {
    'olca_pb2': False,
    'services_pb2': False,
    'services_pb2_grpc': False,
}

def to_json(entity, indent: int = 2) -> str:
    return jf.MessageToJson(entity, indent=indent)


def ref(ref_type, ref_id: str, name='') -> Ref:
    r = Ref()
    if inspect.isclass(ref_type):
        r.type = ref_type.__name__
    else:
        r.type = ref_type
    r.id = ref_id
    r.name = name
    return r


class Client:

    def __init__(self, port=8080):
        self.port = port
        self.chan = grpc.insecure_channel('localhost:%i' % port)

    def __enter__(self):
        if self.chan is None:
            self.chan = grpc.insecure_channel('localhost:%i' % self.port)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.chan.close()
        self.chan = None

    def close(self):
        if self.chan is not None:
            self.chan.close()
            self.chan = None

    @property
    def data(self) -> services.DataServiceStub:
        return services.DataServiceStub(self.chan)

    def delete(self, ref: Union[Any, Ref]) -> Status:
        """
        Deletes the given object from the database.

        Parameters
        ----------
        ref: Union[Any, Ref]
            The (descriptor of) the object that should be deleted from the
            database. The given object needs to be a descriptor where at least
            the `id` and `type` fields are set (this is typically the case for
            the objects that are returned by the openLCA gRPC service).

        Example
        -------
        ```python
        import olcarpc as rpc

        client = rpc.Client()
        flow_status = client.flow(name='Test flow')
        if flow_status.ok:
            del_status = client.delete(flow_status.flow)
            print(del_status)
        ```
        """

        r = ref
        if not isinstance(ref, Ref):
            r = Ref()
            r.id = ref.id
            if ref.type is None or ref.type == '':
                r.type = ref.__class__.__name__
            else:
                r.type = ref.type
        return self.data.delete(r)

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

    def flow(self, id='', name='') -> FlowStatus:
        return self.data.flow(Ref(id=id, name=name))

    def put_flow(self, flow: Flow) -> RefStatus:
        return self.data.put_flow(flow)

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
