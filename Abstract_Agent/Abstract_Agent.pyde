class Agent:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def sense(self,r,lx,ly):
      pass

  def action(self):
      pass

class Environment:
  def __init__(self,maze):
      self.maze= maze
      self.scale = len(maze) #assumes square array

  def display(self,w):
    s=w/self.scale
    for i, row in enumerate(self.maze):
        for j,col  in enumerate(row):
            fill(0)
            rect(j*s,i*s,s*col,s*col)
            
env = Environment(
        [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def setup():
    size(800,800)
    
def draw():
    background(255)
    env.display(width)
    print("---")
