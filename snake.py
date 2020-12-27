from tkinter import *
import random

# Win geometry
win = Tk()
win.title('Snake')
win['bg'] = '#3caa3c'
rand_coordx = [5, 25, 45, 65, 85, 105, 125, 145, 165, 185, 205, 225, 245, 265, 285, 305, 325, 345, 365, 385]
rand_coordy = [5, 25, 45, 65, 85, 105, 125, 145, 165, 185]
win.resizable(width=False, height=False)
# win.iconbitmap('icons8_tetris.ico')
win.geometry('600x400')
k = 20
dx = 20
dy = 0
# game place
gm = Canvas(win, bg='#3caa3c', width=600, height=400)
for i in range(k, 30 * k, k):
    gm.create_line(i, 0, i, 20 * k, fill='#3caa3c')
for i in range(k, 20 * k, k):
    gm.create_line(0, i, 30 * k, i, fill='#3caa3c')

# Food

a = random.choice(rand_coordx)
b = random.choice(rand_coordy)
food = gm.create_rectangle(a, b, a + 10, b + 10, fill='red')

# Snake

head_snake = gm.create_rectangle(80, 100, 100, 80, fill='yellow')


def down(event):
    global dx
    global dy
    dy = 20
    dx = 0


def up(event):
    global dx
    global dy
    dy = -20
    dx = 0


def left(event):
    global dx
    global dy
    dy = 0
    dx = -20


def right(event):
    global dx
    global dy
    dy = 0
    dx = 20


def motion():
    global dx
    global dy
    global go
    go = TRUE
    if gm.coords(head_snake)[2] > 600:
        gm.coords(head_snake, 0, gm.coords(head_snake)[1], 20, gm.coords(head_snake)[3])
    if gm.coords(head_snake)[0] < 0:
        gm.coords(head_snake, 580, gm.coords(head_snake)[1], 600, gm.coords(head_snake)[3])
    if gm.coords(head_snake)[3] > 400:
        gm.coords(head_snake, gm.coords(head_snake)[0], 0, gm.coords(head_snake)[2], 20)
    if gm.coords(head_snake)[1] < 0:
        gm.coords(head_snake, gm.coords(head_snake)[0], 380, gm.coords(head_snake)[2], 400)
    if ((gm.coords(head_snake)[0] + 5) == (gm.coords(food)[0])) and ((gm.coords(head_snake)[1] + 5) == (gm.coords(food)[1])):
        a = random.choice(rand_coordx)
        b = random.choice(rand_coordy)
        gm.coords(food, a, b, a + 10, b + 10)
    gm.pack()
    gm.move(head_snake, dx, dy)
    if go:
        win.after(100, motion)

score = gm.create_text(50,30, text='Score: 0', font='Arial 15')
gm.pack()
gm.bind('<Down>', down)
gm.bind('<Up>', up)
gm.bind('<Left>', left)
gm.bind('<Right>', right)
gm.focus_set()
motion()

win.mainloop()
