### Physics? ###
import turtle
import time
hitboxes = []
shot = 0
def hitboxes(x1, x2, y1, y2):
    return True if shot.xcor() > x1 and shot.xcor() < x2 and shot.ycor() < y1 and shot.ycor() > y2 else False
def collision():
    return True if hitboxes(-600, 600, -115, -200) or hitboxes(-550, -500, 0, -100) else False
def setup():
    target = turtle.Turtle()
    floor = turtle.Turtle()
    floor.speed(0)
    floor.penup()
    floor.goto(-600, -115)
    floor.pendown()
    floor.clear()
    floor.forward(1200)
    target.penup()
    target.goto(-500, 0)
    target.pendown()
    target.goto(-500, -100)
def arrow(pow, ang):
    global shot
    drag = 0
    grav = 0
    shot_in_air = True
    turtle.screensize(1200, 250)
    shot = turtle.Turtle()
    shot.hideturtle()
    shot.penup()
    shot.speed(0)
    shot.goto(600, -100)
    shot.clear()
    shot.pendown()
    shot.speed(0)
    shot.showturtle()
    while shot_in_air == True:
        shot.goto(shot.xcor() - (pow - drag), shot.ycor() + (ang - grav))
        grav += 2
        drag += 0.5 if drag < pow else 0
        shot_in_air = False if shot.xcor() < -800 or collision() else True
    turtle.delay(7000)
    shot.write("nice")
setup()
time.sleep(1)
arrow(44, 30)