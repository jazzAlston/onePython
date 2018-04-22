import turtle

def draw_Square(some_turtle):
    numSides = 4
    length = 100

    while(numSides > 0): 
      some_turtle.forward(length)
      some_turtle.right(90)
   
      numSides = numSides - 1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    rick = turtle.Turtle()
    rick.shape("turtle")
    rick.color("red")
    rick.speed(2)
    for i in  range(1,37):
      draw_Square(rick)
      rick.right(10)

    window.exitonclick()

draw_art()
