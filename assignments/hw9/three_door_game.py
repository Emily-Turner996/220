"""
    Name: Emily Turner
    three_door_game.py

    Problem: create a game where one randomized door must be clicked to win

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Rectangle, Point, Text
from button import Button
from random import randint


def set_up_door(p1x, p1y, p2x, p2y, label):
    rectangle = Rectangle(Point(p1x, p1y), Point(p2x, p2y))  # set up the rectangle info
    door = Button(rectangle, label)  # create door object using rectangle and label
    return door  # return the object


def set_up_message(center_x, center_y, words):
    message = Text(Point(center_x, center_y), words)
    return message


def draw_messages(message1, message2, win):  # instead of drawing both messages everytime
    message1.draw(win)  # top message
    message2.draw(win)  # bottom message


def check_all_buttons(button1, button2, button3):  # returns true if any button was hit
    any_button_hit = bool(button1 or button2 or button3)
    return any_button_hit


def find_clicked_door(b1_hit, b2_hit, door1, door2, door3):  # determines what was clicked
    if b1_hit:
        clicked_door = door1
    elif b2_hit:
        clicked_door = door2
    else:
        clicked_door = door3
    return clicked_door  # will be the door that was clicked


def set_winning_door(random_num, door1, door2, door3):  # determines winning door
    if random_num == 1:
        winning_door = door1
    elif random_num == 2:
        winning_door = door2
    else:
        winning_door = door3
    return winning_door  # the random, winning door


def create_second_screen(winning_center, clicked_center, door_clicked, winning_door, win):
    # determines if won/lost and sets up final screen accordingly
    if winning_center == clicked_center:  # if won
        door_clicked.color_button("green")
        message1 = set_up_message(8, 13, "You Win!")
        message2 = set_up_message(8, 3, "Click to close")
    else:  # if lost
        door_clicked.color_button("red")
        message1 = set_up_message(8, 13, "You Lost!")
        message2 = set_up_message(8, 3, "{0} is my secret door".format(winning_door.get_label()))
    # draw results of decision structure (draws final screen)
    door_clicked.draw(win)
    draw_messages(message1, message2, win)


def main():
    # set up graphics window
    win = GraphWin("Three Door Game", 800, 500)
    win.setCoords(0, 0, 16, 16)

    # CREATE OBJECTS (ON FIRST SCREEN):
    # door1 (make and draw)
    door1 = set_up_door(2, 7, 4, 9, "Door 1")  # create door1 object
    door1.draw(win)  # gets rectangle and label to actually show up, using method
    # make and draw door 2
    door2 = set_up_door(7, 7, 9, 9, "Door 2")  # create door2 object
    door2.draw(win)
    # make and draw door 3
    door3 = set_up_door(12, 7, 14, 9, "Door 3")  # create door3 object
    door3.draw(win)
    # draw initial messages
    message1 = set_up_message(8, 13, "I have a secret door")  # set up message 1
    message2 = set_up_message(8, 3, "click to choose my door")  # set up message 2
    draw_messages(message1, message2, win)  # draw both messages at once

    # set door clicked initial (boolean) value
    button_hit = False

    while not button_hit:  # while no doors are clicked
        click_point = win.getMouse()  # pause until clicks anywhere, stores point
        # check if doors were clicked:
        button1_hit = door1.is_clicked(click_point)  # check if door1 was clicked, bool
        button2_hit = door2.is_clicked(click_point)
        button3_hit = door3.is_clicked(click_point)
        # function to return true if any of the buttons were true:
        button_hit = check_all_buttons(button1_hit, button2_hit, button3_hit)

    # CLEAR FIRST SCREEN, part 1 of transition
    door_clicked = find_clicked_door(button1_hit, button2_hit, door1, door2, door3)
    door_clicked.undraw()
    message1.undraw()
    message2.undraw()

    # SET UP RANDOM, WINNING DOOR:
    random_num = randint(1, 3)
    winning_door = set_winning_door(random_num, door1, door2, door3)

    # CHECK IF WON OR LOST, 2nd part of transition
    # determine where the centers are, will use to determine if clicked winning door
    winning_center = winning_door.get_center()
    clicked_center = door_clicked.get_center()
    # function that sets up and draws the second screen:
    create_second_screen(winning_center, clicked_center, door_clicked, winning_door, win)

    # CLOSING THE PROGRAM:
    win.getMouse()  # so it doesn't close immediately
    win.close()  # close the program


if __name__ == '__main__':
    main()
