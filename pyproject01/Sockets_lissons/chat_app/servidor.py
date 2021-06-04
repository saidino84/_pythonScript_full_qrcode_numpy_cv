import socket
import threading
import sys
import threading
import pickle


class Server():
    '''this is server side'''

    def __init__(self, host='', port=3001):
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)

        self.acceitar_thread = threading.Thread(target=self.aceitar_connection)
        self.processar_threading = threading.Thread(target=self.process_connection)

        self.acceitar_thread.daemon = True
        self.acceitar_thread.start()

        self.processar_threading.daemon = True
        self.processar_threading.start()

        #     thread_principal/ hillo principale
        while True:
            if len(self.clientes) >0:
                msg = input("\033[32m[server send]\033[m >>")
                if msg=='x':
                    self.sock.close()
                    sys.exit()
                else:
                    pass

    def aceitar_connection(self):
        print('\033[35 ACEITANDO CONECTIONS]')
        while True:
            try:
                connetion, addr = self.sock.accept()
                connetion.setblocking(False)
                self.clientes.append(connetion)
                if len(self.clientes) > 1:
                    print(f'\033[32m[new connection]033[m')
                else:
                    print(f'\033[36m[first coection]\033[m {addr}')
            except Exception as e:
                # print(f'\033[32m[acceptconnection]\033[mOcooreu um erro de [{e}')
                ...

    def process_connection(self):
        print('[Processing initialized]')
        while True:
            if len(self.clientes) > 0:
                for client in self.clientes:
                    try:
                        dada = client.recv(1024)
                        # print('clientes ',self.clientes[0][5])
                        # print(dada)
                        # if dada:
                        #     dada = pickle.loads(dada)
                            # print(f'[from {client}] \033[034m{dada}\033[m')
                            # vou enviar amessage pra os clientes excepto ocliente k enviou
                            # self.send_message_to_all(f'from_[{client}] : >>{dada}', client)
                    except  Exception as e:
                        # print("\033[31m [processing erro]",e)
                        ...

    def send_message_to_all(self, mesage, fromclient):
        fromclient.send(pickle.dumps("you send it"))
        for client in self.clients:
            try:
                if client != fromclient:
                    client.send(pickle.dumps(mesage))
                else:
                    client.send(pickle.dumps('\033[37m[your message has  send]\033[m'))
            except Exception as e:
                # o erro aqui vai acontecer se a connectio de la cliente nao xta activa e precisamos remove lo
                # da lista dos meus clients
                print('\033[31m[send all error]\033[m', e.message)
                print(f'removing the client {client}')
                self.clients.remove(client)


if __name__ == '__main__':
    server = Server()
