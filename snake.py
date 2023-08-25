from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            temp_square = Turtle("square")
            temp_square.color("white")
            temp_square.penup()
            temp_square.goto(position)
            self.body.append(temp_square)

    def add_body(self):
        temp_square = Turtle("square")
        temp_square.color("white")
        temp_square.penup()
        last_square = self.body[len(self.body) - 1]
        last_square_xcor = last_square.xcor()
        last_square_ycor = last_square.ycor()
        if last_square.heading() == RIGHT:
            last_square_xcor -= 20
            self.body.append(last_square)
        elif last_square.heading() == LEFT:
            last_square_xcor += 20
            self.body.append(last_square)
        elif last_square.heading() == UP:
            last_square_ycor += 20
            self.body.append(last_square)
        elif last_square.heading() == DOWN:
            last_square_ycor -= 20
            self.body.append(last_square)
        temp_square.goto(last_square_xcor, last_square_ycor)
        self.body.append(temp_square)

    def keep_going(self):
        for square_num in range(len(self.body) - 1, 0, -1):
            xcor = self.body[square_num - 1].xcor()
            ycor = self.body[square_num - 1].ycor()
            self.body[square_num].goto(xcor, ycor)
        self.body[0].forward(MOVE_DISTANCE)

    def left(self):
        heading = int(self.body[0].heading())
        if heading == UP or heading == DOWN:
            self.body[0].setheading(LEFT)

    def right(self):
        heading = int(self.body[0].heading())
        if heading == UP or heading == DOWN:
            self.body[0].setheading(RIGHT)

    def up(self):
        heading = int(self.body[0].heading())
        if heading == RIGHT or heading == LEFT:
            self.body[0].setheading(UP)

    def down(self):
        heading = int(self.body[0].heading())
        if heading == RIGHT or heading == LEFT:
            self.body[0].setheading(DOWN)

    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.body = []
        self.create_snake()


