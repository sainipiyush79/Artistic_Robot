from letters import *
from Graphics import *
sim = Simulation("Blank World", 1000, 1000, Color("lightgrey"))
sim.setup()
makeRobot("SimScribbler", sim)
sim.setPose(0, 40, 400, 0)
penDown()
def write(letter):
    
    if letter == 'A':
        drawA()
    elif letter == 'B':
        drawB()
    elif letter == 'C':
        drawC()
    elif letter == 'D':
        drawD()
    elif letter == 'E':
        drawE()
    elif letter == 'F':
        drawF()
    elif letter == 'G':
        drawG()
    elif letter == 'H':
        drawH()
    elif letter == 'I':
        drawI()
    elif letter == 'J':
        drawJ()
    elif letter == 'K':
        drawK()
    elif letter == 'L':
        drawL()
    elif letter == 'M':
        drawM()
    elif letter == 'N':
        drawN()
    elif letter == 'O':
        drawO()
    elif letter == 'P':
        drawP()
    elif letter == 'Q':
        drawQ()
    elif letter == 'R':
        drawR()
    elif letter == 'S':
        drawS()
    elif letter == 'T':
        drawT()
    elif letter == 'U':
        drawU()
    elif letter == 'V':
        drawV()
    elif letter == 'W':
        drawW()
    elif letter == 'X':
        drawX()
    elif letter == 'Y':
        drawY()
    elif letter == 'Z':
        drawZ()

def draw(word):
    speak(str(word))
    word = str.upper(word)
    for x in str(word):
        write(x)
draw('AEIMQV')
