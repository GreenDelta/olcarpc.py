from .olca_pb2 import *
import google.protobuf.json_format as jf


def to_json(entity, indent: int = 2) -> str:
    return jf.MessageToJson(entity, indent=indent)
