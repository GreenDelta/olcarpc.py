# olca-grpc.py
This is an experiment to replace [olca-ipc.py](https://github.com/GreenDelta/olca-ipc.py).
with a [gRPC](https://grpc.io/) based implementation.
[olca-proto](https://github.com/msrocka/olca-proto) currently implements the
corresponding server side.

## Generating the `pb2[_grpc].py[i]` modules
We check in the generated code into version control so this only has to be done
when the `*.proto` files change. You need to have the following tools installed:

* the [Protocol Buffers Compiler](https://github.com/protocolbuffers/protobuf/releases);
  `$ protoc --version` should say something
* for generating type hints we use
  [mypy-protobuf](https://github.com/dropbox/mypy-protobuf); make sure that
  the `protoc-gen-mypy` script is in your path
* finally, install the `grpcio-tools`: `python -m pip install grpcio-tools`

On Windows, you can then just run the `gen.bat` file.
