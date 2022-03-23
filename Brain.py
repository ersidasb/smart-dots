import math
import random
import math

class Brain():
    def __init__(self, size):
        self.directions = []
        self.step = 0
        self.size = size
        self.initList()
        self.randomize()

    def initList(self):
        for i in range(self.size):
            self.directions.append([])

    def randomize(self):
        for i in range(self.size):
            randomAngle = random.uniform(0, 2*math.pi)
            self.directions[i] = [math.cos(randomAngle), math.sin(randomAngle)]

    def mutate(self):
        mutationRate = 0.01
        for i in range(len(self.directions)):
            rand = random.uniform(0, 1)
            if(rand < mutationRate):
                randomAngle = random.uniform(0, 2*math.pi)
                self.directions[i] = [math.cos(randomAngle), math.sin(randomAngle)]
