import turtle
wn = turtle.Screen()
t=turtle.Turtle()
for i in range(15):
    wn.bgcolor('light green')
    t.shape('circle')
    t.shape('triangle')
    t.forward(10)
    t.right(90)
    t.penup()
    t.color('red')
    t.pendown()
    t.shape('triangle')
    wn.title("Turtle")
    skk = turtle.Turtle()