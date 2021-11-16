"""
create a button object to be used in three_door_game.py
Object will take shape and a label (string)
Will draw a rectangle with text inside
"""
from graphics import *  # GraphWin, Point, Rectangle


class Button:
    """
    Class representing a button with a shape and a label
    """

    def __init__(self, shape, label):  # initializes shape and text
        self.shape = shape  # this may or may not be correct, just trying to have something
        # get the centerpoint of rectangle here so it can be the centerpoint of self.text
        center_point = shape.getCenter()
        self.text = Text(center_point, label)  # might be correct, just trying to have smthng
        # LABEL is a STRING (input a string, not text object!) used to create the Text object

    def get_label(self):
        text_object = self.text
        text_string = text_object.getText()  # get the text from the text object
        return text_string  # idk what exactly gets returned, ...
        # ... if returned variable needs to be smthng particular
        # returns string.
        # returns the text of the button.
    # think this ^ is related to getText() and that returning...
    # ...self.text will mess it up, might need some string variable instead

    def draw(self, win):  # might bring color_button & set_label in this. ...
        # ... Mayb not. Mayb another one to combine them idk
        # returns void.
        # draws the button with text on it
        door = self.shape
        label = self.text
        door.draw(win)
        label.draw(win)

    def undraw(self):
        # returns void.
        # undraws button as well as the associated label.
        door = self.shape
        label = self.text
        door.undraw()
        label.undraw()

    def __get_corners(self):  # since getP1 and getP2 don't want to work
        rectangle = self.shape
        x_1 = rectangle.getP1().getX()
        y_1 = rectangle.getP1().getY()
        x_2 = rectangle.getP2().getX()
        y_2 = rectangle.getP2().getY()
        return x_1, y_1, x_2, y_2

    def is_clicked(self, click_point):
        # returns bool.
        # true if the point is within the button (including the edges).
        mouse_x = click_point.getX()
        mouse_y = click_point.getY()
        x_1, y_1, x_2, y_2 = self.__get_corners()
        # test if click was within corners
        button_hit = bool(x_1 <= mouse_x <= x_2 and y_1 <= mouse_y <= y_2)
        return button_hit

    def color_button(self, color):
        # returns void.
        # color the button with color.
        self.shape.setFill(color)  # ? just a random vague idea, might b completely off

    def set_label(self, label):  # still don't really get the point of this one, not yet
        # returns void.
        # update the button text.
        center_point = self.shape.getCenter()  # unless need self.shape equal to smthng b4 this
        self.text = Text(center_point, label)  # may or may not be it
