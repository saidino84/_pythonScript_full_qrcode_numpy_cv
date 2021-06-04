import socket
import server
import os
import threading
import pickle
from settings import BUFFER_SIZE
class Jogador(threading.Thread):
    '''por default o jogador esta esperand na porta 5000 e host=127.0.1.1 '''
    def __init__(self,porta:int=5000,endereco:int=socket.gethostbyname(socket.gethostname()),):
        assert (type(porta) is int)
        assert (type(endereco) is str)
        self.port=porta
        self.endereco=endereco
        
        threading.Thread.__init__(self)
    
    def run(self):
        self._client_soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._client_soc.connect((self.porta,self.server))
            print(f'[{chr(10004)}][client connection ] sucess')
        except socket.error as soc_error:
            print(f'[{chr(10007)}][client connection error] ')
            

    def send_message(self,dado:bytes):
        self._client_soc.send(pickle.dumps(dado))
        print(f'[{chr(10004)}][client send ] sucess')
    def receve_message(self):
        message = pickle.loads(self._client_soc.recv(BUFFER_SIZE))
        print(f'[{chr(10004)}][client receved ] sucess \n message:{message}')
        
        ...

 