import grpc
import google.protobuf.json_format as jf

from .olca_pb2 import *
from .services_pb2 import *
from .factory import *

import olcarpc.services_pb2_grpc as services

import inspect
from typing import Any, Iterable, Iterator, Type, Union

__pdoc__ = {
    'olca_pb2': False,
    'services_pb2': False,
    'services_pb2_grpc': False,
}


def to_json(entity, indent: int = 2) -> str:
    """
    Converts an entity to a JSON string.

    Parameters
    ----------
    entity: Any rpc message
        The entity you want to convert to JSON (e.g. a `Flow` or `Process`).
    indent: int, optional
        The number of space characters to indent the JSON output, defaults to 2.

    Example
    -------
    ```py
    import olcarpc as rpc

    unit = rpc.unit_of('kg')
    json = rpc.to_json(unit)
    print(json)
    ```
    """
    return jf.MessageToJson(entity, indent=indent)


def ref_of(ref_type: Union[Type, str], ref_id: str, name='') -> Ref:
    """
    Creates a data set reference.

    Parameters
    ----------
    ref_type: Union[Type, str]
        The data set type.
    ref_id: str
        The reference ID (uuid) of the data set
    name: str, optional
        The name of the data set.

    Example
    -------
    ```py
    import olcarpc as rpc
    rpc.ref_of(
        'Flow',
        '071a81fe-5e75-32ee-af1a-734a8a0f3dda',
        'compost plant, open')
    ```

    """
    r = Ref()
    if inspect.isclass(ref_type):
        r.type = ref_type.__name__
    else:
        r.type = ref_type
    r.id = ref_id
    r.name = name
    return r


def to_ref(entity) -> Ref:
    """
    Creates a data set reference from an entity.

    Parameters
    ----------
    entity: Any
        A root entity like a `Flow` or `Process`.

    Example
    -------
    ```py
    import olcarpc as rpc
    unit = rpc.unit_of('kg')
    ref = rpc.to_ref(unit)
    ```
    """
    return ref_of(entity.__class__, entity.id, entity.name)


