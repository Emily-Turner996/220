"""
    Name: Emily Turner
    three_door_game.py

    Problem: create a game where one randomized door must be clicked to win

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
# from button import Button
from graphics import GraphWin, Rectangle, Point, Text
from hw9.button import Button  # this was how it corrected the import itself


def set_up_door(p1x, p1y, p2x, p2y, label):  # !
    rectangle = Rectangle(Point(p1x, p1y), Point(p2x, p2y))  # set up the rectangle info
    # label = Text(Point(center_x, center_y), label)  # set up the label info, DELETE LATER
    door = Button(rectangle, label)  # create door object using rectangle and label
    return door  # return the object


def set_up_message(center_x, center_y, words):  # !!?
    message = Text(Point(center_x, center_y), words)
    return message


def check_all_buttons(button1, button2, button3):  # function returns true if any button was hit
    any_button_hit = bool(button1 or button2 or button3)
    return any_button_hit


def main():
    # set up graphics window
    win = GraphWin("Three Door Game", 800, 500)
    win.setCoords(0, 0, 16, 16)

    # create doors (& initial messages) (SET UP FIRST SCREEN)
    # door1 (make and draw)
    door1 = set_up_door(2, 7, 4, 9, "Door 1")  # create door1 object !
    door1.draw(win)  # gets the rectangle and label to actually show up, using method
    # make and draw door 2
    door2 = set_up_door(7, 7, 9, 9, "Door 2")  # create door2 object !
    door2.draw(win)
    # make and draw door 3
    door3 = set_up_door(12, 7, 14, 9, "Door 3")  # create door 3 object !
    door3.draw(win)
    # draw initial messages
    message1 = set_up_message(8, 13, "I have a secret door")  # set up message 1 !!
    message1.draw(win)  # draw message 1
    message2 = set_up_message(8, 3, "click to choose my door")  # set up message 2 !!
    message2.draw(win)  # draw message 2

    # set door clicked initial (boolean) value
    button_hit = False

    # while no doors are clicked
    while not button_hit:  # while button_hit == False
        # keep opening screen up and running (until click correct place) ...
        # ...(may have to move down some code from the top, maybe not)
        # check if any doors where hit (probably use is_clicked method, maybe on each door)
        click_point = win.getMouse()  # pause until user clicks anywhere, stores point in variable
        print(click_point)  # TESTING
        # check if doors were clicked:
        button1_hit = door1.is_clicked(click_point)  # check if door1 was clicked, bool
        button2_hit = door2.is_clicked(click_point)
        button3_hit = door3.is_clicked(click_point)
        print(button1_hit, button2_hit, button3_hit)  # TESTNG
        # function to return true if any of the buttons were true:
        button_hit = check_all_buttons(button1_hit, button2_hit, button3_hit)


    # testing
    #win.close()  # just closes instead of whole transition thing
    door1.undraw()  # just something random, seeing that the undraw method works

    # undraw messages, buttons(?)

    # if hit correct door
    # run winning door code (change color, messages)

    # if hit wrong door
    # run losing door code (change color, messages)

    # this is just stuff for closing the program:
    win.getMouse()  # so it doesn't immediately close, TESTING
    win.close()  # close the program


if __name__ == '__main__':
    main()
