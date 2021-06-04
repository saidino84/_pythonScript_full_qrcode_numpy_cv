import socket
from time import sleep

def main():
	host=socket.gethostbyname(socket.gethostname())
	soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.connect((host,12345))
	msg=input("[you]>>")
	soc.send(f"{msg}")
	print(" send sucess full")
	
	sleep(.5)
	dada=soc.recv(1024)
	print(dada.decode("utf-8"))

main()
	

