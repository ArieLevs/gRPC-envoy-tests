
## Build image
```bash
docker build -t arielev/grpc-messenger .
docker push docker.io/arielev/grpc-messenger:latest
```


## Local testing
This container needs to be override with exec command,  
To run on local host execute:
```bash
SERVER_HOST=localhost
SERVER_PORT=50505

# Start server
docker run \
    --network host \
    -p 50505:50505 \
    --env SERVER_HOST=${SERVER_HOST} \
    --env SERVER_PORT=${SERVER_PORT} \
    grpc-messenger/grpc-messenger \
    python /messenger/server.py

# Start client
docker run \
    --network host \
    --env SERVER_HOST=${SERVER_HOST} \
    --env SERVER_PORT=${SERVER_PORT} \
    grpc-messenger/grpc-messenger \
    python /messenger/client.py --word arielevs
```
