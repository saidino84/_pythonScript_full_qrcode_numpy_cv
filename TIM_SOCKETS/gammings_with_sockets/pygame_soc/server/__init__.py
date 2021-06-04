import socket
import threading
import pickle
import sys
import client


class Server():
    def __init__(self,port:int=5000,host:str=socket.gethostbyname(socket.gethostname())):
        self._clients =list()
        self.port = port
        self.host = host
        self._server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((self.port,self.host))
        self._server.listen(2)
        self._current_id='0'
        
        """ Thread-1 (accept_thread)-> Listen and accept connections from other clients
            Thread-2 (process_connectio)-> Sending commands to an already connected client
        """
        self.accept_thread = threading.Thread(target=self.accept_connection)
        self.process_connection_thread = threading.Thread(target=self.process_connection)
        
        self.accept_thread.daemon = True
        self.accept_thread.start()
        
        self.process_connection_thread.daemon=True
        self.process_connection_thread.start()
        
        
        '''Thread principal'''
        
                    ...
    def accept_connection(self):
        while True:
            try:
                connection, addr = self._server.accept()
                connection.setblocking(False)
                self._clients.append(connection)
                if len(self._clients) > 1:
                    print(f'\033[32m[new connection]033[m id {self._clients.find(connection)}')
                else:
                    print(f'\033[36m[first coection]\033[m {addr}')
            except Exception as e:
                print(str(e))
        
    def process_connection(self,conn):
        conn.se
        
        ...
    
        
        
    
    def handle_connection(self):
        self._server.bind((self.port, self.host))
        

def server_connect():
    print(__name__)