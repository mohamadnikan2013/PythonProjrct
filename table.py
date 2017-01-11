import turtle


class File:
    def __init__(self, fileName):
        self._fileName = fileName
        self.data = [line.split() for line in open(fileName)]
        self.data.pop(-1)
        self.up = self.data[0][1:6]
        self.down = self.data[6][1:6]
        self.left = self.column(1)[1:6]
        self.right = self.column(6)[1:6]
        self.table = self.gettable()
        print("hello world")

    def column(self, i):
        return [row[i] for row in self.data[0:7]]

    def gettable(self):
        return [row[1:6] for row in self.data[1:6]]


class BoardUI:
    def __init__(self, file):
        self.x_coord = -250
        self.y_coord = 300
        self.side = 80
        self.file = file
        self.draw_board()
        self.draw_down_condition()
        self.draw_up_condition()
        self.draw_left_condition()
        self.draw_right_condition()

    def draw_board(self):
        myxcoord = self.x_coord
        myycoord = self.y_coord
        my_pen = turtle.Turtle()
        my_pen.speed('fastest')
        my_pen.hideturtle()
        my_pen.pensize(3)
        dimension = 5

        for i in range(dimension ** 2):
            if i % dimension == 0:
                myycoord -= self.side
                my_pen.penup()
                my_pen.setpos(myxcoord, myycoord)
                my_pen.pendown()

            for _ in range(4):
                my_pen.forward(self.side)
                my_pen.right(90)

            my_pen.forward(self.side)
        dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z']
        lalist = []
        for i in range(1, 6):
            for j in range(5):
                lalist.append([self.x_coord + (j * self.side), self.y_coord - (self.side * i)])
        my_pen.penup()
        index = 0
        for i in lalist:
            my_pen.goto(i[0] + 4, i[1] - 19)
            my_pen.write(dic[index])
            index += 1

    def draw_up_condition(self):
        my_pen = turtle.Turtle()
        my_pen.speed('fastest')
        my_pen.hideturtle()
        my_pen.pensize(3)
        my_pen.penup()
        my_pen.goto(self.x_coord + 40, self.y_coord - 70)
        for i in self.file.up:
            if i != '0':
                my_pen.write(i)
            my_pen.forward(self.side)

    def draw_down_condition(self):
        my_pen = turtle.Turtle()
        my_pen.speed('fastest')
        my_pen.hideturtle()
        my_pen.pensize(3)
        my_pen.penup()
        my_pen.goto(self.x_coord + 40, self.y_coord - 500)
        for i in self.file.down:
            if i != '0':
                my_pen.write(i)
            my_pen.forward(self.side)

    def draw_left_condition(self):
        my_pen = turtle.Turtle()
        my_pen.speed('fastest')
        my_pen.hideturtle()
        my_pen.pensize(3)
        my_pen.penup()
        my_pen.goto(self.x_coord - 15, self.y_coord - 120)
        my_pen.right(90)
        for i in self.file.left:
            if i != '0':
                my_pen.write(i)
            my_pen.forward(self.side)

    def draw_right_condition(self):
        my_pen = turtle.Turtle()
        my_pen.speed('fastest')
        my_pen.hideturtle()
        my_pen.pensize(3)
        my_pen.penup()
        my_pen.goto(self.x_coord + 420, self.y_coord - 120)
        my_pen.right(90)
        for i in self.file.right:
            if i != '0':
                my_pen.write(i)
            my_pen.forward(self.side)


class Grid:
    def __init__(self, x, y, name, is_initialized=False, val=0):
        self.is_initialized = is_initialized
        self.val = val
        self.y = y
        self.x = x
        self.name = name
        if self.is_initialized:
            self.write(self.val)

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


class BoardLogic:
    def __init__(self, file):
        self.x_coord = -250
        self.y_coord = 300
        self.side = 80
        dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z']
        lalist = []
        for i in range(1, 6):
            for j in range(5):
                lalist.append([self.x_coord + (j * self.side), self.y_coord - (self.side * i)])

        index = 0
        self.grids = []
        for i in lalist:
            g = Grid(x=i[0], y=i[1], name=dic[index])
        self.grids.append(g)
        index += 1

    def solve(self):
        pass

    def check(self):
        pass


if __name__ == '__main__':
    ff = File("static/e1.txt")
    Ui = BoardUI(ff)
    logic = BoardLogic(ff)
    turtle.exitonclick()
