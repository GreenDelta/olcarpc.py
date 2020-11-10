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
            ('Air Blast', rpc.FlowType.PRODUCT_FLOW, 245.8751543969349),
            ('Combustion Air', rpc.FlowType.WASTE_FLOW, 59.764430236449158),
            ('Hematite Pellets', rpc.FlowType.PRODUCT_FLOW, 200),
            ('Coke', rpc.FlowType.PRODUCT_FLOW, 50),
            ('Limestone', rpc.FlowType.PRODUCT_FLOW, 30.422441963816247),
            ('Steel Scrap', rpc.FlowType.WASTE_FLOW, 1.8853256607049331),
            ('Reductant', rpc.FlowType.PRODUCT_FLOW, 16),
            ('Washing Solution', rpc.FlowType.PRODUCT_FLOW, 75),
        ]
        for (name, flow_type, amount) in inputs:
            f = flow(client, name, flow_type, mass)
            i = rpc.input_of(process, f, amount)
            process.exchanges.append(i)

        # add outputs
        outputs = [
            ('Slag', rpc.FlowType.WASTE_FLOW, 33.573534216580185),
            ('Carbon dioxide', rpc.FlowType.ELEMENTARY_FLOW, 140.44236409682583),
            ('Water vapour', rpc.FlowType.ELEMENTARY_FLOW, 30.591043638569072),
            ('Sulfur dioxide', rpc.FlowType.ELEMENTARY_FLOW, 0.01134867565288134),
            ('Air', rpc.FlowType.ELEMENTARY_FLOW, 158.58576460676247),
            ('Pig Iron', rpc.FlowType.PRODUCT_FLOW, 138.2370620852756),
            ('Heat Loss', rpc.FlowType.WASTE_FLOW, 32727.272727272728),
            ('Coarse Dust', rpc.FlowType.ELEMENTARY_FLOW, 1.4340290871696806),
            ('Scrubber Sludge', rpc.FlowType.WASTE_FLOW, 56.261517810249792),
            ('Fine Dust', rpc.FlowType.ELEMENTARY_FLOW, 0.18398927491951844),
        ]
        for (name, flow_type, amount) in outputs:
            f = flow(client, name, flow_type, mass)
            o = rpc.output_of(process, f, amount)
            if name == 'Pig Iron':
                o.quantitative_reference = True
            process.exchanges.append(o)

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
