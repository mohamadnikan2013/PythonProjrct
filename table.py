import turtle


class Board:
    pass


class Grid:
    def __init__(self, x, y, name, is_initialized=False, val=0):
        self.is_initialized = is_initialized
        self.val = val
        self.y = y
        self.x = x
        self.name = name

    def write(self, new_val):
        if self.is_initialized:
            pass
        self.erase()
        self.val = new_val
        if new_val != 0:
            my_pen = turtle.Turtle()
            my_pen.speed('fastest')
            my_pen.hideturtle()
            my_pen.pensize(3)
            my_pen.penup()
            my_pen.goto(self.x + 45, self.y - 45)
            my_pen.write(new_val)

    def erase(self):
        my_pen = turtle.Turtle()
        my_pen.speed('fastest')
        my_pen.hideturtle()
        my_pen.pensize(3)
        my_pen.penup()
        my_pen.color("white")
        my_pen.goto(self.x + 45, self.y - 45)
        my_pen.write(self.val)


def draw_board(x_coord=-250, y_coord=300, side=80):
    myxcoord = x_coord
    myycoord = y_coord
    my_pen = turtle.Turtle()
    my_pen.speed('fastest')
    my_pen.hideturtle()
    my_pen.pensize(3)
    dimension = 5

    for i in range(dimension ** 2):
        if i % dimension == 0:
            y_coord -= side
            my_pen.penup()
            my_pen.setpos(x_coord, y_coord)
            my_pen.pendown()

        for _ in range(4):
            my_pen.forward(side)
            my_pen.right(90)

        my_pen.forward(side)
    dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    lalist = []
    for i in range(1, 6):
        for j in range(5):
            lalist.append([myxcoord + (j * side), myycoord - (side * i)])
    my_pen.penup()
    index = 0
    for i in lalist:
        my_pen.goto(i[0] + 4, i[1] - 19)
        my_pen.write(dic[index])
        index += 1


def draw_up_condition(x, x_coord=-250, y_coord=300, side=80):
    my_pen = turtle.Turtle()
    my_pen.speed('fastest')
    my_pen.hideturtle()
    my_pen.pensize(3)
    my_pen.penup()
    my_pen.goto(x_coord + 40, y_coord - 70)
    for i in x:
        my_pen.write(i)
        my_pen.forward(side)


def draw_down_condition(x, x_coord=-250, y_coord=300, side=80):
    my_pen = turtle.Turtle()
    my_pen.speed('fastest')
    my_pen.hideturtle()
    my_pen.pensize(3)
    my_pen.penup()
    my_pen.goto(x_coord + 40, y_coord - 500)
    for i in x:
        my_pen.write(i)
        my_pen.forward(side)


def draw_left_condition(x, x_coord=-250, y_coord=300, side=80):
    my_pen = turtle.Turtle()
    my_pen.speed('fastest')
    my_pen.hideturtle()
    my_pen.pensize(3)
    my_pen.penup()
    my_pen.goto(x_coord - 15, y_coord - 120)
    my_pen.right(90)
    for i in x:
        my_pen.write(i)
        my_pen.forward(side)


def draw_right_condition(x, x_coord=-250, y_coord=300, side=80):
    my_pen = turtle.Turtle()
    my_pen.speed('fastest')
    my_pen.hideturtle()
    my_pen.pensize(3)
    my_pen.penup()
    my_pen.goto(x_coord + 420, y_coord - 120)
    my_pen.right(90)
    for i in x:
        my_pen.write(i)
        my_pen.forward(side)


def initial_board(x_coord=-250, y_coord=300, side=80):
    dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    lalist = []
    for i in range(1, 6):
        for j in range(5):
            lalist.append([x_coord + (j * side), y_coord - (side * i)])

    index = 0
    grids = []
    for i in lalist:
        g = Grid(x=i[0], y=i[1], name=dic[index])
        grids.append(g)
        index += 1
    return grids


def solve():
    pass


def check():
    pass


if __name__ == '__main__':
    draw_board()
    TT = initial_board()

    turtle.exitonclick()
