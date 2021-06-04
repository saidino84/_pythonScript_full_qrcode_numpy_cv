from kivy.uix.recycleview import RecycleView
from kivymd.app import MDApp
from kivy.uix.screenmanager import FadeTransition, ScreenManager, SwapTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.taptargetview import MDTapTargetView
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.list import TwoLineAvatarListItem, TwoLineAvatarIconListItem
from kivy.clock import Clock
Window.size = (340, 700)


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # sm = ScreenManager()
        #     sm.switch_to(screen1)
        #     # later
        #     sm.switch_to(screen2, direction='left')
        #     # later
        #     sm.switch_to(screen3, direction='right', duration=1.)

    def change_screen(self, screen_to_go):
        self.transition = FadeTransition()
        self.transition.direction = 'top'
        self.current = screen_to_go
        for screen in self.screen_names:
            print(screen)
        print('[current screen is]', self.current)

    def on_kv_post(self, base_widget):
        mainscreen = MainScreen(name="main_screen")
        sendscreen = SenderScreen(name='sender_screen')
        receivescreen = ReceiveScreen(name='receiver_screen')
        self.add_widget(mainscreen)
        self.add_widget(receivescreen)
        self.add_widget(sendscreen)
        return super().on_kv_post(base_widget)


class DadosEnviados(TwoLineAvatarListItem):
    nome = StringProperty()
    icon = StringProperty()
    status = StringProperty()

    def __init__(self, nome='github', **kwargs):
        super().__init__(**kwargs)
        self.nome = nome
        self.icon = nome
        self.status = 'walking.. 28%'
        self.received = 0
        Clock.schedule_interval(self.increment, 1)

    def update_status(self):
        if self.received < 100:
            self.status = f" recebendo aos {self.received}"
        else:
            self.status = f" Recebido com sucesso {self.received}"

    def increment(self, *args):
        from random import randint
        self.received += randint(6, 13)
        if self.received >= 101:
            Clock.unschedule(self.increment, 1)
        self.update_status()
        print('[self.received ] :', self.received)


class MainScreen(MDScreen):
    btn_send = ObjectProperty()

    def __init__(self, **args):
        super().__init__(**args)
        self.app = MDApp().get_running_app()
        self.tap_target_v = MDTapTargetView(
            widget=self.btn_send,
            title_text="Share App ",
            description_text="Clique em aqui pra enviar",

        )

    def start_target_lesson(self, btn, type):
        print(btn)
        self.tap_target_v.widget = btn
        self.tap_target_v.title_text = type
        m = Manager()
        m.change_screen("receiver_screen")
        # if self. tap_target_v.state == "close":
        #     self.tap_target_v.start()
        # else:
        #     if type=="send":
        #         # Manager().current="sender_screen"
        #         m.change_screen('sender_screen')
        #         print('screen changed to sender')
        #     else:
        #         m.change_screen("receive_screen")
        #         print('screen changed to receiver')
        #     # self.tap_target_v.stop()


class SenderScreen(MDScreen):
    dialog = None
    got = False

    def show_dialog_message(self, title, message):

        ok_btn = MDRoundFlatButton(
            text="ok",
            on_release=lambda x: self.dialog.dismiss()
            if self.got
            else print("Action take"),
        )
        if not self.dialog:
            self.got = True
            self.dialog = MDDialog(
                size_hint=[0.8, 0.5],
                title=title,
                text=f" {message}",
                buttons=[ok_btn],
                auto_dismiss=False,
            )
        self.dialog.open()

    def on_enter(self, *args):
        icon = ['language-python', 'language-java', 'language-javascript',
                'language-cpp', 'language-csharp', 'language-html5']
        for i in range(0, len(icon)):
            self.ids['send_list_receive'].add_widget(DadosEnviados(icon[i]))
            self.ids['rv'].data = [{'nome': icon[i]}]


class ReceiveScreen(MDScreen):
    ...


class PyShareApp(MDApp):
    def build(self):
        return Builder.load_file("assets/kv_files/pyshare.kv")


if __name__ == "__main__":
    PyShareApp().run()
