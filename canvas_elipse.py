from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

root = Builder.load_string("""
<WaterFill@Widget>:
    level: 0
    color: 0, 0, 1
    canvas:
        StencilPush
        Ellipse:
            pos: root.pos
            size: root.size
        StencilUse
        # Color:
        #     rgb: root.color
        Rectangle:
            pos: root.pos
            size: (root.width, root.level*root.height)
        StencilUnUse
        StencilPop

<FloatLayout>:
    WaterFill:
        id: left
        level: 0.4
        pos_hint:  {'x' : 0.10, 'y': 0.4}
        size_hint: 0.4, 0.4
    WaterFill:
        id: right
        pos_hint:  {'x' : 0.55, 'y': 0.4}
        size_hint: 0.4, 0.4
    Button:
        id: button
        text: 'text'
        size_hint: .25, .25
        on_press: root.press_me()
""")

class Principal(FloatLayout):
    def press_me(self):
        current_level = self.ids["right"].level
        self.ids["right"].level = 0.0 if current_level >= 1.0 else current_level + 1.0/9

class TestApp(App):
    def build(self):
        return Principal()

if __name__ == "__main__":
    TestApp().run()
