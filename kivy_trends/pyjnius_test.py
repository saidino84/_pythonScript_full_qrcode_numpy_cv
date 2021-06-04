from time import sleep
from jnius import autoclass
from pprint import pprint
from datetime import datetime
from time import  strftime

import sys,os
os.system("clear")
System= autoclass("java.lang.System")
print("cleared")

System.out.println("Tudo bem ao seu lado???")
d=System.currentTimeMillis()
# print(' time is ',strftime("%d",d))

arrayList= autoclass('java.util.List')
# arrayList.add(20)
 
# pprint(dir(arrayList))

from datetime import datetime
data=datetime.now()
tempo=data.strftime("%A-%b-%Y %H:%M:%S")

print(tempo)
eval(input('>>'))