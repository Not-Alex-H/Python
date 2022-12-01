### graphing with turtle |||| do not run on battery! ###

import turtle
import time
import random
import os
def printGraph(height, val):
    graph = turtle.Turtle()
    turtle.tracer(0, 0)
    graph.goto(-600,-275)
    graph.clear
    turtle.screensize(1000, 500)
    for x in range(100000000000):
        graph.goto(-600,-275)
        val.append(random.randint(1, 10))
        if len(val) > 50:
            pass
        for i in range(len(val)):
            graph.pendown()
            graph.speed(0)
            graphX = -600 + i * 1100 / len(val) 
            graphY = -275 + val[i] * height
            graph.goto(graphX + 10, graphY)
            turtle.update()
        graph.speed(5000000)
        graph.penup()
        os.system('cls')
        graph.clear()
        print(val)
printGraph(50, [0])