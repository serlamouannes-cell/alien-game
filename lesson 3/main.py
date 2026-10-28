import pgzrun
import random

HEIGHT = 400
WIDTH = 400
TITLE = "alien game"

message = "Game starts"

alien=Actor('alien')
alien.pos=50,50

def draw():
    screen.clear()
    screen.fill(color="brown")
    screen.draw.text(message, center=(200,20), fontsize=30, color="black")
    alien.draw()

def move_alien():
    alien.x=random.randint(50,350)
    alien.y=random.randint(50,350)

def on_mouse_down(pos):
    print("Hi")
    global message
    if alien.collidepoint(pos):
        message="Good Shot!"
        move_alien()
    else:
        message="You missed try again"

move_alien()
pgzrun.go()