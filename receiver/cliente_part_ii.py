#:/usr/lib/python3
import socket
import os
import sys
print("hello python3")
# from  kivymd.app import MDApp
os.chdir(os.path.dirname(__file__))

import socket
import pickle
from shutil import copyfileobj

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(("localhost",30303))
print('[cliente has connected]')

sock.send(pickle.dumps("hello server"))

while True:
    dada= sock.recv(8888888)
    if not dada:
        print("[not dada]closing the connection...")
        break
    print("Image saving")
    with open('image.jpg','wb') as file:
        file.write(dada)
print("image saved")
