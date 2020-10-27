import uuid
import olcarpc as rpc

flow = rpc.Flow()
flow.type = 'Flow'
flow.id = str(uuid.uuid4())
flow.name = 'Steel'
flow.flow_type = rpc.FlowType.PRODUCT_FLOW
print(rpc.to_json(flow))
