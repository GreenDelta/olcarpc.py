from .olca_pb2 import *

import datetime
import uuid


def unit_of(name='', conversion_factor=1.0) -> Unit:
    unit = Unit()
    unit.id = str(uuid.uuid4())
    unit.name = name
    unit.conversion_factor = conversion_factor
    return unit


def unit_group_of(name: str, unit: Unit) -> UnitGroup:
    unit.reference_unit = True
    group = UnitGroup()
    _set_base_attributes(group, name)
    group.units.append(unit)
    return group


def flow_property_of(name: str, unit_group: UnitGroup) -> FlowProperty:
    fp = FlowProperty()
    _set_base_attributes(fp, name)
    fp.unit_group.type = 'UnitGroup'
    fp.unit_group.id = unit_group.id
    fp.unit_group.name = unit_group.name
    return fp


def flow_of(name: str, flow_type: FlowType, flow_property: FlowProperty) -> Flow:
    flow = Flow()
    _set_base_attributes(flow, name)
    flow.flow_type = flow_type

    prop = FlowPropertyFactor()
    prop.conversion_factor = 1.0
    prop.reference_flow_property = True
    prop.flow_property.id = flow_property.id
    prop.flow_property.name = flow_property.name
    flow.flow_properties.append(prop)
    return flow


def product_flow_of(name: str, flow_property: FlowProperty) -> Flow:
    return flow_of(name, FlowType.PRODUCT_FLOW, flow_property)


def waste_flow_of(name: str, flow_property: FlowProperty) -> Flow:
    return flow_of(name, FlowType.WASTE_FLOW, flow_property)


def elementary_flow_of(name: str, flow_property: FlowProperty) -> Flow:
    return flow_of(name, FlowType.ELEMENTARY_FLOW, flow_property)


def exchange_of(process: Process, flow: Flow, amount=1.0) -> Exchange:
    if process.last_internal_id is None:
        internal_id = 1
    else:
        internal_id = process.last_internal_id + 1
    process.last_internal_id = internal_id
    exchange = Exchange(
        internal_id=internal_id,
        amount=amount)
    exchange.flow.id = flow.id
    exchange.flow.name = flow.name
    return exchange


def input_of(process: Process, flow: Flow, amount=1.0) -> Exchange:
    exchange = exchange_of(process, flow, amount)
    exchange.input = True
    return exchange


def output_of(process: Process, flow: Flow, amount=1.0) -> Exchange:
    exchange = exchange_of(process, flow, amount)
    exchange.input = False
    return exchange


def process_of(name: str) -> Process:
    process = Process()
    _set_base_attributes(process, name)
    process.process_type = ProcessType.UNIT_PROCESS
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
