import uuid
import olcarpc as rpc

import google.protobuf.json_format as format


def main():
    flow = rpc.ProtoFlow(
        type=rpc.Flow,
        id=str(uuid.uuid4()),
        name='Steel',
        flow_type=rpc.ProtoFlowType.PRODUCT_FLOW)
    print(format.MessageToJson(flow))


if __name__ == '__main__':
    main()
