from tkinter import *
from tkinter import ttk
import tkinter as tk
import turtle
import random

def UnitCircleInformation():


    t.reset()
    t.penup()
    t.ht()

    t.goto(0,90)
    t.write("The unit circle is a tool used in trigonometry to help students", align= "center", font= "20")
    t.goto(0,60)
    t.write("remember special angles and the trigonometric functions.", align= "center", font= "20")
    t.goto(0,30)
    t.write(" The center of the unit circle is at the origin (0,0).", align= "center", font= "20")
    t.goto(0,0)
    t.write("The radius of the unit circle is 1.", align= "center", font= "20")
    t.goto(0,-30)
    t.write("The special angles that appear on the unit circle is the 30-60-90", align= "center", font= "20")
    t.goto(0,-60)
    t.write("triangle and the isosceles right triangle.", align= "center", font= "20")



def UnitCircle():


    t.reset()
    t.pendown()
    t.clear()

    for i in range(1):

        t.speed(0)
        t.dot(2)

        t.penup()
        t.width(2)
        t.goto(0,-300)
        t.pendown()
        t.circle(300)

        t.fillcolor("blue")
        t.begin_fill()
        t.circle(300,180)
        t.end_fill()

        t.penup()
        t.goto(300,0)
        t.pendown()
        t.right(90)

        t.fillcolor("green")
        t.begin_fill()
        t.circle(300,180)
        t.end_fill()

        t.penup()
        t.goto(0,300)
        t.pendown()
        t.right(90)

        t.fillcolor("red")
        t.begin_fill()
        t.circle(300, 180)
        t.end_fill()


        t.penup()
        t.goto(-300, 0)
        t.pendown()

        t.fillcolor("yellow")
        t.begin_fill()

        t.right(90)
        t.circle(300, 90)

        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

        t.end_fill()

        for i in range(12):
            t.width(2)

            t.penup()
            t.goto(0, 0)
            t.pendown()

            t.left(30)
            t.forward(300)
            t.dot(10)

        t.right(45)

        for i in range(4):

            t.penup()
            t.goto(0, 0)
            t.pendown()

            t.right(90)
            t.forward(300)
            t.dot(10)

        t.right(45)

        for i in range(8):
            t.goto(0, 0)
            t.penup()

            t.width(4)
            t.right(90)
            t.forward(375)
            t.penup()

        t.right(90)
        t.width(1)
        t.goto(0,-330)
        t.write("3π/2 | (0,-1) | 270°", align = "center", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)

        t.pendown()
        t.circle(300,30)
        t.write("5π/3 | (1/2,-√3/2) | 300°", align = "left", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(30)

        t.pendown()
        t.circle(300,60)
        t.write("11π/6 | (√3/2,-1/2) | 330°", align = "left", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(60)

        t.pendown()
        t.circle(300,90)
        t.write("0π,2π | (1,0) | 0°,180°", align = "left", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(90)

        t.pendown()
        t.circle(300,120)
        t.write("π/6 | (√3/2,1/2) | 30°", align = "left", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(120)

        t.pendown()
        t.circle(300,150)
        t.write("π/3 | (1/2,√3/2) | 60°", align = "left", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(150)

        t.pendown()
        t.circle(300,180)
        t.write("π/2 | (0,1) | 90°", align = "center", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(180)

        t.pendown()
        t.circle(300,210)
        t.write("2π/3 | (-1/2,√3/2) | 120°", align = "right", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(210)

        t.pendown()
        t.circle(300,240)
        t.write("5π/6 | (-√3/2,1/2) | 150°", align = "right", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(240)

        t.pendown()
        t.circle(300,270)
        t.write("1π | (-1,0) | 180°", align = "right", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(270)

        t.pendown()
        t.circle(300,300)
        t.write("7π/6 | (-√3/2,-1/2) | 210°", align = "right", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(300)

        t.pendown()
        t.circle(300,330)
        t.write("4π/3 | (-1/2,-√3/2) | 240°", align = "right", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(330)

        t.pendown()
        t.circle(300,45)
        t.write("7π/4 | (√2/2,-√2/2) | 315°", align = "left", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(45)

        t.pendown()
        t.circle(300,135)
        t.write("π/4 | (√2/2,√2/2) | 45°", align = "left", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(135)

        t.pendown()
        t.circle(300,225)
        t.write("3π/4 | (-√2/2,√2/2) | 135°", align = "right", font = "Arial, 12")

        t.penup()
        t.goto(0,-300)
        t.right(225)

        t.pendown()
        t.circle(300,315)
        t.write("5π/4 | (-√2/2,-√2/2) | 225°", align = "right", font = "Arial, 12")


def MAINQUIZ():


    def QUIZ():
        def Quiz():
            global qE
            global roots
            global question

            roots = Tk()
            roots.title("Quiz")

            question = random.randint(1, 20)

            if question == 1:
                q = Label(roots, text="(0,1)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 2:
                q = Label(roots, text="(-√3/2 , 1/2)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 3:
                q = Label(roots, text="(√2/2 , √2/2)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 4:
                q = Label(roots, text="(√3/2 , 1/2)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 5:
                q = Label(roots, text="(-√2/2 , -√2/2)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 6:
                q = Label(roots, text="(0,-1)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 7:
                q = Label(roots, text="(1,0)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 8:
                q = Label(roots, text="(-1,0)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 9:
                q = Label(roots, text="(-1/2 , √3/2)")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 10:
                q = Label(roots, text="(1/2, -√3/2")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 11:
                q = Label(roots, text="2π/3")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 12:
                q = Label(roots, text="π/3")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 13:
                q = Label(roots, text="π/6")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 14:
                q = Label(roots, text="π")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 15:
                q = Label(roots, text="3π/2")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 16:
                q = Label(roots, text="0π")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 17:
                q = Label(roots, text="5π/4")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 18:
                q = Label(roots, text="11π/6")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 19:
                q = Label(roots, text="3π/4")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            if question == 20:
                q = Label(roots, text="π/2")
                q.grid(row=1, column=0, sticky=E)
                qE = Entry(roots)
                qE.grid(row=1, column=1)

                Answer = Button(roots, text='CHECK', command=Check)
                Answer.grid(columnspan=2)

            Next = Button(roots, text='CONTINUE', command=Redue)
            Exit = Button(roots, text='EXIT QUIZ', command=roots.destroy)

            Next.grid(columnspan=3)
            Exit.grid(columnspan=3)


            roots.geometry("300x200+0+0")
            roots.mainloop()

        def Check():
            global Q

            Q = qE.get()
            Q = int(Q)

            if question == 1 and Q is 90:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 1 and Q is not 90:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 2 and Q is 150:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 2 and Q is not 150:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 3 and Q is 45:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 3 and Q is not 45:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 4 and Q is 30:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 4 and Q is not 30:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 5 and Q is 225:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 5 and Q is not 225:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 6 and Q is 270:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 6 and Q is not 270:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 7 and Q is 0:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 7 and Q is not 0:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 8 and Q is 180:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 8 and Q is not 180:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 9 and Q is 120:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 9 and Q is not 120:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 10 and Q is 300:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 10 and Q is not 300:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 11 and Q is 120:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 11 and Q is not 120:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 12 and Q is 60:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 12 and Q is not 60:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 13 and Q is 30:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 13 and Q is not 30:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 14 and Q is 180:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 14 and Q is not 180:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 15 and Q is 270:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 15 and Q is not 270:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 16 and Q is 0:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 16 and Q is not 0:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 17 and Q is 225:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 17 and Q is not 225:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 18 and Q is 330:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 18 and Q is not 330:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 19 and Q is 135:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 19 and Q is not 135:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

            if question == 20 and Q is 90:
                answer = Label(roots, text="Correct", font="Arial 12 ", fg="green")
                answer.pack(side=BOTTOM)

            if question == 20 and Q is not 90:
                answer = Label(roots, text="Incorrect", font="Arial 12 ", fg="red")
                answer.pack(side=BOTTOM)

        def Redue():
            roots.destroy()
            Quiz()

        Quiz()

    def Window():
        global label

        roots = Tk()
        roots.title('Interactive Unit Circle Quiz')

        Description = Label(roots, text="Unit Circle Quiz", font="Arial 48 bold")
        Description1 = Label(roots, text="This is a quiz to test if you know the", font="Arial 24")
        Description2 = Label(roots, text="angle given the radians or the coordinate.", font="Arial 24")

        Start = Button(roots, text="Click Button to Begin", command=QUIZ)
        Exit = Button(roots, text="Exit Program", command=roots.destroy)

        Description.pack()
        Description1.pack()
        Description2.pack()
        Exit.pack(side=BOTTOM)
        Start.pack(side=BOTTOM)

        roots.geometry("500x200+0+0")
        roots.mainloop()

    Window()


roots = Tk()
roots.title("Unit Circle Program")
canvas = tk.Canvas(master = roots, width = 850, height = 780)
canvas.pack()
t = turtle.RawTurtle(canvas)

Label(roots, text="----------------------------------------------------------------------------Selections----------------------------------------------------------------------------").pack()
tk.Button(roots, text="Unit Circle Information", command=UnitCircleInformation).pack()
tk.Button(roots, text="Diagram", command=UnitCircle).pack()
tk.Button(roots, text="Unit Circle Quiz", command=MAINQUIZ).pack()
tk.Button(roots, text = "Exit", command =roots.destroy).pack()
roots.geometry("950x950+200+200")
roots.mainloop()