from .generated.olca_pb2 import *

import datetime
import uuid


def unit_of(name='', conversion_factor=1.0) -> ProtoUnit:
    unit = ProtoUnit()
    unit.id = str(uuid.uuid4())
    unit.name = name
    unit.conversion_factor = conversion_factor
    return unit


def unit_group_of(name: str, unit: ProtoUnit) -> ProtoUnitGroup:
    unit.reference_unit = True
    group = ProtoUnitGroup()
    _set_base_attributes(group, name)
    group.units.append(unit)
    return group


def flow_property_of(name: str,
                     unit_group: ProtoUnitGroup) -> ProtoFlowProperty:
    fp = ProtoFlowProperty()
    _set_base_attributes(fp, name)
    fp.unit_group.type = 'UnitGroup'
    fp.unit_group.id = unit_group.id
    fp.unit_group.name = unit_group.name
    return fp


def flow_of(name: str, flow_type: ProtoFlowType,
            flow_property: ProtoFlowProperty) -> ProtoFlow:
    flow = ProtoFlow()
    _set_base_attributes(flow, name)
    flow.flow_type = flow_type

    prop = ProtoFlowPropertyFactor()
    prop.conversion_factor = 1.0
    prop.reference_flow_property = True
    prop.flow_property.id = flow_property.id
    prop.flow_property.name = flow_property.name
    flow.flow_properties.append(prop)
    return flow


def product_flow_of(name: str, flow_property: FlowProperty) -> Flow:
    return flow_of(name, ProtoFlowType.PRODUCT_FLOW, flow_property)


def waste_flow_of(name: str, flow_property: FlowProperty) -> Flow:
    return flow_of(name, ProtoFlowType.WASTE_FLOW, flow_property)


def elementary_flow_of(name: str, flow_property: FlowProperty) -> Flow:
    return flow_of(name, ProtoFlowType.ELEMENTARY_FLOW, flow_property)


def exchange_of(process: Process, flow: Flow, amount=1.0) -> ProtoExchange:
    if process.last_internal_id is None:
        internal_id = 1
    else:
        internal_id = process.last_internal_id + 1
    process.last_internal_id = internal_id
    exchange = ProtoExchange(
        internal_id=internal_id,
        amount=amount)
    exchange.flow.id = flow.id
    exchange.flow.name = flow.name
    return exchange


def input_of(process: Process, flow: Flow, amount=1.0) -> ProtoExchange:
    exchange = exchange_of(process, flow, amount)
    exchange.input = True
    return exchange


def output_of(process: Process, flow: Flow, amount=1.0) -> ProtoExchange:
    exchange = exchange_of(process, flow, amount)
    exchange.input = False
    return exchange


def process_of(name: str) -> ProtoProcess:
    process = ProtoProcess()
    _set_base_attributes(process, name)
    process.process_type = ProtoProcessType.UNIT_PROCESS
    return process


def location_of(name: str, code=None) -> Location:
    location = Location()
    _set_base_attributes(location, name)
    location.code = code or name
    return location


def _set_base_attributes(entity, name: str):
    entity.id = str(uuid.uuid4())
    entity.type = entity.DESCRIPTOR.name
    entity.name = name
    entity.version = '00.00.000'
    entity.last_change = datetime.datetime.utcnow().isoformat() + 'Z'
