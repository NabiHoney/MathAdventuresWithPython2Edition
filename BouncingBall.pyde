ballList=[]

class Ball:
    def __init__(self,x,y):
        self.xcor = x
        self.ycor = y
        self.xvel = random(-2,2)
        self.yvel = random(-2,2)
        self.sz = random(5,50)
        self.col = color(random(255),
                         random(255),
                         random(255))
    
    def update(self):
        self.xcor += self.xvel
        self.ycor += self.yvel
        if self.xcor > width or self.xcor < 0:
            self.xvel = -self.xvel
        if self.ycor > height or self.ycor < 0:
            self.yvel = -self.yvel
        fill(self.col)
        ellipse(self.xcor,self.ycor,self.sz,self.sz)
        
def setup():
    size(600,600)
    for i in range(50):
        ballList.append(Ball(random(width),
                             random(height)))
def draw():
    background(0)
    for ball in ballList:
        ball.update()
