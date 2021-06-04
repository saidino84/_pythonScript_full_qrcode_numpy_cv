import os
import socket

from kivy.lang import Builder
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.screenmanager import Screen, NoTransition, WipeTransition, RiseInTransition
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import Snackbar
from kivy.utils import platform

Builder.load_string("""

<SenderScreen>:
    id:send_screen
    name:'screen_send'
    MDLabel:
        text:'107.0.0.1:8080'
        id:lbl_receiver_ip
        pos_hint:{'center_y':.7}
        halign:'center'
    MDIconButton:
        icon:'keyboard-backspace'
        pos_hint:{'y':.9}
        icon_color:1,0,0,1
        on_release:
            app.sm.current="main_screen"
    MDRaisedButton:
        text:'choose file'
        pos_hint:{'y':.2,'x':.5}
        halign:'center'
        on_release:
            root.open_file_manager()
    MDCard:
        #md_bg_color:app.theme_cls.primary_
        elevation:10
        orientation:'horizontal'
        size_hint:1,None
        height:self.minimum_height
        padding:10
        MDLabel:
            text:'Not connected'
            id:lbl_conection_state
            halign:'center'
            color_text:1,1,1,1
            color:.61,1,1,1




#conteudo de popup
<ReceiverIpContent>:
    orientation:'horizontal'
    size_hint_x:1
    padding:10

    MDBoxLayout:
        # size_hint_x:.5
        orientation:'vertical'
        MDTextField:
            id:edt_receiver_ip
            # mode:'rectangle'
            input_type:'number' #'text', 'number', 'url', 'mail', 'datetime', 'tel', 'address']
            # size_hint_x:.5
            hint_text:'167.0.0.1'
            helper_text:'receiver ip adress'
            helper_text_mode:'on_focus'
        MDTextField:
            id:connection_port
            # mode:'rectangle'
            # size_hint_x:.5
            hint_text:'8080'
            disabled:True
            readonly:True
            helper_text:'porta padrao 8080'
    Image:
        source:'icons/claudia_iamge.jpg'



""")
class ReceiverIpContent(MDBoxLayout):

    def __init__(self,**kwargs):
        super(ReceiverIpContent, self).__init__(**kwargs)
    ...





class SenderScreen(Screen):

    receiver_ip = StringProperty()
    filemanager = ObjectProperty(None)
    filemanager_open = BooleanProperty(False)

    def __init__(self,**kwargs):
        super(SenderScreen, self).__init__(**kwargs)
        self.app=MDApp.get_running_app()

    def send_file(self, path):
        port =5001
        buffer_size=1024

        sock=socket.socket()
        sock.connect((self.receiver_ip, port))
        print("Connected..")



    def on_enter(self,*arg):
        def receive_ip_from_input(*ags):
            print(self.prompt_receiver_ip.type)
            print(arg)
            # self.ids['lbl_receiver_ip'].text = self.prompt_receiver_ip.ids['edt_receiver_ip'].text
            ip_editado=self.prompt_receiver_ip.content_cls.ids['edt_receiver_ip'].text
            # ip_editado=self.prompt_receiver_ip.content_cls.ids['edt_receiver_ip'].text
            texto="sou"
            if ip_editado.strip() =="" or len(ip_editado.strip())<7:
                toast("Endereco invalido",3.2)
                Snackbar(text="Endereco Invalido edit denovo").show()
                self.prompt_receiver_ip.content_cls.ids['edt_receiver_ip'].error=True

            else:
                self.receiver_ip=ip_editado.strip()
                toast('Ip conectado')
                self.ids['lbl_receiver_ip'].text=ip_editado
                self.ids['lbl_receiver_ip'].text_color=self.app.theme_cls.primary_color
                self.prompt_receiver_ip.dismiss()
                Snackbar(text="Sucessful").show()
                self.prompt_receiver_ip.dismiss()
                ip_editado = self.prompt_receiver_ip.content_cls.ids['edt_receiver_ip'].error=False

        def cancel_dialog(arg):
            print(arg)
            self.prompt_receiver_ip.dismiss()
            # self.app.sm.transition=WipeTransition()
            self.app.sm.transition=RiseInTransition()
            self.app.sm.current = "main_screen"
        #               )
        btn_cancel=MDFlatButton(text="cancel")
        btn_ok=MDFlatButton(text='ok',text_color=self.app.theme_cls.primary_color)
        self.prompt_receiver_ip=MDDialog(
            title="Digite o endereco IP",
            type='custom',
            size_hint=(.8,.5),
            content_cls=ReceiverIpContent(),
            auto_dismiss=False,
            buttons=[
                 MDFlatButton(text="cancel",text_color=[1,0,0,1],
                              on_release=lambda x:cancel_dialog(x)
                              ),
                 MDFlatButton(text='ok', text_color=self.app.theme_cls.primary_color,
                              on_release=lambda x:receive_ip_from_input()
                              )
            ]
        )
        self.prompt_receiver_ip.open()

    def open_file_manager(self):
        def on_select_path(path):
            print(path)
            on_exit_manager()
            self.filemanager_open=False
            self.path=path
            if path !="":
                print(f" [file]file received  {os.path.splitext(path)}")

            pass

        def on_exit_manager(*args):
            print(f'[exit manager] {args}')
            self.filemanager.close()
            self.filemanager_open=False
            pass

        if self.filemanager is None:

            self.filemanager=MDFileManager(
                exit_manager=on_exit_manager,
                select_path=on_select_path,
                ext='txt,jpg',use_access =False,

                            )
        if platform=="android":
            path="storage/emulated/0/"
        self.filemanager.show("/")
        self.filemanager_open = True
