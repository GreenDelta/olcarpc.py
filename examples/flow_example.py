import olcarpc as rpc


def main():
    with rpc.Client() as client:
        mass = client.flow_property(name='Mass').flow_property
        flow = rpc.product_flow_of('butter, fried', mass)
        client.put_flow(flow)
        print(client.flow(flow.id))


if __name__ == '__main__':
    main()
