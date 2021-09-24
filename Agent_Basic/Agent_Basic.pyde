class Agent():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.angle = 0

    def display(self):
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.angle)
        rect(0, 0, 50, 50)
        popMatrix()


    def rotate(self, a):
        self.angle += a

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if (self.x > width or self.x<0):
            self.vx = -self.vx
        if (self.y > height or self.y<0):
            self.vy = -self.vy
    

agent = Agent(300, 300)
agent.vx = -2
agent.vy = 2.3

def setup():
    size(600, 600)
    rectMode(CENTER)

def draw():
    agent.display()
    agent.rotate(0.01)
    agent.move()
