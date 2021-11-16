"""
create a button object to be used in three_door_game.py
Object will take shape and a label (string)
Will draw a rectangle with text inside
"""
from graphics import Text
# from graphics import GraphWin, Point, Rectangle, Text


class Button:
    """
    Class representing a button with a shape and a label
    """

    def __init__(self, shape, label):  # initializes shape and text
        self.shape = shape
        # get the center of rectangle here so it can be the center of self.text:
        center_point = shape.getCenter()
        self.text = Text(center_point, label)

    def get_label(self):
        """
        returns the text of the button in a string
        """
        text_object = self.text
        text_string = text_object.getText()  # get text from the text object
        return text_string

    def draw(self, win):
        """
        draws the button with text on it, returns void
        """
        door = self.shape
        label = self.text
        door.draw(win)
        label.draw(win)

    def undraw(self):
        """
        undraws button as well as the associated label, returns void
        """
        door = self.shape
        label = self.text
        door.undraw()
        label.undraw()

    def __get_corners(self):
        """
        determines x and y coordinates of the rectangle's corner points
        """
        rectangle = self.shape
        x_1 = rectangle.getP1().getX()
        y_1 = rectangle.getP1().getY()
        x_2 = rectangle.getP2().getX()
        y_2 = rectangle.getP2().getY()
        return x_1, y_1, x_2, y_2

    def get_center(self):
        """
        Gets the center point of the rectangle
        """
        rectangle = self.shape
        center_point = rectangle.getCenter
        return center_point

    def is_clicked(self, click_point):
        """
        will return True if the point is within the button (including the edges)
        returns bool
        """
        mouse_x = click_point.getX()
        mouse_y = click_point.getY()
        x_1, y_1, x_2, y_2 = self.__get_corners()
        # test if click was within corners
        button_hit = bool(x_1 <= mouse_x <= x_2 and y_1 <= mouse_y <= y_2)
        return button_hit

    def color_button(self, color):
        """
        color the button with color, returns void
        """
        self.shape.setFill(color)

    def set_label(self, label):
        """
        Updates the button text, returns void.
        """
        center_point = self.shape.getCenter()
        self.text = Text(center_point, label)
