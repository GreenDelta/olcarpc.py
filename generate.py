import os
import subprocess


#  pip install grpcio-tools
#  pip install mypy-protobuf

def main():
    for proto in os.listdir('proto'):
        print(proto)
        subprocess.call(
            'py -m grpc_tools.protoc'
            ' -I./proto'
            ' --python_out=./olcarpc/generated'
            ' --grpc_python_out=./olcarpc/generated'
            ' --mypy_out=./olcarpc/generated'
            ' ./proto/' + proto)
        """
        subprocess.call(
            'protoc'
            ' -I./proto'
            ' --python_out=./olcarpc/generated'
            ' --mypy_out=./olcarpc/generated'
            ' ./proto/' + proto)
            """


if __name__ == '__main__':
    main()
