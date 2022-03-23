class Obstacles():
    obstacles = [
        [100,200,400,220],
        [0, 300, 200, 320],
        [300, 300, 500, 320]
    ]

    def drawObstacles(canvas):
        for i in range(len(Obstacles.obstacles)):
            canvas.create_rectangle(Obstacles.obstacles[i][0], Obstacles.obstacles[i][1], Obstacles.obstacles[i][2], Obstacles.obstacles[i][3], fill='gray')

    def colided(pos):
        for i in range(len(Obstacles.obstacles)):
            if(pos[0] > Obstacles.obstacles[i][0] and
               pos[0] < Obstacles.obstacles[i][2] and
               pos[1] > Obstacles.obstacles[i][1] and
               pos[1] < Obstacles.obstacles[i][3]):
                
                return True
        return False
