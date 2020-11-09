import grpc
import google.protobuf.json_format as jf

from .olca_pb2 import *
from .services_pb2 import *
from .factory import *

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


def ref_of(entity) -> Ref:
    return ref(entity.__class__, entity.id, entity.name)


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

    def actors(self) -> Iterable[Actor]:
        for actor in self.data.actors(Empty()):
            yield actor

    def actor(self, id='', name='') -> ActorStatus:
        return self.data.actor(Ref(id=id, name=name))

    def put_actor(self, actor: Actor) -> RefStatus:
        return self.data.put_actor(actor)

    def categories(self) -> Iterable[Category]:
        for category in self.data.categories(Empty()):
            yield category

    def category(self, id='', name='') -> CategoryStatus:
        return self.data.category(Ref(id=id, name=name))

    def put_category(self, category: Category) -> RefStatus:
        return self.data.put_category(category)

    def currencies(self) -> Iterable[Currency]:
        for currency in self.data.currencies(Empty()):
            yield currency

    def currency(self, id='', name='') -> CurrencyStatus:
        return self.data.currency(Ref(id=id, name=name))

    def put_currency(self, currency: Currency) -> RefStatus:
        return self.data.put_currency(currency)

    def dq_systems(self) -> Iterable[DQSystem]:
        for dqSystem in self.data.dq_systems(Empty()):
            yield dqSystem

    def dq_system(self, id='', name='') -> DQSystemStatus:
        return self.data.dq_system(Ref(id=id, name=name))

    def put_dq_system(self, dq_system: DQSystem) -> RefStatus:
        return self.data.put_dq_system(dq_system)

    def flows(self) -> Iterable[Flow]:
        for flow in self.data.flows(Empty()):
            yield flow

    def flow(self, id='', name='') -> FlowStatus:
        return self.data.flow(Ref(id=id, name=name))

    def put_flow(self, flow: Flow) -> RefStatus:
        return self.data.put_flow(flow)

    def flow_properties(self) -> Iterable[FlowProperty]:
        for p in self.data.flow_properties(Empty()):
            yield p

    def flow_property(self, id='', name='') -> FlowPropertyStatus:
        return self.data.flow_property(Ref(id=id, name=name))

    def put_flow_property(self, flow_property: FlowProperty) -> RefStatus:
        return self.data.put_flow_property(flow_property)

    def impact_categories(self) -> Iterable[ImpactCategory]:
        for impact in self.data.impact_categories(Empty()):
            yield impact

    def impact_category(self, id='', name='') -> ImpactCategoryStatus:
        return self.data.impact_category(Ref(id=id, name=name))

    def put_impact_category(self, impact_category: ImpactCategory) -> RefStatus:
        return self.data.put_impact_category(impact_category)

    def impact_methods(self) -> Iterable[ImpactMethod]:
        for method in self.data.impact_methods(Empty()):
            yield method

    def impact_method(self, id='', name='') -> ImpactMethodStatus:
        return self.data.impact_method(Ref(id=id, name=name))

    def put_impact_method(self, impact_method: ImpactMethod) -> RefStatus:
        return self.data.put_impact_method(impact_method)

    def locations(self) -> Iterable[Location]:
        for location in self.data.locations(Empty()):
            yield location

    def location(self, id='', name='') -> LocationStatus:
        return self.data.location(Ref(id=id, name=name))

    def put_location(self, location: Location) -> RefStatus:
        return self.data.put_location(location)

    def parameters(self) -> Iterable[Parameter]:
        for parameter in self.data.parameters(Empty()):
            yield parameter

    def parameter(self, id='', name='') -> ParameterStatus:
        return self.data.parameter(Ref(id=id, name=name))

    def put_parameter(self, parameter: Parameter) -> RefStatus:
        return self.data.put_parameter(parameter)

    def processes(self) -> Iterable[Process]:
        for process in self.data.processes(Empty()):
            yield process

    def process(self, id='', name='') -> ProcessStatus:
        return self.data.process(Ref(id=id, name=name))

    def put_process(self, process: Process) -> RefStatus:
        return self.data.put_process(process)

    def product_systems(self) -> Iterable[ProductSystem]:
        for system in self.data.product_systems(Empty()):
            yield system

    def product_system(self, id='', name='') -> ProductSystemStatus:
        return self.data.product_system(Ref(id=id, name=name))

    def put_product_system(self, product_system: ProductSystem) -> RefStatus:
        return self.data.put_product_system(product_system)

    def projects(self) -> Iterable[Project]:
        for project in self.data.projects(Empty()):
            yield project

    def project(self, id='', name='') -> ProjectStatus:
        return self.data.project(Ref(id=id, name=name))

    def put_project(self, project: Project) -> RefStatus:
        return self.data.put_project(project)

    def social_indicators(self) -> Iterable[SocialIndicator]:
        for indicator in self.data.social_indicators(Empty()):
            yield indicator

    def social_indicator(self, id='', name='') -> SocialIndicatorStatus:
        return self.data.social_indicator(Ref(id=id, name=name))

    def put_social_indicator(self, social_indicator: SocialIndicator) -> RefStatus:
        return self.data.put_social_indicator(social_indicator)

    def sources(self) -> Iterable[Source]:
        for source in self.data.sources(Empty()):
            yield source

    def source(self, id='', name='') -> SourceStatus:
        return self.data.source(Ref(id=id, name=name))

    def put_source(self, source: Source) -> RefStatus:
        return self.data.put_source(source)

    def unit_groups(self) -> Iterable[UnitGroup]:
        for group in self.data.unit_groups(Empty()):
            yield group

    def unit_group(self, id='', name='') -> UnitGroupStatus:
        return self.data.unit_group(Ref(id=id, name=name))

    def put_unit_group(self, unit_group: UnitGroup) -> RefStatus:
        return self.data.put_unit_group(unit_group)
