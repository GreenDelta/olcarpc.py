# Generates the gRPC code from the schema files in the ./proto folder of this
# project. It first tries to update these proto-files if the project is located
# next to the olca-proto project which contains the current schema definitions.
# (see https://github.com/GreenDelta/olca-proto).
# In order to run the script the following tools need to be installed:
#
# * grpcio-tools
# * mypy-protobuf
#
# Both can be installed via 'pip install' (so
# 'pip install grpcio-tools mypy-protobuf').

import os
import shutil
import subprocess
import pathlib


def sync_protos():
    origin = pathlib.Path('../olca-proto/proto')
    if not origin.exists() or not origin.is_dir():
        return
    print(f'sync proto-files from {origin}')
    target = pathlib.Path('./proto')
    shutil.rmtree(target)
    target.mkdir()
    for f in os.listdir(origin):
        print(f'  copy {f}')
        shutil.copy2(origin / f, target / f)


def generate():
    target = './olcarpc/generated'
    print(f'generate modules in {target}')

    # clean folder
    if os.path.exists(target):
        shutil.rmtree(target)
    os.mkdir(target)

    # exec generator
    command = 'py -m grpc_tools.protoc  -I./proto' \
              f' --python_out={target}' \
              f' --grpc_python_out={target}' \
              f' --mypy_out={target}' \
              ' ./proto/*.proto'
    print(f'  command: {command}')
    subprocess.call(command)

    # collect modules
    modules: set[str] = set()
    for f in os.listdir(target):
        if f.endswith('.py'):
            print(f'  generated: {f}')
            module = f.rstrip('.py')
            modules.add(module)

    # fix the module imports see:
    # https://github.com/protocolbuffers/protobuf/issues/1491
    for f in os.listdir(target):
        path = os.path.join(target, f)
        lines = []
        with open(path, 'r', encoding='utf-8') as stream:
            for line in stream:
                lines.append(line.rstrip())
        with open(path, 'w', encoding='utf-8', newline='\n') as stream:
            for line in lines:
                stream.write(fix_import(line, modules) + '\n')

    # generate the init file
    init = os.path.join(target, '__init__.py')
    with open(init, 'w', encoding='utf-8') as stream:
        for mod in modules:
            stream.write(f'from .{mod} import *\n')
    print(f'  generated: __init__.py')


def fix_import(line: str, mods: set[str]) -> str:
    if not line.startswith('import'):
        return line
    for mod in mods:
        if line == f'import {mod}':
            return f'import olcarpc.generated.{mod} as {mod}'
        pref = f'import {mod} as '
        if line.startswith(pref):
            return f'import olcarpc.generated.{mod} as {line[len(pref):]}'
    return line


def main():
    sync_protos()
    generate()


if __name__ == '__main__':
    main()
