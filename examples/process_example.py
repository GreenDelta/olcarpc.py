import olcarpc as rpc
import uuid


def main():
    with rpc.Client() as client:
        # create a unit group
        units = rpc.ProtoUnitGroup(
            id=str(uuid.uuid4()),
            name='Units of mass',
            units=[rpc.ProtoUnit(
                id=str(uuid.uuid4()),
                name='kg',
                conversion_factor=1.0,
                is_ref_unit=True)])
        client.update.Put(rpc.ProtoDataSet(unit_group=units))
        kg = units.units[0]

        # create a flow property
        mass = rpc.ProtoFlowProperty(
            id=str(uuid.uuid4()),
            name='Mass',
            type=rpc.ProtoFlowPropertyType.PHYSICAL_QUANTITY,
            unit_group=rpc.ProtoRef(id=units.id))
        client.update.Put(rpc.ProtoDataSet(flow_property=mass))

        # create an elementary flow
        co2 = rpc.ProtoFlow(
            id=str(uuid.uuid4()),
            name='CO2',
            flow_type=rpc.ProtoFlowType.ELEMENTARY_FLOW,
            flow_properties=[
                rpc.ProtoFlowPropertyFactor(
                    flow_property=rpc.ProtoRef(id=mass.id),
                    conversion_factor=1.0,
                    is_ref_flow_property=True)])
        client.update.Put(rpc.ProtoDataSet(flow=co2))

        # create a product flow
        steel = rpc.ProtoFlow(
            id=str(uuid.uuid4()),
            name='Steel',
            flow_type=rpc.ProtoFlowType.PRODUCT_FLOW,
            flow_properties=[
                rpc.ProtoFlowPropertyFactor(
                    flow_property=rpc.ProtoRef(id=mass.id),
                    conversion_factor=1.0,
                    is_ref_flow_property=True)])
        client.update.Put(rpc.ProtoDataSet(flow=steel))

        # create a process
        process = rpc.ProtoProcess(
            id=str(uuid.uuid4()),
            name='Steel production',
            process_type=rpc.ProtoProcessType.UNIT_PROCESS,
            exchanges=[
                rpc.ProtoExchange(
                    flow=rpc.ProtoRef(id=steel.id),
                    amount=1.0,
                    is_input=False,
                    is_quantitative_reference=True,
                    flow_property=rpc.ProtoRef(id=mass.id),
                    unit=rpc.ProtoRef(id=kg.id),
                ),
                rpc.ProtoExchange(
                    flow=rpc.ProtoRef(id=co2.id),
                    amount=2.0,
                    is_input=False,
                    flow_property=rpc.ProtoRef(id=mass.id),
                    unit=rpc.ProtoRef(id=kg.id),
                )
            ]
        )
        client.update.Put(rpc.ProtoDataSet(process=process))

        # fetch and print the created process
        print(client.fetch.Get(rpc.GetRequest(type=rpc.Process, id=process.id)))


if __name__ == '__main__':
    main()
