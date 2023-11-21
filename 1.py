from kivy.metrics import sp
from kivy.core.window import Window
from kivy.app import App
from kivy.clock import Clock
from kivy import properties as kp
from kivy.uix.widget import Widget
from collections import defaultdict

SPRITE_SIZE = sp(20)
COLS = int(Window.width / SPRITE_SIZE)
ROWS = int(Window.height / SPRITE_SIZE)

LENGHT = 4
MOVESPEED = .1

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

direction_values = {LEFT: [-1, 0],
                    RIGHT: [1, 0],
                    UP: [0, 1],
                    DOWN: [0, -1]

                    }

class Sprite(Widget):
    coord = kp.ListProperty([0,0])
    bgcolor = kp.ListProperty([0,0,0,0])


SPRITES = defaultdict(lambda:Sprite())



class Snake(App):
    head = kp.ListProperty([0,0])
    fruit = kp.ListProperty([0,0])
    snake = kp.ListProperty()


direction = kp.StringProperty(RIGHT,options=(LEFT,UP,RIGHT,DOWN))


def on_start(self):
    Clock.schedule_interval(self.move, MOVESPEED)

def on_head(self, *args):
    self.snake = self.snake[-self.lenght:] + [self.head]

def on_snake(self, *args):
    for index, coord in enumerate(self.snake):
        sprite = SPRITES[index]
        sprite_coord = coord
        if not sprite.parent:
            self.root.add.widget(sprite)

def move(self, *args):
    new_head = [sum(x) for x in zip(self.head, direction_values[self.direction])]

    self.head = new_head


if __name__ == "__main__":
    Snake().run()
