import time
from tkinter import *
from tracemalloc import start
from Dot import *
from Population import *
from Obstacles import *

def drawGoal(canvas):
    goalRadius = 5
    canvas.create_oval(GOAL[0]-goalRadius, GOAL[1]-goalRadius, GOAL[0]+goalRadius, GOAL[1]+goalRadius, fill='red')

def resetCanvas(canvas, window):
    canvas.delete('all')
    drawGoal(canvas)
    Obstacles.drawObstacles(canvas=canvas)
    window.update()

window = Tk()
window.title('dots')
WIDTH = 500
HEIGHT = 500
START = [250, 460]
GOAL = [250, 50]

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack(padx=10, pady=10)
pop = Population(WIDTH, HEIGHT, canvas, 200, START, GOAL)
resetCanvas(canvas, window)
while pop.generation < 40:
    if(pop.populationDead()):
        resetCanvas(canvas, window)
        pop.calculateFitness()
        pop.naturalSelection()
        pop.mutateBabies()
    else:
        pop.update()
        pop.show()
        window.update()
        time.sleep(0.01)


window.mainloop()