class Client:

    def __init__(self, port=8080):
        self.__port = port
        self.__channel = grpc.insecure_channel('localhost:%i' % port)
        self.__data = services.DataServiceStub(self.__channel)
        self.__flow_maps = services.FlowMapServiceStub(self.__channel)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self.__channel is not None:
            self.__channel.close()
            self.__channel = None

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
        return self.__data.Delete(r)

    def get_actors(self) -> Iterator[Actor]:
        """
        Get all `Actor` instances from the database.
        """
        for actor in self.__data.GetActors(Empty()):
            yield actor

    def get_actor(self, ref_id='', name='') -> ActorStatus:
        """
        Get an `Actor` by ID or name from the database.
        """
        return self.__data.GetActor(Ref(id=ref_id, name=name))

    def put_actor(self, actor: Actor) -> RefStatus:
        """
        Save or update an `Actor` in the database.
        """
        return self.__data.PutActor(actor)

    def categories(self) -> Iterable[Category]:
        for category in self.__data.GetCategories(Empty()):
            yield category

    def category(self, id='', name='') -> CategoryStatus:
        return self.__data.GetCategory(Ref(id=id, name=name))

    def put_category(self, category: Category) -> RefStatus:
        return self.__data.PutCategory(category)

    def currencies(self) -> Iterable[Currency]:
        for currency in self.__data.GetCurrencies(Empty()):
            yield currency

    def currency(self, id='', name='') -> CurrencyStatus:
        return self.__data.GetCurrency(Ref(id=id, name=name))

    def put_currency(self, currency: Currency) -> RefStatus:
        return self.__data.PutCurrency(currency)

    def dq_systems(self) -> Iterable[DQSystem]:
        for dqSystem in self.__data.GetDQSystems(Empty()):
            yield dqSystem

    def dq_system(self, id='', name='') -> DQSystemStatus:
        return self.__data.GetDQSystem(Ref(id=id, name=name))

    def put_dq_system(self, dq_system: DQSystem) -> RefStatus:
        return self.__data.PutDQSystem(dq_system)

    def flows(self) -> Iterable[Flow]:
        for flow in self.__data.GetFlows(Empty()):
            yield flow

    def flow(self, id='', name='') -> FlowStatus:
        return self.__data.GetFlow(Ref(id=id, name=name))

    def put_flow(self, flow: Flow) -> RefStatus:
        return self.__data.PutFlow(flow)

    def flow_properties(self) -> Iterable[FlowProperty]:
        for p in self.__data.GetFlowProperties(Empty()):
            yield p

    def flow_property(self, id='', name='') -> FlowPropertyStatus:
        return self.__data.GetFlowProperty(Ref(id=id, name=name))

    def put_flow_property(self, flow_property: FlowProperty) -> RefStatus:
        return self.__data.PutFlowProperty(flow_property)

    def impact_categories(self) -> Iterable[ImpactCategory]:
        for impact in self.__data.GetImpactCategories(Empty()):
            yield impact

    def impact_category(self, id='', name='') -> ImpactCategoryStatus:
        return self.__data.GetImpactCategory(Ref(id=id, name=name))

    def put_impact_category(self, impact_category: ImpactCategory) -> RefStatus:
        return self.__data.PutImpactCategory(impact_category)

    def impact_methods(self) -> Iterable[ImpactMethod]:
        for method in self.__data.GetImpactMethods(Empty()):
            yield method

    def impact_method(self, id='', name='') -> ImpactMethodStatus:
        return self.__data.GetImpactMethod(Ref(id=id, name=name))

    def put_impact_method(self, impact_method: ImpactMethod) -> RefStatus:
        return self.__data.PutImpactMethod(impact_method)

    def locations(self) -> Iterable[Location]:
        for location in self.__data.GetLocations(Empty()):
            yield location

    def location(self, id='', name='') -> LocationStatus:
        return self.__data.GetLocation(Ref(id=id, name=name))

    def put_location(self, location: Location) -> RefStatus:
        return self.__data.PutLocation(location)

    def parameters(self) -> Iterable[Parameter]:
        for parameter in self.__data.GetParameters(Empty()):
            yield parameter

    def parameter(self, id='', name='') -> ParameterStatus:
        return self.__data.GetParameter(Ref(id=id, name=name))

    def put_parameter(self, parameter: Parameter) -> RefStatus:
        return self.__data.PutParameter(parameter)

    def processes(self) -> Iterable[Process]:
        for process in self.__data.GetProcesses(Empty()):
            yield process

    def process(self, id='', name='') -> ProcessStatus:
        return self.__data.GetProcess(Ref(id=id, name=name))

    def put_process(self, process: Process) -> RefStatus:
        return self.__data.PutProcess(process)

    def product_systems(self) -> Iterable[ProductSystem]:
        for system in self.__data.GetProductSystems(Empty()):
            yield system

    def product_system(self, id='', name='') -> ProductSystemStatus:
        return self.__data.GetProductSystem(Ref(id=id, name=name))

    def put_product_system(self, product_system: ProductSystem) -> RefStatus:
        return self.__data.PutProductSystem(product_system)

    def projects(self) -> Iterable[Project]:
        for project in self.__data.GetProjects(Empty()):
            yield project

    def project(self, id='', name='') -> ProjectStatus:
        return self.__data.GetProject(Ref(id=id, name=name))

    def put_project(self, project: Project) -> RefStatus:
        return self.__data.PutProject(project)

    def social_indicators(self) -> Iterable[SocialIndicator]:
        for indicator in self.__data.GetSocialIndicators(Empty()):
            yield indicator

    def social_indicator(self, id='', name='') -> SocialIndicatorStatus:
        return self.__data.GetSocialIndicator(Ref(id=id, name=name))

    def put_social_indicator(self, social_indicator: SocialIndicator) -> RefStatus:
        return self.__data.PutSocialIndicator(social_indicator)

    def sources(self) -> Iterable[Source]:
        for source in self.__data.GetSources(Empty()):
            yield source

    def source(self, id='', name='') -> SourceStatus:
        return self.__data.GetSource(Ref(id=id, name=name))

    def put_source(self, source: Source) -> RefStatus:
        return self.__data.PutSource(source)

    def unit_groups(self) -> Iterable[UnitGroup]:
        for group in self.__data.GetUnitGroups(Empty()):
            yield group

    def unit_group(self, id='', name='') -> UnitGroupStatus:
        return self.__data.GetUnitGroup(Ref(id=id, name=name))

    def put_unit_group(self, unit_group: UnitGroup) -> RefStatus:
        return self.__data.PutUnitGroup(unit_group)

    def get_providers_of(
        self, flow: Union[Flow, FlowRef, Ref]) -> Iterator[ProcessRef]:
        flow_ref = FlowRef(
            type='Flow',
            id=flow.id,
            name=flow.name)
        for provider in self.__data.GetProvidersFor(flow_ref):
            yield provider

    def get_flow_maps(self) -> Iterator[str]:
        """
        Get the names of the flow maps that are stored in the database.
        """
        info: FlowMapInfo
        for info in self.__flow_maps.GetAll(Empty()):
            yield info.name

    def get_flow_map(self, name: str) -> FlowMapStatus:
        """
        Get the flow map with the given name from the database.
        """
        return self.__flow_maps.Get(FlowMapInfo(name=name))

    def put_flow_map(self, flow_map: FlowMap) -> Status:
        """
        Saves the given flow map into the database.

        If a flow map with the same name already exists, it updates it in the
        database.
        """
        return self.__flow_maps.Put(flow_map)

    def delete_flow_map(self, name: str) -> Status:
        """
        Delete the flow map with the given name from the database.
        """
        return self.__flow_maps.Delete(FlowMapInfo(name=name))
