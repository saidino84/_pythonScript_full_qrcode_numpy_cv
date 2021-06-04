import socket

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ReceiverScreen>:
    id:receive_screen
    name:'screen_receiver'
    MDIconButton:
        icon:'keyboard-backspace'
        pos_hint:{'y':.9}
        icon_color:1,0,0,1
        on_release:
            app.sm.current="main_screen"
        
    MDCard:
        orientation:'vertical'
        size_hint:1,None
        adaptive_size:True
        md_bg_color:.3,.3,.5,1
        
        MDLabel:
            halign:'center'
            text:root._connection_state
            color:1,1,1,1
            text_size:self.texture_size
            color:1,.21,.41,1
            
            

""")

class ReceiverScreen(Screen):
    ip=StringProperty()
    _connection_state=StringProperty("Sem conneccao")
    def __init__(self,*args,**kwarg):
        super(ReceiverScreen,self).__init__(*args,**kwarg)
        self.ip=socket.gethostbyname(socket.gethostname())

    def on_enter(self,*arg):
        print(self.ip)
        if self.ip.startswith('127.') or self.ip.startswith("0."):
            sock_client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock_client.connect(('',80))
            print(f"[host] \033[34m {sock_client.getsockname()}")
            # sock_client.close()