import os.path
import shutil
import subprocess


#  pip install grpcio-tools
#  pip install mypy-protobuf

def main():
    output_dir = './olcarpc/generated'
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)

    subprocess.call(
        'py -m grpc_tools.protoc  -I./proto' +
        f' --python_out={output_dir}' +
        f' --grpc_python_out={output_dir}' +
        f' --mypy_out={output_dir}' +
        ' ./proto/*.proto')

    modules: set[str] = set()
    for f in os.listdir(output_dir):
        if f.endswith('.py'):
            modules.add(f.rstrip('.py'))

    # fix the module imports see:
    # https://github.com/protocolbuffers/protobuf/issues/1491
    for f in os.listdir(output_dir):
        path = os.path.join(output_dir, f)
        lines = []
        with open(path, 'r', encoding='utf-8') as stream:
            for line in stream:
                lines.append(line.rstrip())
        with open(path, 'w', encoding='utf-8', newline='\n') as stream:
            for line in lines:
                stream.write(fix_import(line, modules) + '\n')

    # generate the init file
    init = os.path.join(output_dir, '__init__.py')
    with open(init, 'w', encoding='utf-8') as stream:
        for mod in modules:
            stream.write(f'from .{mod} import *\n')


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


if __name__ == '__main__':
    main()
