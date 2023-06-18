import turtle
import random
import time

#Making a background color
screen = turtle.Screen()
screen.bgcolor('lightpink') #screen is a light pink

#We want 2 players. Whoever gets to the other side first wins

#Player One - basic set up
player_one = turtle.Turtle()
#Color of player one
player_one.color('green')
#Make this player a turtle
player_one.shape('turtle')

#Player 2 basic setup - clone player 1 to avoid duplicate code

player_two = player_one.clone()
player_two.color('red')

#Position our players
player_one.penup()
player_one.goto(-300, 200)


player_two.penup()
player_two.goto(-300, -200)
player_two.pendown()

#Drawing the finish line
player_one.goto(300,-250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish!', font=40)
#Allows player one to go back to the start
player_one.penup()
player_one.color('Green')
player_one.goto(-300,200)
player_one.right(90)

#We need to make sure both players have their pens down
player_two.pendown()
player_one.pendown()

#Create values for the die
die = [1, 2, 3, 4, 5, 6]

#let's create the game!

for i in range(30):
    if player_one.pos() >= (300, 250):
        print("Player One Wins! Good job Turtle!")
        break
    elif player_two.pos() >= (300, -250):
        print("Player Two Wins! Good job Turtle!")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30*die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30*die_roll2)
        time.sleep(1)

#this keeps the turtle drawing on the screen!
turtle.done()
