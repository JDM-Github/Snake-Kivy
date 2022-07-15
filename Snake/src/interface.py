"""Interface Of Snake Game"""
from calendar import c
from kivy.utils import get_color_from_hex as gc
from config import WIDTH, HEIGHT, SPEED
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.clock import Clock
from widgets import SnakeTail, Snake, GameLabel, Food


class Interface(Widget):
    """Snake Game"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = Window.size
        self.all_variable()
        self.display_field()
        Window.bind(on_keyboard=self.keyboard)
        self.run = Clock.schedule_interval(lambda _: self.run_game(), 1/SPEED)

    def keyboard(self, _, key, *__):
        """Keyboard Listener"""
        if key == 115 and self.mover != "UP":
            self.mover = "DOWN"
        elif key == 119 and self.mover != "DOWN":
            self.mover = "UP"
        elif key == 97 and self.mover != "RIGHT":
            self.mover = "LEFT"
        elif key == 100 and self.mover != "LEFT":
            self.mover = "RIGHT"
        elif key == 112:
            self.pauseGame = False if self.pauseGame else True
            if self.pauseGame is False:
                self.run()
        elif key == 113:
            self.gameOver = True

    def all_variable(self):
        """All Variable"""
        self.mover = "STOP"
        self.score = 0
        self.gameOver = False
        self.pauseGame = False
        self.player = Snake()
        self.food = Food()
        self.all_tail = list()
        self.block_size = Window.width/WIDTH, Window.height/HEIGHT

    def display_field(self):
        """Display Field"""
        self.add_widget(self.player)
        self.score_label = GameLabel()
        self.score_label.text = f"Score: {self.score}"
        self.score_label.pos = (self.center_x-(self.score_label.width/2),
                                Window.height-self.score_label.height)
        self.add_widget(self.score_label)
        self.add_widget(self.food)
        self.add_tail(gc("55FF55"))

    def run_game(self):
        """Run The Game"""
        if self.gameOver or self.pauseGame:
            return False
        self.move_snake()
        self.game_logic()
        self.update_labels()

    def move_snake(self):
        """Move Snake"""
        self.prev_pos = self.player.pos
        if self.mover == "UP":
            self.player.y += self.block_size[1]
            if self.player.y >= Window.height:
                self.player.y = 0
        elif self.mover == "DOWN":
            self.player.y -= self.block_size[1]
            if self.player.y < 0:
                self.player.y = Window.height-self.block_size[1]
        elif self.mover == "LEFT":
            self.player.x -= self.block_size[0]
            if self.player.x < 0:
                self.player.x = Window.width-self.block_size[0]
        elif self.mover == "RIGHT":
            self.player.x += self.block_size[0]
            if self.player.x >= Window.width:
                self.player.x = 0
        for tail in self.all_tail:
            prev_pos2 = tail.x, tail.y
            tail.x, tail.y = self.prev_pos
            self.prev_pos = prev_pos2
            if self.player.pos == tail.pos and tail != self.all_tail[0]:
                tail.color = gc("FF1111")
                self.gameOver = True
                break

    def add_tail(self, color=gc("55AA55")):
        """Add Tail"""
        self.all_tail.append(SnakeTail(*self.player.pos, color))
        self.add_widget(self.all_tail[len(self.all_tail)-1])

    def update_labels(self):
        """Update All Label"""
        self.score_label.text = f"Score: {self.score}"

    def game_logic(self):
        """Logic"""
        self.check_if_eat()

    def check_if_eat(self):
        """Check if Snake eat Apple"""
        if self.player.pos == self.food.pos:
            self.score += 10
            self.remove_widget(self.food)
            self.food = Food()
            self.add_widget(self.food)
            self.add_tail()
