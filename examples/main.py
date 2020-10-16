import grpc

import olcarpc.olca_pb2 as model
import olcarpc.services_pb2_grpc as lca

chan = grpc.insecure_channel('localhost:8080')
stub = lca.ModelServiceStub(chan)
flow = stub.getFlow(model.Ref(id='6ecfae7a-6bc2-3d24-996c-1ea4a394f958'))
chan.close()
print(flow.name)
