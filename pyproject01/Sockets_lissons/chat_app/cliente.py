import socket
import sys
import threading
import pickle
from time import sleep
# print(socket.gethostbyname(socket.gethostname()))
class Cliente():
    def __init__(self, host='', port=3001):

        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.connect( (str(host),int(port)))
            self.connected=True
            self.socket.send(pickle.dumps("iam in"))
        except ConnectionRefusedError as e:
            print('\033[31m No connection found waiting for you in this port \033[m')
            self.connected=False
        message_recved_thread=threading.Thread(target=self.msg_recv)
        message_recved_thread.daemon=True
        message_recved_thread.start()
        if self.connected:
            while True:
                message=input(">>").capitalize()
                if 'x' in message:
                    print(f'\033[33m exiting through the convesation with\033[m {host}')
                    self.socket.close()
                    sys.exit()
                else:
                    self.send_message(message)
        print('\033[36m Exited\033[m')

    def msg_recv(self):
        while True:
            try:
                data=self.socket.recv(1024)
                print("[clien received]",data)
                if data:print(f'\033[34m{pickle.loads(data)}\033[m')
                else:break
            except Exception as e:pass
    def send_message(self,msg):
        global host
        self.socket.send(pickle.dumps(msg))
        sleep(1)
        print(f'\033[35mmessge send to\033[m')


c=Cliente()