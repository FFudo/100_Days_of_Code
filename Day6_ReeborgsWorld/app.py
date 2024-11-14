# the section below is just to fix the editor underlines

def at_goal():
    return
def turn_left():
    return
def right_is_clear():
    return
def front_is_clear():
    return
def move():
    return

# This code is used in a maze challenge found here:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
while not at_goal():
    if right_is_clear() and not front_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
