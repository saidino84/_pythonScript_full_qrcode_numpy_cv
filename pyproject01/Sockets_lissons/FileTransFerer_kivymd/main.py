from kivy.animation import Animation
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.theming import ThemeManager
from screens.receiver import ReceiverScreen
from screens.sender import SenderScreen
from kivy.core.window import Window
from kivy.utils import platform

if platform =="android":
    from android import request_permissions, Permissions

Window.size=(430,760)

class MainScreen(Screen):

    def __init__(self,**kwargs):
        super(MainScreen, self).__init__(**kwargs)
    def on_enter(self,*arg):
        if platform =="android":
            request_permissions([
                Permissions.READ_EXTENAL_STORAGE,
                Permissions.WRITE_EXTERNAL_STORAGE
            ])

        btn_send=self.ids['btn_send']
        btn_receive=self.ids['btn_receive']

        anim1=Animation(opacity=1,
                        md_bg_color=(.3, .3, .3, 1),
                        pos_hint={'y':.6}, duration=2)
        anim2=Animation(
            md_bg_color=(.2,.2,.2,1),
            opacity=1,
            pos_hint={'y':.6},
            t="in_quad"
            )

        anim2.start(btn_send)
        anim1.start(btn_receive)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.accent_palette= "Lime"
        self.transition=['TransitionBase', 'ShaderTransition', 'SlideTransition',
           'SwapTransition', 'FadeTransition', 'WipeTransition',
           'FallOutTransition', 'RiseInTransition', 'NoTransition',
           'CardTransition']
        self.sm=ScreenManager()
        self.sm.add_widget(MainScreen())
        self.sm.add_widget(ReceiverScreen())
        self.sm.add_widget(SenderScreen())
        return self.sm

if __name__ == "__main__":
    MainApp().run()
