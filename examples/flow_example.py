import olcarpc as rpc
import uuid


def main():
    with rpc.Client() as client:
        # get the flow property 'Mass' by name
        dataset: rpc.ProtoDataSet = client.fetch.Find(
            rpc.FindRequest(type=rpc.FlowProperty, name='Mass'))

        mass: rpc.ProtoFlowProperty = dataset.flow_property
        if mass is None:
            print('could not find flow property Mass')
            return

        # create a product flow with mass as reference flow property
        flow = rpc.ProtoFlow(
            id=str(uuid.uuid4()),
            name="my product flow",
            flow_type=rpc.ProtoFlowType.PRODUCT_FLOW,
            flow_properties=[
                rpc.ProtoFlowPropertyFactor(
                    flow_property=rpc.ProtoRef(id=mass.id),
                    is_ref_flow_property=True,
                    conversion_factor=1.0)
            ])

        # insert the flow in the database
        client.update.Put(rpc.ProtoDataSet(flow=flow))

        # get it via ID
        print(client.fetch.Get(rpc.GetRequest(type=rpc.Flow, id=flow.id)))


if __name__ == '__main__':
    main()
