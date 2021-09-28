#Tomas de Camino Beck

#A_Star code modified from origianl code from Nicholas Swift
#based on seudocode in wikipedia

class Environment:
  def __init__(self,maze):
      self.maze= maze
      self.scale = len(maze) #assumes square array

  def setcolor(self,value):
    switch = {
        0: color(255,255,255),
        1: color(0,0,0),
        2: color(0,255,0)
    }
    return switch.get(value,0)

  def display(self,w):
    s=w/self.scale
    for i, row in enumerate(self.maze):
        for j,col  in enumerate(row):
            fill(self.setcolor(col))
            rect(j*s,i*s,s,s)

  def displayPath(self,w,path):
      s=w/self.scale
      for pos in path:
          fill(self.setcolor(2))
          rect(pos[1] * s,pos[0]* s,s,s)


class Node():
    #A*

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    #returns path

    # start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            
            
###################### Main ################
# x & y are inverted in array with respect to canvas
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

#Global variables
start = (0, 0)
end = (2, 6)
path = astar(env.maze, start, end)


def setup():
    size(600,600)
    ellipseMode(CORNER)

def draw():
    background(255)
    env.display(width)
    env.displayPath(width,path)
    s = width/env.scale
    #start position
    fill(color(0,0,255))
    circle(start[1]*s,start[0]*s,s)
    #end position
    fill(color(255,0,10))
    circle(path[-1][1]*s,path[-1][0]*s,s)
    
def mousePressed():
    global end
    global env
    global path
    global start 
    if mouseButton == LEFT:
        newY=int(mouseY*env.scale//height)
        newX=int(mouseX*env.scale//width)
        end = (newY,newX)
        print(end)
        path = astar(env.maze, start, end)

    if mouseButton == RIGHT:
        newY=int(mouseY*env.scale//height)
        newX=int(mouseX*env.scale//width)
        start = (newY,newX)
        path = astar(env.maze, start, end)
