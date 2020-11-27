import olcarpc as rpc


def print_flow_maps():
    with rpc.Client() as client:
        for flow_map_name in client.get_flow_maps():
            print(flow_map_name)


def copy():
    with rpc.Client() as client:
        status: rpc.FlowMapStatus = client.get_flow_map('ILCD_Import.csv')
        if not status.ok:
            raise RuntimeError(status.error)
        flow_map: rpc.FlowMap = status.flow_map
        flow_map.name = 'My copy.csv'
        status: rpc.Status = client.put_flow_map(flow_map)
        if not status.ok:
            raise RuntimeError(status.error)


def delete():
    with rpc.Client() as client:
        status: rpc.Status = client.delete_flow_map('My copy.csv')
        if not status.ok:
            raise RuntimeError(status.error)


def create():
    flow_map = rpc.FlowMap(name='hsc2ei.csv')
    entry = rpc.FlowMapEntry(
        conversion_factor=1.0,
        to=rpc.FlowMapRef(
            flow=rpc.FlowRef(
                id='64cea105-f89a-4f95-ae44-84ff904a28fc',
                name='limestone, crushed, washed',
                ref_unit='kg',
            ),
            provider=rpc.ProcessRef(
                id='a321ecf5-907e-3d93-bcd9-2f1a9b5a1189',
                name='limestone production, crushed, washed ...',
                location='RoW'
            )))

    source: rpc.FlowMapRef = getattr(entry, 'from')
    source.flow.id = 'hsc/Limestone'
    source.flow.name = 'Limestone'
    source.flow.ref_unit = 'kg'
    flow_map.mappings.append(entry)

    with rpc.Client() as client:
        client.put_flow_map(flow_map)


if __name__ == '__main__':
    # print_flow_maps()
    # copy()
    # delete()
    create()
