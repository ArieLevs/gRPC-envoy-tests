import argparse
import os
import time

import grpc

# import the generated classes
import messenger_pb2
import messenger_pb2_grpc

SERVER_HOST = os.environ.get('SERVER_HOST', 'localhost')
SERVER_PORT = os.environ.get('SERVER_PORT', '50505')


def _run_client(host, port, word):
    """
    Start a gRPC client, on the input host:port
    :param host: string
    :param port: string
    :param word: string
    :return:
    """
    # open a gRPC channel
    print('open gRPC channel to {}:{}'.format(host, port))
    channel = grpc.insecure_channel('{}:{}'.format(host, port))

    # create a stub (client)
    stub = messenger_pb2_grpc.PyMessengerStub(channel)

    # create a request message
    message = messenger_pb2.MyMessage(string_1=word)

    # sent the request to the server
    try:
        response = stub.MessageLength(message)
        print(response)
    except grpc.RpcError as exc:
        print('client failed to execute due to: {}'.format(str(exc)))


def main():
    parser = argparse.ArgumentParser(description='Python gRPC client')
    parser.add_argument('--word', required=True, help='The word to sent to the server')
    args = vars(parser.parse_args())

    # run_forever
    try:
        while True:
            # Send message from client

            _run_client(SERVER_HOST, SERVER_PORT, args['word'])
            time.sleep(5)
    except KeyboardInterrupt as exc:
        print('client crashed due to: {}'.format(str(exc)))
        pass


if __name__ == "__main__":
    main()
