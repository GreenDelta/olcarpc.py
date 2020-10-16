@echo off

protoc  --python_out=olcarpc --mypy_out=olcarpc olca.proto
py -m grpc_tools.protoc -I. --python_out=olcarpc --mypy_out=olcarpc  --grpc_python_out=olcarpc services.proto