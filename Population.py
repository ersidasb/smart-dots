from Dot import *
import random

class Population():
    
    def __init__(self, width, height, canvas, size, start, goal):
        self.dots = []
        self.maxNumberOfSteps = 400

        self.size = size

        self.canvas = canvas
        self.start = start
        self.goal = goal

        self.width = width
        self.height = height

        self.generation = 1
        self.bestDot = 0

        self.initList()

    def initList(self):
        for i in range(self.size):
            self.dots.append(Dot(self.width, self.height, self.canvas, self.start, self.goal, self.maxNumberOfSteps))

    def show(self):
        for i in range(1, len(self.dots)):
            self.dots[i].show()
        self.dots[0].show()

    def update(self):
        for i in range(len(self.dots)):
            if(self.dots[i].brain.step > self.maxNumberOfSteps):
                self.dots[i].dead = True
            if(not self.dots[i].dead):
                self.dots[i].update()

    def populationDead(self):
        for i in range(len(self.dots)):
            if(not self.dots[i].dead and not self.dots[i].reachedGoal):
                return False
        return True

    def calculateFitness(self):
        for i in range(len(self.dots)):
            self.dots[i].calculateFitness()

    def naturalSelection(self):
        newDots = []
        self.setBestDot()
        self.calculateFitnessSum()


        for i in range(len(self.dots)):
            newDots.append([])
        
        newDots[0] = self.dots[self.bestDot].getBaby()
        newDots[0].isBest = True
        if(self.dots[self.bestDot].reachedGoal):
            self.maxNumberOfSteps = self.dots[self.bestDot].brain.step


        for i in range(1, len(newDots)):
            parent = self.selectParent()

            newDots[i] = parent.getBaby()

        self.dots = newDots.copy()
        self.generation += 1


    def calculateFitnessSum(self):
        sum = 0
        for i in range(len(self.dots)):
            sum += self.dots[i].fitness
        self.fitnessSum = sum

    def selectParent(self):
        randomFitness = random.uniform(0, self.fitnessSum)
        runningSum = 0
        for i in range(len(self.dots)):
            runningSum += self.dots[i].fitness
            if(runningSum > randomFitness):
                return self.dots[i]
        return NULL

    def mutateBabies(self):
        for i in range(1, len(self.dots)):
            self.dots[i].brain.mutate()

    def setBestDot(self):
        maxFitness = 0
        maxFitnessIdx = 0
        for i in range(len(self.dots)):
            if(self.dots[i].fitness > maxFitness):
                maxFitness = self.dots[i].fitness
                maxFitnessIdx = i
        self.bestDot = maxFitnessIdx
