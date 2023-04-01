import turtle

pen = turtle. Turtle()

def curve():
 for i in range (200):
  pen.right(1)
  pen. forward (1)
  pen.speed(80)

def heart():

 pen.fillcolor('red')
 pen.begin_fill()
 pen.speed(80)
 pen. left(140)
 pen. forward(113)

 curve()
 pen. left(120)

 curve()

 pen. forward(112)

 pen.end_fill()

def txt():

 pen.up()
 pen.setpos(-68, 95)

 pen.down()
 pen.color('black')
 pen.write("BESTIE " ,font=("verdena", 12,"bold"))

heart()
txt()
pen.ht()