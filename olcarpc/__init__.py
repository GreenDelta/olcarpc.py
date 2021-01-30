import inspect
from typing import Any, Iterator, List, Optional, Type, Union

import google.protobuf.json_format as jf
import grpc

import olcarpc.services_pb2_grpc as services
from .factory import *
from .olca_pb2 import *
from .services_pb2 import *

import logging as log

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
        self.__channel = grpc.insecure_channel(
            'localhost:%i' % port, options=[
                ('grpc.max_send_message_length', 1024 * 1024 * 1024),
                ('grpc.max_receive_message_length', 1024 * 1024 * 1024),
            ])
        self.__data = services.DataServiceStub(self.__channel)
        self.__flow_maps = services.FlowMapServiceStub(self.__channel)
        self.__results = services.ResultServiceStub(self.__channel)

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
        """Get all `Actor` instances from the database."""
        for actor in self.__data.GetActors(Empty()):
            yield actor

    def get_actor(self, ref_id='', name='') -> Optional[Actor]:
        """Get the actor with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: ActorStatus = self.__data.GetActor(ref)
        if status.ok:
            return status.actor
        s = name if ref_id == '' else ref_id
        log.error('failed to get actor "%s" from database: %s', s, status.error)
        return None

    def put_actor(self, actor: Actor) -> Optional[Ref]:
        """Insert or update the given actor in the database."""
        status: RefStatus = self.__data.PutActor(actor)
        if status.ok:
            return status.ref
        log.error('failed to save actor "%s": %s', actor.id, status.error)
        return None

    def get_categories(self) -> Iterator[Category]:
        """Get all `Category` instances from the database."""
        for category in self.__data.GetCategories(Empty()):
            yield category

    def get_category(self, ref_id='', name='') -> Optional[Category]:
        """Get the category with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: CategoryStatus = self.__data.GetCategory(ref)
        if status.ok:
            return status.category
        s = name if ref_id == '' else ref_id
        log.error('failed to get category "%s" from database: %s',
                  s, status.error)
        return None

    def put_category(self, category: Category) -> Optional[Ref]:
        """Insert or update the given category in the database."""
        status: RefStatus = self.__data.PutCategory(category)
        if status.ok:
            return status.ref
        log.error('failed to save category "%s": %s', category.id, status.error)
        return None

    def get_currencies(self) -> Iterator[Currency]:
        """Get all `Currency` instances from the database."""
        for currency in self.__data.GetCurrencies(Empty()):
            yield currency

    def get_currency(self, ref_id='', name='') -> Optional[Currency]:
        """Get the currency with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: CurrencyStatus = self.__data.GetCurrency(ref)
        if status.ok:
            return status.currency
        s = name if ref_id == '' else ref_id
        log.error('failed to get currency "%s" from database: %s',
                  s, status.error)
        return None

    def put_currency(self, currency: Currency) -> Optional[Ref]:
        """Insert or update the given currency in the database."""
        status: RefStatus = self.__data.PutCurrency(currency)
        if status.ok:
            return status.ref
        log.error('failed to save currency "%s": %s', currency.id, status.error)
        return None

    def get_dq_systems(self) -> Iterator[DQSystem]:
        """
        Get all `DQSystem` instances from the database.
        """
        for dq_system in self.__data.GetDQSystems(Empty()):
            yield dq_system

    def get_dq_system(self, ref_id='', name='') -> Optional[DQSystem]:
        """Get the DQ system with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: DQSystemStatus = self.__data.GetDQSystem(ref)
        if status.ok:
            return status.dq_system
        s = name if ref_id == '' else ref_id
        log.error('failed to get DQ system "%s" from database: %s',
                  s, status.error)
        return None

    def put_dq_system(self, dq_system: DQSystem) -> Optional[Ref]:
        """Insert or update the given DQ system in the database."""
        status: RefStatus = self.__data.PutDQSystem(dq_system)
        if status.ok:
            return status.ref
        log.error('failed to save DQ system "%s": %s',
                  dq_system.id, status.error)
        return None

    def get_flows(self) -> Iterator[Flow]:
        """
        Get all `Flow` instances from the database.
        """
        for flow in self.__data.GetFlows(Empty()):
            yield flow

    def get_flow(self, ref_id='', name='') -> Optional[Flow]:
        """Get the flow with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: FlowStatus = self.__data.GetFlow(ref)
        if status.ok:
            return status.flow
        s = name if ref_id == '' else ref_id
        log.error('failed to get flow "%s" from database: %s', s, status.error)
        return None

    def put_flow(self, flow: Flow) -> Optional[Ref]:
        """Insert or update the given flow in the database."""
        status: RefStatus = self.__data.PutFlow(flow)
        if status.ok:
            return status.ref
        log.error('failed to save flow "%s": %s', flow.id, status.error)
        return None

    def get_flow_properties(self) -> Iterator[FlowProperty]:
        """
        Get all `FlowProperty` instances from the database.
        """
        for flow_property in self.__data.GetFlowProperties(Empty()):
            yield flow_property

    def get_flow_property(self, ref_id='', name='') -> Optional[FlowProperty]:
        """Get the flow property with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: FlowPropertyStatus = self.__data.GetFlowProperty(ref)
        if status.ok:
            return status.flow_property
        s = name if ref_id == '' else ref_id
        log.error('failed to get flow property "%s" from database: %s',
                  s, status.error)
        return None

    def put_flow_property(self, flow_property: FlowProperty) -> Optional[Ref]:
        """Insert or update the given flow property in the database."""
        status: RefStatus = self.__data.PutFlowProperty(flow_property)
        if status.ok:
            return status.ref
        log.error('failed to save flow property "%s": %s', flow_property.id, status.error)
        return None

    def get_impact_categories(self) -> Iterator[ImpactCategory]:
        """
        Get all `ImpactCategory` instances from the database.
        """
        for impact_category in self.__data.GetImpactCategories(Empty()):
            yield impact_category

    def get_impact_category(self, ref_id='', name='') -> Optional[ImpactCategory]:
        """Get the impact category with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: ImpactCategoryStatus = self.__data.GetImpactCategory(ref)
        if status.ok:
            return status.impact_category
        s = name if ref_id == '' else ref_id
        log.error('failed to get impact category "%s" from database: %s',
                  s, status.error)
        return None

    def put_impact_category(self, impact_category: ImpactCategory) -> Optional[Ref]:
        """Insert or update the given impact category in the database."""
        status: RefStatus = self.__data.PutImpactCategory(impact_category)
        if status.ok:
            return status.ref
        log.error('failed to save impact category "%s": %s',
                  impact_category.id, status.error)
        return None

    def get_impact_methods(self) -> Iterator[ImpactMethod]:
        """
        Get all `ImpactMethod` instances from the database.
        """
        for impact_method in self.__data.GetImpactMethods(Empty()):
            yield impact_method

    def get_impact_method(self, ref_id='', name='') -> Optional[ImpactMethod]:
        """Get the impact method with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: ImpactMethodStatus = self.__data.GetImpactMethod(ref)
        if status.ok:
            return status.impact_method
        s = name if ref_id == '' else ref_id
        log.error('failed to get impact method "%s" from database: %s', s, status.error)
        return None

    def put_impact_method(self, impact_method: ImpactMethod) -> Optional[Ref]:
        """Insert or update the given impact method in the database."""
        status: RefStatus = self.__data.PutImpactMethod(impact_method)
        if status.ok:
            return status.ref
        log.error('failed to save impact method "%s": %s', impact_method.id, status.error)
        return None

    def get_locations(self) -> Iterator[Location]:
        """
        Get all `Location` instances from the database.
        """
        for location in self.__data.GetLocations(Empty()):
            yield location

    def get_location(self, ref_id='', name='') -> Optional[Location]:
        """Get the location with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: LocationStatus = self.__data.GetLocation(ref)
        if status.ok:
            return status.location
        s = name if ref_id == '' else ref_id
        log.error('failed to get location "%s" from database: %s',
                  s, status.error)
        return None

    def put_location(self, location: Location) -> Optional[Ref]:
        """Insert or update the given location in the database."""
        status: RefStatus = self.__data.PutLocation(location)
        if status.ok:
            return status.ref
        log.error('failed to save location "%s": %s', location.id, status.error)
        return None

    def get_parameters(self) -> Iterator[Parameter]:
        """
        Get all `Parameter` instances from the database.
        """
        for parameter in self.__data.GetParameters(Empty()):
            yield parameter

    def get_parameter(self, ref_id='', name='') -> Optional[Parameter]:
        """Get the parameter with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: ParameterStatus = self.__data.GetParameter(ref)
        if status.ok:
            return status.parameter
        s = name if ref_id == '' else ref_id
        log.error('failed to get parameter "%s" from database: %s', s, status.error)
        return None

    def put_parameter(self, parameter: Parameter) -> Optional[Ref]:
        """Insert or update the given parameter in the database."""
        status: RefStatus = self.__data.PutParameter(parameter)
        if status.ok:
            return status.ref
        log.error('failed to save parameter "%s": %s', parameter.id, status.error)
        return None

    def get_processes(self) -> Iterator[Process]:
        """
        Get all `Process` instances from the database.
        """
        for process in self.__data.GetProcesses(Empty()):
            yield process

    def get_process(self, ref_id='', name='') -> Optional[Process]:
        """Get the process with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: ProcessStatus = self.__data.GetProcess(ref)
        if status.ok:
            return status.process
        s = name if ref_id == '' else ref_id
        log.error('failed to get process "%s" from database: %s',
                  s, status.error)
        return None

    def put_process(self, process: Process) -> Optional[Ref]:
        """Insert or update the given process in the database."""
        status: RefStatus = self.__data.PutProcess(process)
        if status.ok:
            return status.ref
        log.error('failed to save process "%s": %s', process.id, status.error)
        return None

    def get_product_systems(self) -> Iterator[ProductSystem]:
        """
        Get all `ProductSystem` instances from the database.
        """
        for product_system in self.__data.GetProductSystems(Empty()):
            yield product_system

    def get_product_system(self, ref_id='', name='') -> Optional[ProductSystem]:
        """Get the product system with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: ProductSystemStatus = self.__data.GetProductSystem(ref)
        if status.ok:
            return status.product_system
        s = name if ref_id == '' else ref_id
        log.error('failed to get product system "%s" from database: %s',
                  s, status.error)
        return None

    def put_product_system(self, product_system: ProductSystem) -> Optional[Ref]:
        """Insert or update the given product system in the database."""
        status: RefStatus = self.__data.PutProductSystem(product_system)
        if status.ok:
            return status.ref
        log.error('failed to save product system "%s": %s', product_system.id, status.error)
        return None

    def get_projects(self) -> Iterator[Project]:
        """
        Get all `Project` instances from the database.
        """
        for project in self.__data.GetProjects(Empty()):
            yield project

    def get_project(self, ref_id='', name='') -> Optional[Project]:
        """Get the project with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: ProjectStatus = self.__data.GetProject(ref)
        if status.ok:
            return status.project
        s = name if ref_id == '' else ref_id
        log.error('failed to get project "%s" from database: %s',
                  s, status.error)
        return None

    def put_project(self, project: Project) -> Optional[Ref]:
        """Insert or update the given project in the database."""
        status: RefStatus = self.__data.PutProject(project)
        if status.ok:
            return status.ref
        log.error('failed to save project "%s": %s', project.id, status.error)
        return None

    def get_social_indicators(self) -> Iterator[SocialIndicator]:
        """
        Get all `SocialIndicator` instances from the database.
        """
        for social_indicator in self.__data.GetSocialIndicators(Empty()):
            yield social_indicator

    def get_social_indicator(self, ref_id='', name='') -> Optional[SocialIndicator]:
        """Get the social indicator with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: SocialIndicatorStatus = self.__data.GetSocialIndicator(ref)
        if status.ok:
            return status.social_indicator
        s = name if ref_id == '' else ref_id
        log.error('failed to get social indicator "%s" from database: %s',
                  s, status.error)
        return None

    def put_social_indicator(self, social_indicator: SocialIndicator) -> Optional[Ref]:
        """Insert or update the given social indicator in the database."""
        status: RefStatus = self.__data.PutSocialIndicator(social_indicator)
        if status.ok:
            return status.ref
        log.error('failed to save social indicator "%s": %s',
                  social_indicator.id, status.error)
        return None

    def get_sources(self) -> Iterator[Source]:
        """
        Get all `Source` instances from the database.
        """
        for source in self.__data.GetSources(Empty()):
            yield source

    def get_source(self, ref_id='', name='') -> Optional[Source]:
        """Get the source with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: SourceStatus = self.__data.GetSource(ref)
        if status.ok:
            return status.source
        s = name if ref_id == '' else ref_id
        log.error('failed to get source "%s" from database: %s', s, status.error)
        return None

    def put_source(self, source: Source) -> Optional[Ref]:
        """Insert or update the given source in the database."""
        status: RefStatus = self.__data.PutSource(source)
        if status.ok:
            return status.ref
        log.error('failed to save source "%s": %s', source.id, status.error)
        return None

    def get_unit_groups(self) -> Iterator[UnitGroup]:
        """
        Get all `UnitGroup` instances from the database.
        """
        for unit_group in self.__data.GetUnitGroups(Empty()):
            yield unit_group

    def get_unit_group(self, ref_id='', name='') -> Optional[UnitGroup]:
        """Get the unit group with the given ID or name from the database."""
        ref = Ref(id=ref_id, name=name)
        status: UnitGroupStatus = self.__data.GetUnitGroup(ref)
        if status.ok:
            return status.unit_group
        s = name if ref_id == '' else ref_id
        log.error('failed to get unit group "%s" from database: %s',
                  s, status.error)
        return None

    def put_unit_group(self, unit_group: UnitGroup) -> Optional[Ref]:
        """Insert or update the given unit group in the database."""
        status: RefStatus = self.__data.PutUnitGroup(unit_group)
        if status.ok:
            return status.ref
        log.error('failed to save unit group "%s": %s',
                  unit_group.id, status.error)
        return None

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

    def get_descriptor(self, model_type: Union[str, int, Type],
                       ref_id='', name='') -> RefStatus:
        return self.__data.GetDescriptor(DescriptorRequest(
            type=_model_type(model_type),
            id=ref_id,
            name=name,
        ))

    def get_descriptors(self, model_type: Union[str, int, Type]) -> Iterator[Ref]:
        req = DescriptorRequest(type=_model_type(model_type))
        for d in self.__data.GetDescriptors(req):
            yield d

    def calculate(self, system: Ref,
                  method: Optional[Ref] = None,
                  nw_set: Optional[Ref] = None,
                  allocation=AllocationType.NO_ALLOCATION,
                  with_costs=False,
                  unit: Optional[Ref] = None,
                  flow_property: Optional[Ref] = None,
                  parameters: Optional[List[ParameterRedef]] = None) -> ResultStatus:
        setup = CalculationSetup(
            product_system=system,
            impact_method=method,
            nw_set=nw_set,
            allocation_method=allocation,
            with_costs=with_costs,
            unit=unit,
            flow_property=flow_property,
            parameter_redefs=parameters)
        return self.__results.Calculate(setup)

    def get_inventory(self, result: Result) -> Iterator[FlowResult]:
        inv = self.__results.GetInventory(result)
        for r in inv:
            yield r

    def get_impacts(self, result: Result) -> Iterator[ImpactResult]:
        imp = self.__results.GetImpacts(result)
        for r in imp:
            yield r

    def dispose(self, result: Result) -> Status:
        return self.__results.Dispose(result)


def _model_type(type_info: Union[str, int, Any]):
    """
    Get the respective model type enumeration value for the given type
    information.

    This is an utility function for converting the given type definition to
    a valid `ModelType` enumeration value.
    """
    if type_info is None:
        return ModelType.UNDEFINED_MODEL_TYPE
    if isinstance(type_info, int):
        return type_info
    info = type_info
    if not isinstance(type_info, str):
        info = type_info.__class__.__name__
        if info == 'GeneratedProtocolMessageType':
            info = type_info.DESCRIPTOR.name
    info: str = info.strip().lower().replace('_', '')
    if info == 'actor':
        return ModelType.ACTOR
    if info == 'category':
        return ModelType.CATEGORY
    if info == 'currency':
        return ModelType.CURRENCY
    if info == 'dqsystem':
        return ModelType.DQ_SYSTEM
    if info == 'flow':
        return ModelType.FLOW
    if info == 'flowproperty':
        return ModelType.FLOW_PROPERTY
    if info == 'impactcategory':
        return ModelType.IMPACT_CATEGORY
    if info == 'impactmethod':
        return ModelType.IMPACT_METHOD
    if info == 'location':
        return ModelType.LOCATION
    if info == 'nwset':
        return ModelType.NW_SET
    if info == 'parameter':
        return ModelType.PARAMETER
    if info == 'process':
        return ModelType.PROCESS
    if info == 'productsystem':
        return ModelType.PRODUCT_SYSTEM
    if info == 'project':
        return ModelType.PROJECT
    if info == 'socialindicator':
        return ModelType.SOCIAL_INDICATOR
    if info == 'source':
        return ModelType.SOURCE
    if info == 'unit':
        return ModelType.UNIT
    if info == 'unitgroup':
        return ModelType.UNIT_GROUP
