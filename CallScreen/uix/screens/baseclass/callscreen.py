import os
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivymd.color_definitions import colors
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp

# Читаем и загружаем KV файл
with open(os.path.join(os.getcwd(), "uix",
                       "screens",
                       "kv",
                       "callscreen.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class CallScreen(MDScreen):
    open_call_box = False
    blur_value = NumericProperty(0)

    def animation_title_image(self, title_image):
        """
        :type title_image: <kivymd.utils.fitimage.FitImage object>
        """

        if not self.open_call_box:
            # Анимация развертывания титульного изображения на весь экран.
            Animation(size_hint_y=1,
                      d=0.6,
                      t="in_out_quad").start(title_image)
        else:
            # Анимация возврата титульного изображения к исходному состоянию.
            Animation(size_hint_y=0.45,
                      d=0.6,
                      t="in_out_quad").start(title_image)

    def animation_blur_value(self):
        if not self.open_call_box:
            Animation(blur_value=15,
                      d=0.6,
                      t="in_out_quad").start(self)
        else:
            Animation(blur_value=0,
                      d=0.6,
                      t="in_out_quad").start(self)

    def animation_call_button(self, call_button):
        if self.open_call_box:
            Animation(
                x=self.center_x - call_button.width / 2,
                y=dp(40),
                md_bg_color=get_color_from_hex(colors["Red"]["A700"]),
                d=0.6,
                t="in_out_quad",
            ).start(call_button)
        else:
            Animation(
                y=Window.height * 45 / 100 + call_button.height / 2,
                x=self.width - call_button.width - dp(20),
                md_bg_color=get_color_from_hex(colors["Green"]["A700"]),
                d=0.6,
                t="in_out_quad",
            ).start(call_button)
