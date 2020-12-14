import inspect
from typing import Any, Iterator, Type, Union

import google.protobuf.json_format as jf
import grpc

import olcarpc.services_pb2_grpc as services
from .factory import *
from .olca_pb2 import *
from .services_pb2 import *

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
        Get an instance of `Actor` by ID or name from the database.
        """
        return self.__data.GetActor(Ref(id=ref_id, name=name))

    def put_actor(self, actor: Actor) -> RefStatus:
        """
        Save or update the given `Actor` instance in the database.
        """
        return self.__data.PutActor(actor)

    def get_categories(self) -> Iterator[Category]:
        """
        Get all `Category` instances from the database.
        """
        for category in self.__data.GetCategories(Empty()):
            yield category

    def get_category(self, ref_id='', name='') -> CategoryStatus:
        """
        Get an instance of `Category` by ID or name from the database.
        """
        return self.__data.GetCategory(Ref(id=ref_id, name=name))

    def put_category(self, category: Category) -> RefStatus:
        """
        Save or update the given `Category` instance in the database.
        """
        return self.__data.PutCategory(category)

    def get_currencies(self) -> Iterator[Currency]:
        """
        Get all `Currency` instances from the database.
        """
        for currency in self.__data.GetCurrencies(Empty()):
            yield currency

    def get_currency(self, ref_id='', name='') -> CurrencyStatus:
        """
        Get an instance of `Currency` by ID or name from the database.
        """
        return self.__data.GetCurrency(Ref(id=ref_id, name=name))

    def put_currency(self, currency: Currency) -> RefStatus:
        """
        Save or update the given `Currency` instance in the database.
        """
        return self.__data.PutCurrency(currency)

    def get_dq_systems(self) -> Iterator[DQSystem]:
        """
        Get all `DQSystem` instances from the database.
        """
        for dq_system in self.__data.GetDQSystems(Empty()):
            yield dq_system

    def get_dq_system(self, ref_id='', name='') -> DQSystemStatus:
        """
        Get an instance of `DQSystem` by ID or name from the database.
        """
        return self.__data.GetDQSystem(Ref(id=ref_id, name=name))

    def put_dq_system(self, dq_system: DQSystem) -> RefStatus:
        """
        Save or update the given `DQSystem` instance in the database.
        """
        return self.__data.PutDQSystem(dq_system)

    def get_flows(self) -> Iterator[Flow]:
        """
        Get all `Flow` instances from the database.
        """
        for flow in self.__data.GetFlows(Empty()):
            yield flow

    def get_flow(self, ref_id='', name='') -> FlowStatus:
        """
        Get an instance of `Flow` by ID or name from the database.
        """
        return self.__data.GetFlow(Ref(id=ref_id, name=name))

    def put_flow(self, flow: Flow) -> RefStatus:
        """
        Save or update the given `Flow` instance in the database.
        """
        return self.__data.PutFlow(flow)

    def get_flow_properties(self) -> Iterator[FlowProperty]:
        """
        Get all `FlowProperty` instances from the database.
        """
        for flow_property in self.__data.GetFlowProperties(Empty()):
            yield flow_property

    def get_flow_property(self, ref_id='', name='') -> FlowPropertyStatus:
        """
        Get an instance of `FlowProperty` by ID or name from the database.
        """
        return self.__data.GetFlowProperty(Ref(id=ref_id, name=name))

    def put_flow_property(self, flow_property: FlowProperty) -> RefStatus:
        """
        Save or update the given `FlowProperty` instance in the database.
        """
        return self.__data.PutFlowProperty(flow_property)

    def get_impact_categories(self) -> Iterator[ImpactCategory]:
        """
        Get all `ImpactCategory` instances from the database.
        """
        for impact_category in self.__data.GetImpactCategories(Empty()):
            yield impact_category

    def get_impact_category(self, ref_id='', name='') -> ImpactCategoryStatus:
        """
        Get an instance of `ImpactCategory` by ID or name from the database.
        """
        return self.__data.GetImpactCategory(Ref(id=ref_id, name=name))

    def put_impact_category(self, impact_category: ImpactCategory) -> RefStatus:
        """
        Save or update the given `ImpactCategory` instance in the database.
        """
        return self.__data.PutImpactCategory(impact_category)

    def get_impact_methods(self) -> Iterator[ImpactMethod]:
        """
        Get all `ImpactMethod` instances from the database.
        """
        for impact_method in self.__data.GetImpactMethods(Empty()):
            yield impact_method

    def get_impact_method(self, ref_id='', name='') -> ImpactMethodStatus:
        """
        Get an instance of `ImpactMethod` by ID or name from the database.
        """
        return self.__data.GetImpactMethod(Ref(id=ref_id, name=name))

    def put_impact_method(self, impact_method: ImpactMethod) -> RefStatus:
        """
        Save or update the given `ImpactMethod` instance in the database.
        """
        return self.__data.PutImpactMethod(impact_method)

    def get_locations(self) -> Iterator[Location]:
        """
        Get all `Location` instances from the database.
        """
        for location in self.__data.GetLocations(Empty()):
            yield location

    def get_location(self, ref_id='', name='') -> LocationStatus:
        """
        Get an instance of `Location` by ID or name from the database.
        """
        return self.__data.GetLocation(Ref(id=ref_id, name=name))

    def put_location(self, location: Location) -> RefStatus:
        """
        Save or update the given `Location` instance in the database.
        """
        return self.__data.PutLocation(location)

    def get_parameters(self) -> Iterator[Parameter]:
        """
        Get all `Parameter` instances from the database.
        """
        for parameter in self.__data.GetParameters(Empty()):
            yield parameter

    def get_parameter(self, ref_id='', name='') -> ParameterStatus:
        """
        Get an instance of `Parameter` by ID or name from the database.
        """
        return self.__data.GetParameter(Ref(id=ref_id, name=name))

    def put_parameter(self, parameter: Parameter) -> RefStatus:
        """
        Save or update the given `Parameter` instance in the database.
        """
        return self.__data.PutParameter(parameter)

    def get_processes(self) -> Iterator[Process]:
        """
        Get all `Process` instances from the database.
        """
        for process in self.__data.GetProcesses(Empty()):
            yield process

    def get_process(self, ref_id='', name='') -> ProcessStatus:
        """
        Get an instance of `Process` by ID or name from the database.
        """
        return self.__data.GetProcess(Ref(id=ref_id, name=name))

    def put_process(self, process: Process) -> RefStatus:
        """
        Save or update the given `Process` instance in the database.
        """
        return self.__data.PutProcess(process)

    def get_product_systems(self) -> Iterator[ProductSystem]:
        """
        Get all `ProductSystem` instances from the database.
        """
        for product_system in self.__data.GetProductSystems(Empty()):
            yield product_system

    def get_product_system(self, ref_id='', name='') -> ProductSystemStatus:
        """
        Get an instance of `ProductSystem` by ID or name from the database.
        """
        return self.__data.GetProductSystem(Ref(id=ref_id, name=name))

    def put_product_system(self, product_system: ProductSystem) -> RefStatus:
        """
        Save or update the given `ProductSystem` instance in the database.
        """
        return self.__data.PutProductSystem(product_system)

    def get_projects(self) -> Iterator[Project]:
        """
        Get all `Project` instances from the database.
        """
        for project in self.__data.GetProjects(Empty()):
            yield project

    def get_project(self, ref_id='', name='') -> ProjectStatus:
        """
        Get an instance of `Project` by ID or name from the database.
        """
        return self.__data.GetProject(Ref(id=ref_id, name=name))

    def put_project(self, project: Project) -> RefStatus:
        """
        Save or update the given `Project` instance in the database.
        """
        return self.__data.PutProject(project)

    def get_social_indicators(self) -> Iterator[SocialIndicator]:
        """
        Get all `SocialIndicator` instances from the database.
        """
        for social_indicator in self.__data.GetSocialIndicators(Empty()):
            yield social_indicator

    def get_social_indicator(self, ref_id='', name='') -> SocialIndicatorStatus:
        """
        Get an instance of `SocialIndicator` by ID or name from the database.
        """
        return self.__data.GetSocialIndicator(Ref(id=ref_id, name=name))

    def put_social_indicator(self, social_indicator: SocialIndicator) -> RefStatus:
        """
        Save or update the given `SocialIndicator` instance in the database.
        """
        return self.__data.PutSocialIndicator(social_indicator)

    def get_sources(self) -> Iterator[Source]:
        """
        Get all `Source` instances from the database.
        """
        for source in self.__data.GetSources(Empty()):
            yield source

    def get_source(self, ref_id='', name='') -> SourceStatus:
        """
        Get an instance of `Source` by ID or name from the database.
        """
        return self.__data.GetSource(Ref(id=ref_id, name=name))

    def put_source(self, source: Source) -> RefStatus:
        """
        Save or update the given `Source` instance in the database.
        """
        return self.__data.PutSource(source)

    def get_unit_groups(self) -> Iterator[UnitGroup]:
        """
        Get all `UnitGroup` instances from the database.
        """
        for unit_group in self.__data.GetUnitGroups(Empty()):
            yield unit_group

    def get_unit_group(self, ref_id='', name='') -> UnitGroupStatus:
        """
        Get an instance of `UnitGroup` by ID or name from the database.
        """
        return self.__data.GetUnitGroup(Ref(id=ref_id, name=name))

    def put_unit_group(self, unit_group: UnitGroup) -> RefStatus:
        """
        Save or update the given `UnitGroup` instance in the database.
        """
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
