"""Snake Class"""
from config import WIDTH, HEIGHT
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex as gc


class Snake(Image):
    """Main Snake"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = gc("55FF55")
        self.x = (Window.width/WIDTH)*(WIDTH//2)
        self.y = (Window.height/HEIGHT)*(HEIGHT//2)
        self.size = Window.width/WIDTH, Window.height/HEIGHT


class SnakeTail(Image):
    """Snake Tail"""

    def __init__(self, x=0, y=0, _color=gc("FFFFFF"), **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.color = _color
        self.size = Window.width/WIDTH, Window.height/HEIGHT
