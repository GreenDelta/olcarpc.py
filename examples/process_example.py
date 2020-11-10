# this example creates a process with inputs and outputs

import olcarpc as rpc


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

        process = rpc.process_of('Iron Process - Gas cleaning')

        # set the location
        loc = location(client, 'Global')
        process.location.id = loc.id
        process.location.name = loc.name

        # add inputs

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
    f = rpc.flow_of(name, flow_type, quantity)
    status = client.put_flow(f)
    if not status.ok:
        raise RuntimeError(status.error)
    return f


def location(client: rpc.Client, name: str) -> rpc.Location:
    """
    Returns the location with the given name or creates a new one
    if it does not exist yet.
    """
    status = client.location(name=name)
    if status.ok:
        return status.location
    loc = rpc.location_of(name)
    status = client.put_location(loc)
    if not status.ok:
        raise RuntimeError(status.error)
    return loc


if __name__ == '__main__':
    main()
