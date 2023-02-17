import turtle
import random
import math

t = turtle
screen = t.Screen()
screen.screensize(640, 480)
screen.title("Adventure Game")

isLoading = True
isEndLevel = False
isClosed = False

countLevel = 1

xPlayer = 0
yPlayer = 0

circleSize = random.randint(5, 15)

curCirclePosX = 0
curCirclePosY = 0

distance = 0



def StartGame():
    global isEndLevel
    global isLoading
    global countLevel
    isEndLevel = False
    isLoading = True
    t.hideturtle()
    screen.clear()
    screen.bgcolor("white")
    t.setpos(0, 150)
    t.write(" Level %s " % countLevel , False, align="center", font=("Arial", 32, "normal"))
    t.setpos(0, 0)
    t.write(" START GAME ", False, align="center", font=("Arial", 64, "normal"))
    t.penup()
    t.setpos(0, -150)
    t.write(" Press E to start game ", False, align="center", font=("Arial", 32, "normal"))
    while isLoading == True:
        screen.listen()
        screen.onkeypress(Loading, "e")
        t.done()
        
    

def Loading():
    global isLoading
    global xPlayer
    global yPlayer
    global distance
    global curCirclePosX
    global curCirclePosY
    global circleSize
    global countLevel
    
    screen.clear()
    screen.bgcolor("lightblue")
    t.color("red")
    while isLoading == True:
        circlePosX = random.randint(50,400)
        circlePosY = random.randint(50,400)

        t.penup()
        t.setposition(circlePosX, circlePosY)
        curCirclePosX = t.xcor()
        curCirclePosY = t.ycor()
        #print(curCirclePos)
        t.pendown()
        t.circle(circleSize)
        t.penup()

        t.setpos(-400, 0)

        xPlayer = t.xcor()
        yPlayer = t.ycor()

        distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
        distance +=2
        print("Level %s started" % countLevel)
        print("Distance to finish: %s" % distance)
        isLoading = False
    while isLoading == False:
    
        #Move events
        screen.listen()
        screen.onkeypress(MoveFD, "Right")
        screen.onkeypress(MoveBack, "Left")
        screen.onkeypress(MoveLeft, "Up")
        screen.onkeypress(MoveRight, "Down")
        #End move events

        t.done()
       

#Moving functions
def MoveFD():
    global xPlayer
    global curCirclePosX
    global curCirclePosY
    global circleSize
    xPlayer += 2
    t.setx(xPlayer)
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))

    if distance <= circleSize + 3.001:
        #screen.bgcolor("white")
        GameOver()

def MoveBack():
    global xPlayer
    global curCirclePosX
    global curCirclePosY
    global circleSize
    xPlayer -= 2
    t.setx(xPlayer)
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
    if distance <= circleSize + 3.001:
        #screen.bgcolor("white")
        GameOver()
    

def MoveLeft():
    global yPlayer
    global curCirclePosX
    global curCirclePosY
    global circleSize
    yPlayer += 2
    t.sety(yPlayer)
    
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
    #print(distance)
    if distance <= circleSize + 3.001:
        #screen.bgcolor("white")
        GameOver()

def MoveRight():
    global yPlayer
    global curCirclePosX
    global curCirclePosY
    global circleSize
    yPlayer -= 2
    t.sety(yPlayer)
    
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
    #print(distance)
    if distance <= circleSize + 3.001:
        #screen.bgcolor("white")
        GameOver()
#End moving functions

def GameOver():
    global countLevel
    isEndLevel = True
    t.hideturtle()
    screen.clear()
    screen.bgcolor("white")
    t.write(" END LEVEL ", False, align="center", font=("Arial", 64, "normal"))
    t.penup()
    t.setpos(0, -150)
    t.write(" Press E to start next ", False, align="center", font=("Arial", 32, "normal"))
    while isEndLevel == True:
        screen.listen()
        screen.onkeypress(StartGame, "e")
        countLevel += 1
        t.done()
        
 
def PrintDistance():
    global distance
    print(distance)

def CheckEdge():
    global yPlayer
    global xPlayer
   
        
print(isLoading)
print(-float(screen.window_width()/2))
StartGame()    

 



