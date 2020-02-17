import datetime
import logging
import os
import time
import sys
from concurrent import futures

import grpc

import messenger_pb2
import messenger_pb2_grpc

# listen on port default port 50505
SERVER_PORT = os.environ.get('SERVER_PORT', '50505')
LOGGER = logging.getLogger(__name__)


# create a class to define the server functions
class PyMessengerServicer(messenger_pb2_grpc.PyMessengerServicer):

    # the request and response are of type messenger_pb2.MyMessage
    def MessageLength(self, request, context):
        response = messenger_pb2.MyMessage()
        print(type(request))
        response.string_1 = "This is server v1, The length of clients message is: {}".format(len(request.string_1))
        return response


def _run_server(port):
    """
    Start a gRPC server, on the input port
    :param port: string
    :return:
    """
    LOGGER.info('Starting new gRPC server.')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # use the generated function `add_PyMessengerServicer_to_server`, to add the defined class to the server
    messenger_pb2_grpc.add_PyMessengerServicer_to_server(PyMessengerServicer(), server)

    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    print('Server started, listening on port {}.'.format(port))
    _wait_forever(server)


def _wait_forever(server):
    try:
        while True:
            time.sleep(datetime.timedelta(days=1).total_seconds())
    except KeyboardInterrupt:
        server.stop(None)


if __name__ == '__main__':
    handler = logging.StreamHandler(sys.stdout)
    # formatter = logging.Formatter('[PID %(process)d] %(message)s')
    # handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.INFO)
    _run_server(SERVER_PORT)
