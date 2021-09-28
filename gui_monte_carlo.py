import random as rd
from tkinter import *
from turtle import RawTurtle as rt

class MyTurtle(rt):
    def __init__(self, screen):
        super(MyTurtle, self).__init__(screen)
        self.speed(0)
        self.pensize(1)
        self.penup()
        self.goto(-350, -350)

    def make_axis(self):
        self.goto(-360, -380)
        self.write(arg = "0", move = False, align = "center", font = ("", 20, ""))

        self.goto(-350, -350)
        self.pendown()
        self.forward(700)
        self.penup()

        self.goto(340, -380)
        self.write(arg = "10", move = False, align = "center", font = ("", 20, ""))

        self.goto(-350, -350)
        self.setheading(90)
        self.pendown()
        self.forward(700)
        self.penup()

        self.goto(-370, 330)
        self.write(arg = "10", move = False, align = "center", font = ("", 20, ""))
        self.goto(-350, -350)

    def draw_graph(self, equation):
        self.pencolor("red")
        self.pensize(3)

        #그래프를 그릴 초기 위치로 이동
        self.penup()
        unit = 70
        x = 0
        y = eval(equation)
        self.goto(-350 + unit*x, -350 + unit*y)
        self.pendown()

        #그래프 그리기
        for i in range(0, 701, 1):
            x = i/unit
            y = eval(equation)
            if y < 0:
                self.hideturtle()
                self.penup()
            elif y >= 0:
                self.showturtle()
                self.pendown()
            if y > 10:
                break
            self.goto(-350 + unit*x, -350 + unit*y)

        #원점으로 복귀
        self.penup()
        self.goto(-350, -350)

    def reset_graph(self):
        self.reset()
        self.speed(0)
        self.pensize(1)
        self.penup()
        self.goto(-350, -350)
        self.make_axis()

    def show_range(self, range_initial, range_final, equation):
        self.pencolor("black")
        self.pensize(2)
        unit = 70

        #시작범위의 함숫값으로 이동
        x = range_initial
        y = eval(equation)
        self.goto(-350 + unit*x, -350 + unit*y)

        #x축까지 점선그리고 x축 좌표적기
        for i in range(unit*y):
            if (i%10 == 0) or (i%10 == 1) or (i%10 == 2) or (i%10 == 3) or (i%10 == 4):
                self.pendown()
            else:
                self.penup()
            self.backward(1)

        self.penup()
        self.goto(-350 + unit*x, -380)
        self.write(arg = str(range_initial), move = False, align = "center", font = ("", 20, ""))

        #끝 범위의 함숫값으로 이동
        x = range_final
        y = eval(equation)
        self.goto(-350 + unit*x, -350 + unit*y)

        #x축까지 점선그리고 x축 좌표적기
        for i in range(unit*y):
            if (i%10 == 0) or (i%10 == 1) or (i%10 == 2) or (i%10 == 3) or (i%10 == 4):
                self.pendown()
            else:
                self.penup()
            self.backward(1)

        self.penup()
        self.goto(-350 + unit*x, -380)
        self.write(arg = str(range_final), move = False, align = "center", font = ("", 20, ""))

        #원점이동
        self.goto(-350, -350)

    def calc_monte_carlo(self, range_initial, range_final, equation, random_num):
        unit = 70
        count_under = 0
        count_above = 0

        self.pencolor("blue")
        self.penup()

        x = range_final
        y = eval(equation)
        rectangle_size = (range_final-range_initial)*y

        for i in range(random_num):
            rand_x = rd.randint(range_initial, range_final-1) + rd.random()
            rand_y = rd.randint(0, y-1) + rd.random()
            self.goto(-350 + unit*rand_x, -350 + unit*rand_y)
            self.dot(4)

            x = rand_x
            y_value = eval(equation)

            if rand_y <= y_value:
                count_under += 1
            else:
                count_above += 1


        area = count_under/random_num * rectangle_size
        self.pencolor("black")
        self.goto(0, 350)
        self.write(arg = "Result({0} times)\nunder dot: {1}\nupper dot: {2}\nrectangle size: {3}\narea: {4}/{5} * {6} = {7}".format(random_num, count_under, count_above, rectangle_size, count_under, random_num, rectangle_size, area ), move = False, align = "center", font = ("", 12, "normal"))





