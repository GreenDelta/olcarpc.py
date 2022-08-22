import olcarpc as rpc

from google.protobuf.empty_pb2 import Empty


def print_flow_maps():
    with rpc.Client() as client:
        for flow_map_name in client.flow_maps.GetAll(Empty()):
            print(flow_map_name)


def copy():
    with rpc.Client() as client:
        flow_map: rpc.ProtoFlowMap = client.flow_maps.Get(
            rpc.ProtoFlowMapName(name='ILCD_Import.csv'))
        flow_map.name = 'My copy.csv'
        client.flow_maps.Put(flow_map)


def delete():
    with rpc.Client() as client:
        client.flow_maps.Delete(rpc.ProtoFlowMapName(name='My copy.csv'))


def create():
    flow_map = rpc.ProtoFlowMap(name='hsc2ei.csv')
    entry = rpc.ProtoFlowMapEntry(
        conversion_factor=1.0,
        to=rpc.ProtoFlowMapRef(
            flow=rpc.ProtoRef(
                id='64cea105-f89a-4f95-ae44-84ff904a28fc',
                name='limestone, crushed, washed',
                ref_unit='kg',
            ),
            provider=rpc.ProtoRef(
                id='a321ecf5-907e-3d93-bcd9-2f1a9b5a1189',
                name='limestone production, crushed, washed ...',
                location='RoW'
            )))

    source: rpc.ProtoFlowMapRef = getattr(entry, 'from')
    source.flow.id = 'hsc/Limestone'
    source.flow.name = 'Limestone'
    source.flow.ref_unit = 'kg'
    flow_map.mappings.append(entry)

    with rpc.Client() as client:
        client.flow_maps.Put(flow_map)


if __name__ == '__main__':
    # print_flow_maps()
    # copy()
    # delete()
    create()
