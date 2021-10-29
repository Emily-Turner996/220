"""
    Name: Emily Turner
    bumper.py

    Problem: simulate bumper cars in graphics window

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
from graphics import *
from random import randint, choice
import math


def get_random_color():  # select a random color*
    random_color = choice(["red", "orange", "yellow", "green", "blue", "purple", "pink"])
    return random_color


def get_random_int():  # choose random integers for movement*
    pass


def calculate_distance(x1, y1, x2, y2):  # check distance between center of the balls, HAVEN"T TESTED
    distance = math.sqrt(((x2-x1) ** 2) + ((y2 - y1) ** 2))  # distance formula
    return distance


def did_collide():  # determine if the balls collided*
    pass


def hit_vertical():  # determine if the ball hit the sides*
    pass


def hit_horizontal():  # determine if the ball hit the top or bottom*
    pass


def wall_collision():  # combine tests for vertical and horizontal collisions
    pass


def draw_ball(x, y, random_color, win):  # create and draw ball
    circle = Circle(Point(x, y), 1)  # create circle with xy points and radius of 1
    circle.setFill(random_color)
    circle.draw(win)
    return circle



def main():
    # Create Graphics Window
    win = GraphWin("Bumper", 600, 600)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("thistle1")  # set background color, could try lavender too!!!

    # Select ball colors
    color_1 = get_random_color()  # run function to get a random color
    color_2 = get_random_color()  # had to add these so i could add it to parameters for draw_ball

    # Create balls
    ball_1 = draw_ball(3, 5, color_1, win)  # this concept works, at least to get the thing on the screen
    ball_2 = draw_ball(7, 5, color_2, win)

    win.getMouse()  # pause before do funky shit

    # move. PLaying to figure out how to do basic movement, see how it works. Playground. Probably irrelevant.
    for i in range(9):
        ball_1.move(.5, -.5)
        time.sleep(.001)

    win.getMouse()  # close program, at least while testing


# remember to change what you import from graphics before you turn it in!! And make sure lines are right length!!
if __name__ == '__main__':
    main()
