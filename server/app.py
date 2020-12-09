import grpc
from concurrent import futures
import time

import pedra_pb2_grpc
from implementacao import Partida


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

pedra_pb2_grpc.add_PartidaServicer_to_server(Partida(), server)

server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
