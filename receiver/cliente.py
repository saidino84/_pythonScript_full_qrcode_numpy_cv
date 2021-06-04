#:/usr/lib/python3
import socket
import sys

# from  kivymd.app import MDApp
import socket
import pickle
from shutil import copyfileobj

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(("localhost",3030))
print('[cliente has connected]')

sock.send(pickle.dumps("hello server"))

while True:
    dada= sock.recv(8888888)
    if not dada:
        print("[not dada]closing the connection...")
        break
    print("Image saving")
    with open('image.jpg','wb') as file:
        copyfileobj(pickle.dumps(dada),file)

print("image saved")
