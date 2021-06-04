import os
os.chdir(os.path.dirname(__file__))

os.system("clear")
print(os.listdir("."))
with open("dictionary.txt",'rb') as file:
    d=file.read()
    print(d)