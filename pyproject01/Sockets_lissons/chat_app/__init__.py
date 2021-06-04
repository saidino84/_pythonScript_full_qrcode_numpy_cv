import pickle

def send(msg):
    data=pickle.dumps(msg)

    print(f'message send \t[type of]{type(data)}\t[content] {data}')
    return data
def recv(msg_pcke):
    data=''
    try:
        data=pickle.loads(msg_pcke)
    except Exception as e:
        print(e.message)
    else:
        print(data)
def main():
    c=6
    while c>1:
        c-=1
        msg=input('type the msg')
        data=send(msg)

        input('>>')
        recv(data)
        if "b" in input("cont/break"):break

class Amigo():
    def __init__(self):
        self.nome="joao"
        self.idade=12
    def __repr__(self):
        return f' \033[33m[Nome]\033[m {self.nome}\n \033[34m[idade]\033[m {self.idade}'

a=Amigo()
da=pickle.dumps(a)
print(da)
x=pickle.loads(da)
print(x)