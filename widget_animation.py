from random import random

from kivy.animation import Animation
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
<Root>:
    AnimRect:
        pos: 500, 300
<AnimRect>:
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')


class Root(Widget):
    pass


class AnimRect(Widget):
    def anim_to_random_pos(self):
        Animation.cancel_all(self)
        random_x = random() * (Window.width - self.width)
        random_y = random() * (Window.height - self.height)

        anim = Animation(x=random_x, y=random_y,
                         duration=2,
                         t='out_elastic')
        anim.start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.anim_to_random_pos()

runTouchApp(Root())
