
Start gRPC test on localhost
============================
Install dependencies
```bash
pip install --requirement requirements.txt
```

Install 
Generate gRPC classes
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. messenger.proto
```

Start the server
```bash
# Optional:
# Add SERVER_PORT as environment variable to listen on that port
python server.py
```

Start the client
```bash
# Optional:
# Add relevant SERVER_HOST and SERVER_PORT as environment variable
python client.py --word some_text
```
