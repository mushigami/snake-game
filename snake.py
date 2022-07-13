from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.make()
        self.head = self.snakes[0]
        self.last_heading = RIGHT

    def make(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def add_segment(self, position):
        new_snake_body = Turtle(shape="square")
        new_snake_body.color("white")
        new_snake_body.penup()
        new_snake_body.goto(position)
        self.snakes.append(new_snake_body)

    def move(self):
        """A method that moves the snake from end to front"""
        for body_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[body_num - 1].xcor()
            new_y = self.snakes[body_num - 1].ycor()
            self.snakes[body_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)
        self.last_heading = self.head.heading()

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.make()
        self.head = self.snakes[0]

    def left(self):
        if self.last_heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.last_heading != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.last_heading != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.last_heading != UP:
            self.head.setheading(270)
