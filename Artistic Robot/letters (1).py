
def drawA():

    forward(1, .5)
    turnLeft(1,1.7)
    forward(1, 3)
    turnRight(1, 3.3)
    forward(1, 1.5)
    turnRight(1, 3.3)
    forward(1, 1.5)
    backward(1, 1.55)
    turnLeft(1, 3.2)
    forward(1, 1.7)
    turnLeft(1, 1.6)
    
def drawB():
    
    forward(1, .5)
    turnLeft(1, 2.4)
    forward(1, 3)
    
    #arc1
    turnRight(1, 2.5)
    forward(1, 1)
    turnRight(1, 1.4)
    forward(1, .75)
    turnRight(1, 1.4)
    forward(1, .75)
    turnRight(1, 1.7)
    forward(1, 1.2)
    
    #arc2
    turnLeft(1, 4.6)
    forward(1, 1)
    turnRight(1, 1.4)
    forward(1, .75)
    turnRight(1, 1.4)
    forward(1, .75)
    turnRight(1, 1.9)
    forward(1, 1.4)
    
    #end
    turnLeft(.5, 9.6)
    forward(1, 2)
    
    
def drawC():
    
    #first go
    forward(1, 2)
    turnLeft(1, 4.7)
    forward(1, 1)
    turnRight(1, 1.5)
    forward(1, 1.3)
    turnRight(1, 1.5)
    forward(1, 1.3)
    turnRight(1, 1.5)
    forward(1, 1)
    turnRight(1, 1)
    forward(1, .5)
    
    #back it up 
    turnRight(.5, 9.8)
    forward(1, .5)
    turnLeft(1, 1)
    forward(1, 1)
    turnLeft(1, 1.5)
    forward(1, 1.3)
    turnLeft(1, 1.5)
    forward(1, 1.3)
    turnLeft(1, 1.5)
    forward(1, 1)
    
    #base of the C
    turnLeft(1, 1)
    forward(1, .5)
    backward(1, .8)
    
    #end
    turnRight(.5, 2.2)
    forward(1, 1)
    
    
    
def drawD():
    
    forward(1, .5)
    turnLeft(1, 2.4)
    forward(1, 3)
    
    #arc
    turnRight(1, 2.5)
    forward(1, 1)
    turnRight(1, 1.5)
    forward(1, 1.2)
    turnRight(.5, 2)
    forward(.5, 2)
    turnRight(.5, 2)
    forward(1, 1.2)
    turnRight(1, 1.2)
    forward(1, 1)
    
    #end
    turnRight(.5, 10)
    forward(1, 2.5)
    
def drawE():
    
    forward(1,1)
    forward(1,2)
    backward(1,2)
    turnTo(90)
    forward(1,2)
    turnTo(360)
    forward(1,2)
    backward(1,2)
    turnTo(90)
    forward(1,2)
    turnTo(360)
    forward(1,2)
    backward(1,2)
    turnBy(90)
    backward(1,4)
    turnBy(90)
    backward(1,2)

def drawF():
    
    forward(1,1)
    turnBy(90)
    forward(1,2)
    turnBy(90)
    backward(1,2)
    forward(1,2)
    turnBy(90)
    backward(1,2)
    turnBy(90)
    forward(1,2)
    backward(1,2)
    turnBy(90)
    backward(1,4)
    turnBy(90)
    backward(1,2)

def drawG():
    
    forward(1,1)
    penDown()
    forward(1,1)
    turnBy(90)
    forward(1,2)
    turnBy(90)
    forward(1,1)
    backward(1,1)
    turnTo(90)
    backward(1,2)
    turnBy(90)
    forward(1,2)
    turnBy(45)
    turnBy(45)
    turnBy(45)
    backward(1,1)
    turnTo(45)
    turnBy(45)
    forward(1,3)
    turnBy(90)
    turnBy(45)
    backward(1,1)
    turnBy(45)
    turnBy(45)
    turnBy(45)
    forward(1,1.8)
    
def drawH():
    
    forward(1,1)
    turnBy(90)
    forward(1,2)
    turnBy(90)
    backward(1,2)
    forward(1,2)
    turnBy(90)
    backward(1,2)
    forward(1,2)
    turnBy(90)
    forward(1,2)
    turnBy(90)
    forward(1,2)
    backward(1,3.8)


def drawI():
    
    motors(1,1,1)
    motors(-1,-1,.5)
    turnBy(90)
    motors(1,1,1)
    turnBy(90)
    motors(1,1,.5)
    motors(-1,-1,1)
   
def drawJ():
    
    turnBy(90)
    motors(1,1,1)
    turnBy(90)
    penDown()
    motors(-1,-1,1)
    motors(1,1,.5)
    turnBy(90)
    motors(1,1,1)
    move(.1,.2)
    stop()
    #motors(1,0,10)
    
    
def drawK():
    
    penDown()
    turnBy(90)
    motors(1,1,2)
    motors(-1,-1,1)
    turnBy(-30)
    motors(1,1,1)
    motors(-1,-1,1)
    turnBy(-90)
    motors(1,1,1)
   
def drawL():
    
    turnBy(90)
    motors(1,1,1.5)
    penDown()
    motors(-1,-1,1.5)
    turnBy(-90)
    motors(1,1,1)