window = Tk()

#스크린
screen = Canvas(master = window, width = 900, height = 900)
screen.grid(row = 0, column = 0)

t = MyTurtle(screen)

frame = Frame(master=window, padx=20)
frame.grid(row=1, column=0)

#프레임 위
frame_up = Frame(master = frame, padx = 20)
frame_up.grid(row = 0, column = 0)
label_up = Label(master = frame_up, text = "monte carlo method visualization")
label_up.grid(row = 0, column = 0)

################################################################################################
#프레임 중앙
frame_center = Frame(master = frame)
frame_center.grid(row = 1, column = 0)
label_center = Label(master = frame_center, text = "frame_center")
label_center.grid(row = 0, column = 0)

#프레임 중앙 왼쪽
frame_center_left = Frame(master = frame_center)
frame_center_left.grid(row = 0, column = 0)
label_center_left = Label(master = frame_center_left, text = "frame_center_left")
label_center_left.grid(row = 0, column = 0)

#프레임 중앙 왼쪽 위
label_equation = Label(master = frame_center_left, text = "1.python 표현식을 입력하세요 ex) x**2+1")
label_equation.grid(row = 0, column = 0)

#프레임 중앙 왼쪽 아래
entry_equation = Entry(master = frame_center_left)
entry_equation.grid(row = 1, column = 0)

#프레임 중앙 오른쪽
frame_center_right = Frame(master = frame_center)
frame_center_right.grid(row = 0, column = 1)
label_center_right = Label(master = frame_center_right, text = "frame_center_right")
label_center_right.grid(row = 0, column = 0)

#프레임 중앙 오른쪽 위
frame_center_right_up = Frame(master = frame_center_right)
frame_center_right_up.grid(row = 0, column = 0)
label_center_right_up = Label(master = frame_center_right_up, text = "2.monte carlo 변수를 해당 칸에 작성하세요(정수입력 필)")
label_center_right_up.grid(row = 0, column = 0)

#프레임 중앙 오른쪽 아래
frame_center_right_down = Frame(master = frame_center_right)
frame_center_right_down.grid(row = 1, column = 0)

#프레임 중앙 오른쪽 아래의 범위와 난수개수
Label(master = frame_center_right_down, text = "범위:").grid(row = 0, column =0)

entry_initial = Entry(master = frame_center_right_down)
entry_initial.grid(row = 0, column = 1)

Label(master = frame_center_right_down, text = "~").grid(row = 0, column =2)

entry_final = Entry(master = frame_center_right_down)
entry_final.grid(row = 0, column = 3)

Label(master = frame_center_right_down, text = ", 난수 개수:").grid(row = 0, column =4)

entry_random = Entry(master = frame_center_right_down)
entry_random.grid(row = 0, column = 5)


###############################################################################################
#프레임 아래
frame_down = Frame(master = frame, padx = 20)
frame_down.grid(row = 2, column = 0)
label_down = Label(master = frame_down, text = "frame_down")
label_down.grid(row = 0, column = 0)

#프레임 아래 버튼들

button_make_axis = Button(master = frame_down, text = "좌표 평면 생성", command = t.make_axis)
button_make_axis.grid(row = 0, column = 0)

button_draw_graph = Button(master = frame_down, text = "그래프 그리기", command = lambda: t.draw_graph(entry_equation.get()))
button_draw_graph.grid(row = 0, column = 1)

button_reset_graph = Button(master = frame_down, text = "그래프 초기화", command = t.reset_graph)
button_reset_graph.grid(row = 0, column = 2)

button_show_range = Button(master = frame_down, text = "몬테 카를로 범위 표시", command = lambda: t.show_range(int(entry_initial.get()), int(entry_final.get()), entry_equation.get()))
button_show_range.grid(row = 0, column = 3)

button_calc_monte_carlo = Button(master = frame_down, text = "몬테카를로 계산", command = lambda: t.calc_monte_carlo(int(entry_initial.get()), int(entry_final.get()), entry_equation.get(), int(entry_random.get())))
button_calc_monte_carlo.grid(row = 0, column = 4)

window.mainloop()