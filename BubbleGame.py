import turtle
import random
import math

t = turtle
screen = t.Screen()

screen.title("Collect Game")
screen.bgcolor("lightblue")
t.color("red")

circlePos = random.randint(50,400)

t.penup()
t.setposition(circlePos, circlePos)
curCirclePosX = t.xcor()
curCirclePosY = t.ycor()
#print(curCirclePos)
t.pendown()
t.circle(2)
t.penup()

t.setpos(-400, 0)


xPlayer = t.xcor()
yPlayer = t.ycor()

distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
distance +=2
print(distance)

#Moving functions
def MoveFD():
    global xPlayer
    xPlayer += 2
    t.setx(xPlayer)
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
    print(distance)
    if distance <= 3.001:
        #screen.bgcolor("white")
        GameOver()

def MoveBack():
    global xPlayer
    xPlayer -= 2
    t.setx(xPlayer)
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
    print(distance)
    if distance <= 3.001:
        #screen.bgcolor("white")
        GameOver()
    

def MoveLeft():
    global yPlayer
    yPlayer += 2
    t.sety(yPlayer)
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
    print(distance)
    if distance <= 3.001:
        #screen.bgcolor("white")
        GameOver()

def MoveRight():
    global yPlayer
    yPlayer -= 2
    t.sety(yPlayer)
    distance = math.sqrt(math.pow(t.xcor()- curCirclePosX, 2) + math.pow(t.ycor() - curCirclePosY, 2))
    print(distance)
    if distance <= 3.001:
        #screen.bgcolor("white")
        GameOver()
#End moving functions

def GameOver():
    t.hideturtle()
    screen.clear()
    screen.bgcolor("white")
    t.write(" GAME OVER ", False, align="center", font=("Arial", 64, "normal"))
    t.penup()
    t.setpos(0, 150)
    t.write(screen.textinput("NIM", "Name: "), False, align="center", font=("Arial", 32, "normal"))

def PrintDistance():
    global distance
    print(distance)

#Move events
screen.listen()
screen.onkeypress(MoveFD, "Up")
screen.onkeypress(MoveBack, "Down")
screen.onkeypress(MoveLeft, "Left")
screen.onkeypress(MoveRight, "Right")
#End move events

t.done()