def drawM():
    
    
    turnBy(90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-110)
    forward(1,3)
    turnBy(30)
    backward(1,2.8)
    turnBy(-25)
    forward(1,3)
    turnBy(30)
    backward(1,2.8)
    turnBy(80)

def drawN():
    
    turnBy(90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-105)
    forward(1,3)
    turnBy(35)
    backward(1,3.1)
    turnBy(-35)
    forward(1,3.1)
    turnBy(15)
    backward(1,2.8)
    turnBy(-90)

def drawO():
    turnBy(90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(180)
    forward(1,1.5)
    move(.7,1)
    wait(6.6)
    stop()
    forward(1,1.5)

def drawP():
    
    turnBy(90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(-90)
    forward(1,3)
    turnBy(180)
    forward(1,1)
    turnBy(90)
    forward(1,3)
    turnBy(90)
    move(-.3,-.8)
    wait(6.35)
    stop()
    turnBy(-82)
    forward(1,2)
    turnBy(90)
    forward(1,2)

def drawQ():
    
    motors(.5, 6, 3.8)
    turnLeft(2, 1.3)
    forward(1, 1)
    turnLeft(.5, 9.65)
    forward(1, 2)
    turnLeft(.5, 2.9)
    forward(1,3)  
    
def drawR():
    
    turnLeft(.5, 4.85)
    forward(1, 3.5)
    turnRight(.5, 4.85)
    forward(.5, .5)
    turnRight(.5, 1)
    forward(.5, .5)
    turnRight(.5, 1)
    forward(.5, .5)
    turnRight(.5, 1)
    forward(.5, .5)
    turnRight(.5, 1)
    forward(.5, 1)
    turnRight(.5, 1)
    forward(.5, 1)
    turnRight(1, 1)
    forward(.5, 1)
    turnRight(1, 1)
    forward(1, .5)
    turnLeft(.5, 6.5)
    forward(1, 2)
    turnLeft(.5, 3)
    forward(1, 2)
    
def drawS():
    turnLeft(.5, 4.85)
    forward(1,1)
    backward(1,1)
    turnRight(.5, 4.85)
    forward(1,1.5)
    turnLeft(.5, 4.85)
    forward(1,1.5)
    turnLeft(.5, 4.85)
    forward(1,1)
    turnRight(.5, 4.85)
    forward(1,1.5)
    turnRight(.5, 4.85)
    forward(1,1.5)
    turnRight(.5, 4.85)
    forward(1,1)  
    turnLeft(.5, 9.7)
    forward(1,1)
    turnLeft(.5, 4.85)
    forward(1,1.5)
    turnLeft(.5, 4.85)
    forward(1,1.5)
    turnLeft(.5, 4.85)
    forward(1,1)
    turnRight(.5, 4.85)
    forward(1,1.5)
    turnLeft(.5, 4.85)
    forward(1,3)
   
    


def drawT():
    
    turnLeft(.5, 4.85)
    forward(1, 3)
    turnRight(.5, 4.85)
    forward(1, 1.5)
    backward(1, 3)
    forward(1, 1.5)
    turnRight(.5, 4.9)
    forward(1, 3)
    turnLeft(.5, 4.85)
    forward(1, 3)   

def drawU():
    
    turnLeft(.5, 4.85)
    forward(1, 3.5)
    backward(1, 3)
    turnRight(.5, 4.85)
    forward(1, 2)
    turnLeft(.5, 4.85)
    forward(1, 3)
    backward(1, 3.5)
    turnRight(.5, 4.85)
    forward(1, 3)

def drawV():
    
    forward(1, 1.5)
    turnLeft(3.2,1)
    forward(1,2.5)
    backward(1,2.5)
    turnRight(1.6, 1)
    forward(1,2.6)
    backward(1,2.5)
    turnRight(1.6, 1)
    forward(1,1)

def drawW():
    
    forward(1, 1.5)
    turnLeft(3.2,1)
    forward(1,2.5)
    backward(1,2.5)
    turnRight(1.6, 1)
    forward(1,2.5)
    turnLeft(1.6,1)
    backward(1,2.5)
    turnRight(1.6,1)
    forward(1,2.5)
    backward(1,2.5)
    turnRight(1.6,1)
    forward(1,1)

def drawX():
    
    turnLeft(1.5,1)
    forward(2,2)
    backward(1,2)
    turnLeft(1.5,1)
    forward(1,2)
    backward(2,2)
    turnRight(3,1)

def drawY():
    
    forward(1,1.5)
    turnLeft(2.45,1)
    forward(1.3,1.8)
    turnLeft(1,1.5)
    forward(1,1.4)
    backward(1,1.4)
    turnRight(1,3)
    forward(1,1.4)
    backward(1,1.4)
    turnLeft(1,1.5)
    backward(1.3, 1.8)
    turnRight(2.45,1)
    forward(1,1.5)

def drawZ():
    
    turnLeft(1.5,1)
    forward(2,2)
    turnRight(1.5,1)
    backward(1.3,2)
    forward(1.3,2)
    turnLeft(1.5,1)
    backward(2,2)
    turnRight(1.5,1)
    forward(1.5,2)




