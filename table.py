import turtle

import sys


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

    def column(self, i):
        return [row[i] for row in self.data[0:7]]

    def gettable(self):
        return [row[1:6] for row in self.data[1:6]]


class BoardUI:
    my_pen = turtle.Turtle()

    def __init__(self, file):
        self.x_coord = -250
        self.y_coord = 300
        self.side = 80
        self.file = file
        self.my_pen.speed('fastest')
        self.my_pen.hideturtle()
        self.my_pen.pensize(3)
        self.draw_board()
        self.draw_down_condition()
        self.draw_up_condition()
        self.draw_left_condition()
        self.draw_right_condition()

    def close(self):
        self.my_pen.clear()
        self.my_pen.reset()
        Grid.close()

    def draw_board(self):
        myxcoord = self.x_coord
        myycoord = self.y_coord
        dimension = 5

        for i in range(dimension ** 2):
            if i % dimension == 0:
                myycoord -= self.side
                self.my_pen.penup()
                self.my_pen.setpos(myxcoord, myycoord)
                self.my_pen.pendown()

            for _ in range(4):
                self.my_pen.forward(self.side)
                self.my_pen.right(90)

            self.my_pen.forward(self.side)
        dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z']
        lalist = []
        for i in range(1, 6):
            for j in range(5):
                lalist.append([self.x_coord + (j * self.side), self.y_coord - (self.side * i)])
        self.my_pen.penup()
        index = 0
        for i in lalist:
            self.my_pen.goto(i[0] + 4, i[1] - 19)
            self.my_pen.write(dic[index])
            index += 1

    def draw_up_condition(self):
        self.my_pen.goto(self.x_coord + 40, self.y_coord - 70)
        for i in self.file.up:
            if i != '0':
                self.my_pen.write(i)
            self.my_pen.forward(self.side)

    def draw_down_condition(self):
        self.my_pen.goto(self.x_coord + 40, self.y_coord - 500)
        for i in self.file.down:
            if i != '0':
                self.my_pen.write(i)
            self.my_pen.forward(self.side)

    def draw_left_condition(self):
        self.my_pen.goto(self.x_coord - 15, self.y_coord - 120)
        self.my_pen.right(90)
        for i in self.file.left:
            if i != '0':
                self.my_pen.write(i)
            self.my_pen.forward(self.side)
        self.my_pen.right(-90)

    def draw_right_condition(self):
        self.my_pen.goto(self.x_coord + 420, self.y_coord - 120)
        self.my_pen.right(90)
        for i in self.file.right:
            if i != '0':
                self.my_pen.write(i)
            self.my_pen.forward(self.side)
        self.my_pen.right(-90)


class Grid:
    my_pen = turtle.Turtle()

    def __init__(self, x, y, name, val=0):
        self.y = y
        self.x = x
        self.name = name
        self.is_initialized = False
        self.val = 0
        self.real = str(abs(int(val)))
        self.my_pen.speed('fastest')
        self.my_pen.hideturtle()
        self.my_pen.pensize(3)
        self.my_pen.penup()
        if int(val) < 0:
            self.val = str(abs(int(val)))
            self.write(self.val)
            self.is_initialized = True

    @staticmethod
    def close():
        Grid.my_pen.clear()
        Grid.my_pen.reset()

    def write(self, new_val, ok=False):
        if self.is_initialized and not ok:
            print("you cant Do this :D ")
            return
        if self.val != '0':
            self.erase()
        self.val = new_val
        if new_val != '0':
            self.my_pen.goto(self.x + 45, self.y - 45)
            self.my_pen.write(new_val)

    def erase(self):
        self.my_pen.color("white")
        self.my_pen.goto(self.x + 45, self.y - 45)
        self.my_pen.write(self.val)
        self.my_pen.color("black")


class BoardLogic:
    def __init__(self, file):
        self.x_coord = -250
        self.y_coord = 300
        self.side = 80
        self.file = file
        self.dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v',
                    'w', 'x', 'y', 'z']
        lalist = []
        for i in range(1, 6):
            for j in range(5):
                lalist.append([self.x_coord + (j * self.side), self.y_coord - (self.side * i)])

        index = 0
        self.grids = []
        for i in lalist:
            value = file.table[int(index / 5)][index % 5]
            g = Grid(x=i[0], y=i[1], name=self.dic[index], val=value)
            self.grids.append(g)
            index += 1

    def show(self):
        for h in self.grids:
            h.write(h.real, True)

    # TODO complete

    def check(self):
        for g in self.grids:
            if g.real != g.val:
                return False
        return True

    def command(self, cmd):
        idx = self.dic.index(cmd[0])
        val = int(cmd[1])
        if val == 0:
            self.grids[idx].erase()
        else:
            self.grids[idx].write(str(val))


if __name__ == '__main__':
    while True:
        while True:
            filename = str(input("Please enter fine name :D \n"))
            try:
                file = File(fileName=filename)
            except ValueError:
                print("input is not correct ")
                continue
            except FileNotFoundError:
                print("File not exist try again")
                continue
            break
        Ui = BoardUI(file)
        logic = BoardLogic(file)
        while True:
            cmd = str(input("please enter your command :D \n"))
            if cmd == "‫‪quit‬‬":
                sys.exit()
            elif cmd == "new":
                Ui.close()
                break
            elif cmd == "show":
                Ui.close()
                Ui = BoardUI(file)
                logic.show()
                cmd = str(input("are you want to play a new game yes/no ?"))
                if cmd == "yes":
                    Ui.close()
                    break
                else:
                    print("goodbye :D")
                    sys.exit()
            elif cmd == "check":
                res = logic.check()
                if not res:
                    print("‫‪not‬‬ ‫‪solved‬  :D ‬")
                    continue
                else:
                    print("solved")
                    cmd = str(input("are you want to play a new game yes/no ?"))
                    if cmd == "yes":
                        Ui.close()
                        break
                    else:
                        print("goodbye :D")
                        sys.exit()

            else:
                if len(cmd) > 2:
                    print("invalid input")
                    continue
                if ord(cmd[0]) < 97 or ord(cmd[0]) > 121 or int(cmd[1]) < 0 or int(cmd[1]) > 3:
                    print("invalid input")
                    continue
                logic.command(cmd)
