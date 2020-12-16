@echo off

rem this script generates the Python code for our messages and services from
rem the proto3 files. it should be executed from the root folder of this project
rem via scripts\gen.bat.
rem in order to run the script you need to have the following tools installed:
rem * the protoc compiler: https://github.com/protocolbuffers/protobuf/releases
rem * mypy-protobuf for type hints: https://github.com/dropbox/mypy-protobuf);
rem   make sure that the `protoc-gen-mypy` script is in your path
rem * the grpcio-tools via python -m pip install grpcio-tools

rem first update the proto files if we are next to the `olca-modules` repo
if exist ..\olca-modules\olca-proto\src\main\proto (
    xcopy /y ..\olca-modules\olca-proto\src\main\proto .\proto
)

rem generate the python modules
protoc -I.\proto --python_out=olcarpc --mypy_out=olcarpc olca.proto
py -m grpc_tools.protoc -I.\proto --python_out=olcarpc --mypy_out=olcarpc --grpc_python_out=olcarpc services.proto
