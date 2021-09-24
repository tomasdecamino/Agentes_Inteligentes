class Node:

    def __init__(self, data,x,y):
        self.left = None
        self.right = None
        self.data = data
        self.x = x
        self.y = y
# Insert method to create nodes

    def insert(self, data):
        if self.data < data:
            if self.left is None:
               self.left = Node(data,self.x-20,self.y+50)
            else:
               self.left.insert(data)
        if self.data > data:
            if self.right is None:
               self.right = Node(data,self.x+20,self.y+50)
            else:
               self.right.insert(data)
    
    def display(self):
        circle(self.x,self.y,10)
        if self.left:
            line(self.x,self.y,self.left.x,self.left.y)
            self.left.display()
        if self.right:
            line(self.x,self.y,self.right.x,self.right.y)
            self.right.display()        


root = Node(12,300,10)

def setup():
    size(600, 600)
    global root
    root = Node(12,300,10)
    for v in range(20):
        root.insert(random(30))


def draw():
    root.display();
