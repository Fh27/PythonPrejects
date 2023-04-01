import turtle
t=turtle.Turtle()
t.screen.bgcolor("black")
t.pensize(3) 
t.color("brown")
t.left(90)
t.backward(100)
t.speed(30)
t.shape("arrow")


def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color("green")
        t.speed(30)
        t.circle(3)
        t.color("#9c4a1a") 
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)

tree(100)
turtle()            
