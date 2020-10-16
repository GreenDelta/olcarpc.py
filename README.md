# olca-grpc.py
This is an experiment to replace the internals of
[olca-ipc.py](https://github.com/GreenDelta/olca-ipc.py). 

```batch
rem get the project
git clone https://github.com/msrocka/olca-grpc.py.git
cd olca-grpc.py

rem create a virtual environment and activate it
py -m venv env
.\env\Scripts\activate.bat

rem install the requirements
pip install -r requirements.txt

rem install the project
pip install -e .

rem ... then start the Python interpreter
python
```

python -m pip install grpcio-tools

py -m grpc_tools.protoc -I. --python_out=olcarpc --grpc_python_out=olcarpc services.proto