import grpc
import google.protobuf.json_format as jf

from .olca_pb2 import *
from .services_pb2 import *
from .factory import *

import olcarpc.services_pb2_grpc as services

import inspect
from typing import Any, Iterable, Iterator, Union

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

    @property
    def flow_maps(self) -> services.FlowMapServiceStub:
        return services.FlowMapServiceStub(self.chan)

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
        return self.data.Delete(r)

    def actors(self) -> Iterable[Actor]:
        for actor in self.data.GetActors(Empty()):
            yield actor

    def actor(self, id='', name='') -> ActorStatus:
        return self.data.GetActor(Ref(id=id, name=name))

    def put_actor(self, actor: Actor) -> RefStatus:
        return self.data.PutActor(actor)

    def categories(self) -> Iterable[Category]:
        for category in self.data.GetCategories(Empty()):
            yield category

    def category(self, id='', name='') -> CategoryStatus:
        return self.data.GetCategory(Ref(id=id, name=name))

    def put_category(self, category: Category) -> RefStatus:
        return self.data.PutCategory(category)

    def currencies(self) -> Iterable[Currency]:
        for currency in self.data.GetCurrencies(Empty()):
            yield currency

    def currency(self, id='', name='') -> CurrencyStatus:
        return self.data.GetCurrency(Ref(id=id, name=name))

    def put_currency(self, currency: Currency) -> RefStatus:
        return self.data.PutCurrency(currency)

    def dq_systems(self) -> Iterable[DQSystem]:
        for dqSystem in self.data.GetDQSystems(Empty()):
            yield dqSystem

    def dq_system(self, id='', name='') -> DQSystemStatus:
        return self.data.GetDQSystem(Ref(id=id, name=name))

    def put_dq_system(self, dq_system: DQSystem) -> RefStatus:
        return self.data.PutDQSystem(dq_system)

    def flows(self) -> Iterable[Flow]:
        for flow in self.data.GetFlows(Empty()):
            yield flow

    def flow(self, id='', name='') -> FlowStatus:
        return self.data.GetFlow(Ref(id=id, name=name))

    def put_flow(self, flow: Flow) -> RefStatus:
        return self.data.PutFlow(flow)

    def flow_properties(self) -> Iterable[FlowProperty]:
        for p in self.data.GetFlowProperties(Empty()):
            yield p

    def flow_property(self, id='', name='') -> FlowPropertyStatus:
        return self.data.GetFlowProperty(Ref(id=id, name=name))

    def put_flow_property(self, flow_property: FlowProperty) -> RefStatus:
        return self.data.PutFlowProperty(flow_property)

    def impact_categories(self) -> Iterable[ImpactCategory]:
        for impact in self.data.GetImpactCategories(Empty()):
            yield impact

    def impact_category(self, id='', name='') -> ImpactCategoryStatus:
        return self.data.GetImpactCategory(Ref(id=id, name=name))

    def put_impact_category(self, impact_category: ImpactCategory) -> RefStatus:
        return self.data.PutImpactCategory(impact_category)

    def impact_methods(self) -> Iterable[ImpactMethod]:
        for method in self.data.GetImpactMethods(Empty()):
            yield method

    def impact_method(self, id='', name='') -> ImpactMethodStatus:
        return self.data.GetImpactMethod(Ref(id=id, name=name))

    def put_impact_method(self, impact_method: ImpactMethod) -> RefStatus:
        return self.data.PutImpactMethod(impact_method)

    def locations(self) -> Iterable[Location]:
        for location in self.data.GetLocations(Empty()):
            yield location

    def location(self, id='', name='') -> LocationStatus:
        return self.data.GetLocation(Ref(id=id, name=name))

    def put_location(self, location: Location) -> RefStatus:
        return self.data.PutLocation(location)

    def parameters(self) -> Iterable[Parameter]:
        for parameter in self.data.GetParameters(Empty()):
            yield parameter

    def parameter(self, id='', name='') -> ParameterStatus:
        return self.data.GetParameter(Ref(id=id, name=name))

    def put_parameter(self, parameter: Parameter) -> RefStatus:
        return self.data.PutParameter(parameter)

    def processes(self) -> Iterable[Process]:
        for process in self.data.GetProcesses(Empty()):
            yield process

    def process(self, id='', name='') -> ProcessStatus:
        return self.data.GetProcess(Ref(id=id, name=name))

    def put_process(self, process: Process) -> RefStatus:
        return self.data.PutProcess(process)

    def product_systems(self) -> Iterable[ProductSystem]:
        for system in self.data.GetProductSystems(Empty()):
            yield system

    def product_system(self, id='', name='') -> ProductSystemStatus:
        return self.data.GetProductSystem(Ref(id=id, name=name))

    def put_product_system(self, product_system: ProductSystem) -> RefStatus:
        return self.data.PutProductSystem(product_system)

    def projects(self) -> Iterable[Project]:
        for project in self.data.GetProjects(Empty()):
            yield project

    def project(self, id='', name='') -> ProjectStatus:
        return self.data.GetProject(Ref(id=id, name=name))

    def put_project(self, project: Project) -> RefStatus:
        return self.data.PutProject(project)

    def social_indicators(self) -> Iterable[SocialIndicator]:
        for indicator in self.data.GetSocialIndicators(Empty()):
            yield indicator

    def social_indicator(self, id='', name='') -> SocialIndicatorStatus:
        return self.data.GetSocialIndicator(Ref(id=id, name=name))

    def put_social_indicator(self, social_indicator: SocialIndicator) -> RefStatus:
        return self.data.PutSocialIndicator(social_indicator)

    def sources(self) -> Iterable[Source]:
        for source in self.data.GetSources(Empty()):
            yield source

    def source(self, id='', name='') -> SourceStatus:
        return self.data.GetSource(Ref(id=id, name=name))

    def put_source(self, source: Source) -> RefStatus:
        return self.data.PutSource(source)

    def unit_groups(self) -> Iterable[UnitGroup]:
        for group in self.data.GetUnitGroups(Empty()):
            yield group

    def unit_group(self, id='', name='') -> UnitGroupStatus:
        return self.data.GetUnitGroup(Ref(id=id, name=name))

    def put_unit_group(self, unit_group: UnitGroup) -> RefStatus:
        return self.data.PutUnitGroup(unit_group)

    def get_providers_of(
            self, flow: Union[Flow, FlowRef, Ref]) -> Iterator[ProcessRef]:
        flow_ref = FlowRef(
            type='Flow',
            id=flow.id,
            name=flow.name)
        for provider in self.data.GetProvidersFor(flow_ref):
            yield provider

    def get_flow_maps(self) -> Iterator[str]:
        """
        Get the names of the flow maps that are stored in the database.
        """
        info: FlowMapInfo
        for info in self.flow_maps.GetAll(Empty()):
            yield info.name

    def get_flow_map(self, name: str) -> FlowMapStatus:
        """
        Get the flow map with the given name from the database.
        """
        return self.flow_maps.Get(FlowMapInfo(name=name))

    def put_flow_map(self, flow_map: FlowMap) -> Status:
        """
        Saves the given flow map into the database.

        If a flow map with the same name already exists, it updates it in the
        database.
        """
        return self.flow_maps.Put(flow_map)

    def delete_flow_map(self, name: str) -> Status:
        """
        Delete the flow map with the given name from the database.
        """
        return self.flow_maps.Delete(FlowMapInfo(name=name))
