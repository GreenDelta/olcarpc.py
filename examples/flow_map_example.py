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


if __name__ == '__main__':
    # print_flow_maps()
    # copy()
    delete()
