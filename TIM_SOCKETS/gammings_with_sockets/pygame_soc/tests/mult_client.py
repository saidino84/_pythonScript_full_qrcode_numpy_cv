from socket import *
import threading

class Cliente(threading.Thread):
    '''Classe que gera os clientes'''
    def __init__(self, c ,servidor , porta , *messagem):
        # Numero de identificacao de cliente
        self.c=c
        self.servidor =servidor # seridor a ser conectado
        self.porta =porta # porta  aser connectada
        self.sms =messagem
        threading.Thread.__init__(self)

    def run(self) -> None:
        # criamos o socket e o connectamos ao servidor
        socket_objecto=socket(AF_INET, SOCK_STREAM)
        socket_objecto.connect( (self.servidor, self.porta))

        """Mandando messagem linha por linha"""
        for linha in self.sms:
            socket_objecto.send(linha)

        #depois de mandar uma linha esperamos um resposta do servidor"""
            data = socket_objecto.recv(1024)
            print('Cliente ', self.c, 'Recebeu :',data)

#         por fim fechamos o a conexao
        socket_objecto.close()

"""Configuraçào de conexao do servidor 
o nome do servidor pode ser o endereço de IP ou dominio
(ola.python.net)
"""
serverhost = 'localhost'
serverport = 50007

# messagem a ser enviada porem em bytes
mesg = [b'Ola mundo da internet']

for cliente in range(20):
    Cliente(cliente , serverhost, serverport , *mesg).start()

print('Geramos todos  os clientes')