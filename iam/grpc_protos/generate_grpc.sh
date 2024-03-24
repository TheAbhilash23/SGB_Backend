python -m  grpc_tools.protoc -I ./ --python_out=../generated_grpc/user --pyi_out=../generated_grpc/user --grpc_python_out=../generated_grpc/user $1.proto
