# this example creates a process with inputs and outputs

import olcarpc as rpc
import uuid


def main():
    with rpc.Client(port=8080) as client:
        # we assume that we are connected to an openLCA
        # database with reference data, so that `Mass`
        # and the respective units are defined.
        # note that you should only get things by name
        # when you are sure that only one entity with
        # this name exists in the database, otherwise
        # it is safer to get things by their IDs

        # get flow property mass
        status = client.flow_property(name='Mass')
        if not status.ok:
            raise RuntimeError('flow property `Mass` does not exist')
        mass: rpc.FlowProperty = status.flow_property

        # get the mass units
        status = client.unit_group(mass.unit_group.id)
        if not status.ok:
            raise RuntimeError('unit group `Units of mass` does not exist')
        units: rpc.UnitGroup = status.unit_group
        kg: rpc.Unit = next(
            filter(lambda u: u.name == 'kg', units.units), None)
        if kg is None:
            raise RuntimeError('unit `kg` does not exist')

        process = rpc.Process(
            id=str(uuid.uuid4()),
            name='Iron Process - Gas cleaning'
        )

        last_id = 0
        inputs = [
            ['Air Blast', rpc.FlowType.PRODUCT_FLOW, 245.8751543969349]
        ]
        for input in inputs:
            f = flow(client, input[0], input[1], mass)
            flow_ref = rpc.FlowRef(id=f.id)
            last_id += 1
            e = rpc.Exchange(
                internal_id=last_id,
                flow=flow_ref,
                input=True,
                amount=input[2]
            )
            process.exchanges.append(e)

        client.put_process(process)
        print(process)


def flow(client: rpc.Client, name: str,
         flow_type: rpc.FlowType, quantity: rpc.FlowProperty) -> rpc.Flow:
    """
    Returns the flow with the given name or creates a new one if it does not
    exist yet.
    """

    status = client.flow(name=name)
    if status.ok:
        return status.flow

    ref_quantity = rpc.FlowPropertyFactor(
        conversion_factor=1.0,
        flow_property=rpc.ref_of(quantity)
    )

    flow = rpc.Flow(
        id=str(uuid.uuid4()),
        name=name,
        flow_type=flow_type,
        flow_properties=[ref_quantity]
    )

    status = client.put_flow(flow)
    if not status.ok:
        raise RuntimeError(status.error)
    return flow


if __name__ == '__main__':
    main()
