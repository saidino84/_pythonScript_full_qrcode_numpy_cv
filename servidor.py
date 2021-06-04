import os
import socket
import threading


clientes=set()
def main():
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	host=socket.gethostbyname(socket.gethostname())
	port=12345

	sock.bind((host,port))
	print("server listenning")
	sock.listen(4)
	print("[waiting for client].." )

	while True:

		client, enderec=sock.accept()
		print(" Cliente conectado com sucesso")
		dado=client.recv(1024)
		print("[received] ",dado.decode('utf-8'))
		response=input("[you]>>")
		sock.send(bytes(esponse,encoding="utf-8"))
		if not dado:
			break
	sock.close()

main()
