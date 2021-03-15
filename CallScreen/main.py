from kivymd.app import MDApp

from uix.screens.baseclass.callscreen import CallScreen


class TestCallScreen(MDApp):
    def build(self):
        return CallScreen()


TestCallScreen().run()
