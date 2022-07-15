"""Snake Game"""
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,  Screen
from src import Interface
from kivy.utils import platform
if platform != "android":
    Window.size = (500, 500)


class GameApp(App):
    """Main Game App"""

    def build(self):
        """Build The Game"""
        self.sm = ScreenManager()
        self.interface = Screen()
        self.interface.add_widget(Interface())
        self.sm.add_widget(self.interface)
        return self.sm


if __name__ == "__main__":
    GameApp().run()
