"""Food Widget"""
from config import WIDTH, HEIGHT
from random import randint
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex as gc


class Food(Image):
    """Food Widget Spawn at random Place"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x = (Window.width/WIDTH)*(randint(0, WIDTH-1))
        self.y = (Window.height/HEIGHT)*(randint(0, HEIGHT-1))
        self.size = Window.width/WIDTH, Window.height/HEIGHT
        self.color = gc("FF5555")
