# olca-grpc.py

This is an experiment to replace [olca-ipc.py](https://github.com/GreenDelta/olca-ipc.py)
with a [gRPC](https://grpc.io/) based implementation. The code of this package
is mainly generated automatically from a set of [proto3 files](./proto). The
[olca-proto](https://github.com/msrocka/olca-proto) currently implements the
corresponding server side.

## Usage
The data exchange is based on a data format that is compatible with the
[olca-schema format](https://github.com/GreenDelta/olca-schema). You can
easily generate JSON(-LD) data sets in the following way:

```python
import uuid
import olcarpc.proto as proto

flow = proto.Flow()
flow.type = 'Flow'
flow.id = str(uuid.uuid4())
flow.name = 'Steel'
flow.flow_type = proto.FlowType.PRODUCT_FLOW
print(proto.to_json(flow))
```

This generates the following JSON output:

```json
{
  "@type": "Flow",
  "@id": "aa2b7b7a-2268-4f29-a1ca-50d4458c4a75",
  "name": "Steel",
  "flowType": "PRODUCT_FLOW"
}
```

With the same format you can talk to openLCA using the gRPC client of this
package:

```python
import olcarpc

with olcarpc.Client(port=8080) as client:
    ref = client.data.put_flow(flow)
    print(ref)
```

This creates a new connection to an openLCA gRPC server that runs on port `8080`.
`data` returns the data service implementation of the [protocol](./protocol.md)
and `put_flow` inserts the given flow in the database of the openLCA server.
