import uuid
import olcarpc.proto as proto

flow = proto.Flow()
flow.type = 'Flow'
flow.id = str(uuid.uuid4())
flow.name = 'Steel'
flow.flow_type = proto.FlowType.PRODUCT_FLOW
print(proto.to_json(flow))
