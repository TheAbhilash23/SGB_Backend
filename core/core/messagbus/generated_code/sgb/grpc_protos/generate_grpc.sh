python -m  grpc_tools.protoc -I . --python_out=../generated_grpc/$1 --pyi_out=../generated_grpc/$1 --grpc_python_out=../generated_grpc/$1 $1.proto
