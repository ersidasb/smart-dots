from asyncio.windows_events import NULL
from Brain import *
from Obstacles import *

DOT_RADIUS = 3

class Dot():
    def __init__(self, width, height, canvas, start, goal, brainSize):
        self.brain = Brain(brainSize)

        self.pos = [start[0], start[1]]
        self.vel = [0, 0]
        self.acc = [0, 0]

        self.canvas = canvas
        self.dot = NULL
        self.start = start
        self.goal = goal

        self.width = width
        self.height = height

        self.dead = False

        self.fitness = 0
        self.reachedGoal = False
        self.isBest = False

    def show(self):
        if(self.dot == NULL):
            if(self.isBest):
                bonusRadius = 3
                self.dot = self.canvas.create_oval(self.pos[0]-DOT_RADIUS-bonusRadius, self.pos[1]-DOT_RADIUS-bonusRadius, self.pos[0]+DOT_RADIUS+bonusRadius, self.pos[1]+DOT_RADIUS+bonusRadius, fill='yellow')
            else:
                self.dot = self.canvas.create_oval(self.pos[0]-DOT_RADIUS, self.pos[1]-DOT_RADIUS, self.pos[0]+DOT_RADIUS, self.pos[1]+DOT_RADIUS, fill='black')

        else:
            if(not self.dead and not self.reachedGoal):
                self.canvas.move(self.dot, self.vel[0], self.vel[1])


    def move(self):
        if(len(self.brain.directions) > self.brain.step):
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        else:
            self.dead = True

        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]

        if(self.vel[0] > 5):
            self.vel[0] = 5
        elif(self.vel[0] < -5):
            self.vel[0] = -5

        if(self.vel[1] > 5):
            self.vel[1] = 5
        elif(self.vel[1] < -5):
            self.vel[1] = -5

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def update(self):
        if(not self.dead and not self.reachedGoal):
            self.move()
            distance = self.distance(self.pos, self.goal)
            if(self.pos[0] < DOT_RADIUS or self.pos[0] > self.width - DOT_RADIUS or self.pos[1] < DOT_RADIUS or self.pos[1] > self.height - DOT_RADIUS):
                self.dead = True
            elif(Obstacles.colided(self.pos)):
                self.dead = True
            elif distance < 5:
                self.reachedGoal = True



    def calculateFitness(self):
        if(self.reachedGoal):
            self.fitness = 1 + 10000.0/(self.brain.step * self.brain.step)
        else:
            distanceToGoal = self.distance(self.pos, self.goal)
            self.fitness = 1.0/(distanceToGoal * distanceToGoal)

    def distance(self, vec1, vec2):
        return math.sqrt(math.pow(vec1[0] - vec2[0], 2) + math.pow(vec1[1] - vec2[1], 2))

        
    def getBaby(self):
        baby = Dot(self.width, self.height, self.canvas, self.start, self.goal, self.brain.size)
        baby.brain.directions = self.brain.directions.copy()
        return baby