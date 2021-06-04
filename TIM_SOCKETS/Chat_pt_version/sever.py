import socket
import sys

HOST={
    "ADDRESS":None,
    "PORT":None,
    "servidor":False
}

def definir_host(escolha):
    print("Digite aqui a porta desejada")
    HOST["PORT"]=int(input("[port] >>"))
    print("Digite o endereco IPV4")
    HOST['ADDRESS']=input("[IPV4] >>")

    if escolha ==1:
        HOST['seridor']=True



def menu():
    print("[Digite 1 se deseja agir como servidor ou 2 como cliente]")
    return int(input(" 1/2 server/client?"))


def main():
    escolha =menu()
    definir_host(escolha)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST['ADDRESS'], HOST['PORT']))
        print('Esperando por conexoes')
        sock.listen()

        conn, addres =sock.accept()

a="qual e seu nome ?"
print(a)
