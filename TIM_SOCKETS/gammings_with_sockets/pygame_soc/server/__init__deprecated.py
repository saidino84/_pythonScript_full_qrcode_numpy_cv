import socket
import threading
import pickle
import sys
import client


class Server(threading.Thread):
    def __init__(self,port:int=5000,host:str=socket.gethostbyname(socket.gethostname())):
        self._clients =list()
        self.port = port
        self.host = host
        self._server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((self.port,self.host))
        self._server.listen(2)
        
        """ Thread-1 (accept_thread)-> Listen and accept connections from other clients
            Thread-2 (process_connectio)-> Sending commands to an already connected client
        """
        self.accept_thread = threading.Thread(target=self.accept_connection)
        self.process_connection = threading.Thread(target=self.process_connection)
        
        self.accept_thread.daemon = True
        self.accept_thread.start()
        
        self.process_connection.daemon=True
        self.process_connection.start()
        
        
        '''Thread principal'''
        while True:
            if (len(self._clients)>0):
                msg =input('[server send] >>')
                if msg.find('x') !=-1:
                    self._server.close()
                    sys.exit()
                else:
                    ...
    
    def run(self):
        print(self._clients)
        
        
    
    def handle_connection(self):
        self._server.bind((self.port, self.host))
        

def server_connect():
    print(__name__)