"""
    Name: Emily Turner
    greeting_card.py

    Problem: display a Valentine's day greeting

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
from graphics import *
import time


def main():
    win = GraphWin(" ", 750, 750)
    win.setCoords(0, 0, 20, 20)  # changes where points go from, changing how grid works
    win.setBackground("lavender blush")

    # draw heart
    heart = Polygon(Point(10, 3), Point(1, 15), Point(5, 19), Point(10, 15), Point(15, 19), Point(19, 15))
    heart.setFill("light pink")
    heart.setOutline("light pink")
    heart.draw(win)

    # greeting message
    message_1 = Text(Point(10, 12), "Happy Valentine's Day!")
    message_1.setFace("courier")
    message_1.setSize(20)
    message_1.setStyle("bold")
    message_1.draw(win)

    # undraw message
    win.getMouse()
    message_1.undraw()

    # draw arrow
    arrowhead = Polygon(Point(20, -2), Point(20, 0), Point(22, 0))
    arrowhead.setFill("gainsboro")
    arrowhead.setOutline("gainsboro")
    arrowhead.draw(win)

    fletching = Polygon(Point(35, -15), Point(35, -16), Point(37, -18), Point(37, -17), Point(38, -17), Point(36, -15))
    fletching.setFill("brown")
    fletching.setOutline("brown")
    fletching.draw(win)

    shaft = Line(Point(21, -1), Point(37, -17))
    shaft.draw(win)

    # move arrow (loop?)
    for i in range(38):
        arrowhead.move(-.5, .5)
        fletching.move(-.5, .5)
        shaft.move(-.5, .5)
        time.sleep(.0005)

    # closing message
    time.sleep(.25)
    message_2 = Text(Point(10, 1), "Click anywhere to close")
    message_2.draw(win)

    win.getMouse()  # close window


if __name__ == '__main__':
    main()
