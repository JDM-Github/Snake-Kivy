"""Custom Label"""
from kivy.uix.label import Label
from kivy.metrics import sp
from kivy.utils import get_color_from_hex as gc


class GameLabel(Label):
    """Game Level"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Test Text"
        self.font_size = sp(20)
        self.color = gc("FFFFFF")
