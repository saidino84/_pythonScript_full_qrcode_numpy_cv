from subprocess import call
import os

class CallPy(object):
    def __init__(self,path):
        self.path=path
        pass
    
    def call_python_file(self,path=''):
        call(['python3','{}'.format(self.path)])
        
    #     ...
        


path=os.path.dirname(os.path.abspath(__file__))
print(path)
        