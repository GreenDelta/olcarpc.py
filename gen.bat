@echo off

protoc  --python_out=olcarpc --mypy_out=olcarpc olca.proto
