from pedra_pb2_grpc import PartidaServicer
from pedra_pb2 import Resposta, Simbolo


class Partida(PartidaServicer):
    

    def Jogar(self, request, context):        
        return Resposta(vencedor=Simbolo.PEDRA)
