from grpc import insecure_channel

from pedra_pb2 import Jogada, Simbolo
from pedra_pb2_grpc import PartidaStub


channel = insecure_channel("localhost:50051")

stub = PartidaStub(channel)

jogada = Jogada(simbolo1=Simbolo.PEDRA , simbolo2=Simbolo.PEDRA)

resposta = stub.Jogar(jogada)


print(resposta.vencedor)