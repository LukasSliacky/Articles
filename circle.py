from kivy.app import App
from kivy.base import runTouchApp

from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.lang import Builder

Builder.load_string('''
<DrawingWidget>:
    canvas:
        Color:
<DrawingWidget>:
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Line:
            circle: self.circle_params
''')


class DrawingWidget(Widget):
    circle_params = ListProperty([0, 0, 50])

    def on_touch_down(self, touch):
        self.on_touch_move(touch)

    def on_touch_move(self, touch):
        self.circle_params = [touch.pos[0], touch.pos[1],
                              touch.pos[0]]


runTouchApp(DrawingWidget())
