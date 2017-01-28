import turtle

import sys

turtle.title('123 Game UI')


# this class open file and  read data
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

    # Fetch data for column
    def column(self, i):
        return [row[i] for row in self.data[0:7]]

    # Fetch table from input
    def gettable(self):
        return [row[1:6] for row in self.data[1:6]]


# this class for Static  UI that get the data from file and generateThe Ui
class BoardUI:
    my_pen = turtle.Turtle()

    def __init__(self, myfile):
        self.x_coord = -250
        self.y_coord = 300
        self.side = 80
        self.file = myfile
        self.my_pen.speed('fastest')
        self.my_pen.hideturtle()
        self.my_pen.pensize(3)
        self.draw_board()
        self.my_pen.color("green")
        self.draw_down_condition()
        self.draw_up_condition()
        self.draw_left_condition()
        self.draw_right_condition()
        self.my_pen.color("black")

    # close The Ui
    def close(self):
        self.my_pen.clear()
        # self.my_pen.reset()
        Grid.close()

    # Draw The Board with custom dimension
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
            self.my_pen.goto(i[0] + 7, i[1] - 23)
            self.my_pen.write(dic[index], font=("Arial", 16, "normal"))
            index += 1

    # draw upper condition
    def draw_up_condition(self):
        self.my_pen.goto(self.x_coord + 40, self.y_coord - 70)
        for i in self.file.up:
            if i != '0':
                self.my_pen.write(i, font=("Arial", 16, "normal"))
            self.my_pen.forward(self.side)

    # draw down condition
    def draw_down_condition(self):
        self.my_pen.goto(self.x_coord + 40, self.y_coord - 510)
        for i in self.file.down:
            if i != '0':
                self.my_pen.write(i, font=("Arial", 16, "normal"))
            self.my_pen.forward(self.side)

    # draw left condition
    def draw_left_condition(self):
        self.my_pen.goto(self.x_coord - 15, self.y_coord - 120)
        self.my_pen.right(90)
        for i in self.file.left:
            if i != '0':
                self.my_pen.write(i, font=("Arial", 16, "normal"))
            self.my_pen.forward(self.side)
        self.my_pen.right(-90)

    # draw right condition
    def draw_right_condition(self):
        self.my_pen.goto(self.x_coord + 420, self.y_coord - 120)
        self.my_pen.right(90)
        for i in self.file.right:
            if i != '0':
                self.my_pen.write(i, font=("Arial", 16, "normal"))
            self.my_pen.forward(self.side)
        self.my_pen.right(-90)


# this class Draw data input with user in to the Ui
class Grid:
    my_pen = turtle.Turtle()

    def __init__(self, x, y, name, val=0):
        self.y = y
        self.x = x
        self.name = name
        self.is_initialized = False
        self.val = '0'
        self.real = str(abs(int(val)))
        self.my_pen.speed('fastest')
        self.my_pen.hideturtle()
        self.my_pen.pensize(3)
        self.my_pen.penup()
        if int(val) < 0:
            self.val = str(abs(int(val)))
            self.write(self.val, True)
            self.is_initialized = True

    # close the UI
    @staticmethod
    def close():
        Grid.my_pen.clear()
        # Grid.my_pen.reset()

    # write data input into the UI
    def write(self, new_val, ok=False):
        if self.is_initialized and not ok:
            print("you cant Do this :D ")
            return
        if self.val != '0':
            self.erase()
        self.val = new_val
        if ok:
            self.my_pen.color("red")
        if new_val != '0':
            self.my_pen.goto(self.x + 45, self.y - 45)
            self.my_pen.write(new_val, font=("Arial", 16, "normal"))
        self.my_pen.color("black")

    # erase data from UI
    def erase(self):
        if self.is_initialized:
            print("you cant Do this :D ")
            return
        self.my_pen.color("white")
        self.my_pen.goto(self.x + 45, self.y - 45)
        self.my_pen.write(self.val, font=("Arial", 16, "normal"))
        self.my_pen.color("black")


# this is main class that handle our logic
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

    # show the solved Board
    def show(self):
        for h in self.grids:
            h.write(h.real, True)

    # chack if we win
    def check(self):
        for g in self.grids:
            if g.real != g.val:
                return False
        return True

    # do our command to input the board
    def command(self, cmd):
        idx = self.dic.index(cmd[0])
        val = int(cmd[1])
        if val == 0:
            self.grids[idx].erase()
        else:
            self.grids[idx].write(str(val))


# this is our main that get our input and use upeer class and method to do our command
if __name__ == '__main__':
    while True:
        while True:
            # get file name
            filename = str(input("Please enter file name :D \n"))
            try:
                file = File(fileName=filename)
            except ValueError:
                print("input is not correct ")
                continue
            except FileNotFoundError:
                print("File not exist try again")
                continue
            break
        # initial Board
        Ui = BoardUI(file)
        logic = BoardLogic(file)
        # get user command and check if valid use appropriate class method to do it
        while True:
            cmd = str(input("please enter your command :D \n"))
            if cmd == "quit":
                print("Good Bye :D ;D ")
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
                if len(cmd) != 2:
                    print("invalid input")
                    continue
                if ord(cmd[0]) < 97 or ord(cmd[0]) > 121 or ord(cmd[1]) < 48 or ord(cmd[1]) > 51:
                    print("invalid input")
                    continue
                logic.command(cmd)
