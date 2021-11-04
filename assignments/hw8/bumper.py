"""
    Name: Emily Turner
    bumper.py

    Problem: simulate bumper cars in graphics window

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
from random import randint, choice
import math
from graphics import GraphWin, Circle, Point, time


def get_random_color():  # select a random color*
    random_color = choice(["red", "orange", "yellow", "green", "blue", "purple", "pink"])
    return random_color


def draw_ball(center_x_value, center_y_value, random_color, win):  # create and draw ball
    circle = Circle(Point(center_x_value, center_y_value), 50)  # (x,y) center point, radius of 10
    circle.setFill(random_color)
    circle.draw(win)
    return circle


def get_random(move_amount):  # choose random ints for movement
    random_num = randint(-move_amount, move_amount)
    return random_num


def get_random_directions(number):  # choose random ints for both balls' movement without any impact
    b1_x = randint(-number, number)
    b1_y = randint(-number, number)
    b2_x = randint(-number, number)
    b2_y = randint(-number, number)
    return b1_x, b1_y, b2_x, b2_y  # these will dictate where both balls move


def get_center_point(ball):  # find the coords of a ball
    center_point = ball.getCenter()  # get the center point of ball
    center_x_value = center_point.getX()  # get x-coord of ball
    center_y_value = center_point.getY()  # get y-coord of ball
    return center_x_value, center_y_value


def did_collide(ball_1, ball_2):  # determine if the balls collided*
    # Calculate impact distance
    radius_1 = ball_1.getRadius()
    radius_2 = ball_2.getRadius()
    impact_distance = radius_1 + radius_2

    # calculate distance
    center_x1, center_y1 = get_center_point(ball_1)  # get center point values for ball1
    center_x2, center_y2 = get_center_point(ball_2)  # get center point values for ball2
    # plug values into distance formula:
    distance = math.sqrt(((center_x2 - center_x1) ** 2) + ((center_y2 - center_y1) ** 2))

    # determine if the balls collided
    collision = bool(distance <= impact_distance)
    return collision


def get_vertical_impact_distance(ball, win):
    radius = ball.getRadius()
    impact_distance_far = win.getWidth() - radius  # depends on window size
    impact_distance_small = 0 + radius  # on the closer side
    return impact_distance_far, impact_distance_small


def get_horizontal_impact_distance(ball, win):
    radius = ball.getRadius()
    impact_distance_far = win.getHeight() - radius  # depends on window size
    impact_distance_small = 0 + radius  # on the closer side
    return impact_distance_far, impact_distance_small


def hit_vertical(ball, win):  # determine if the ball hit the sides*
    # calculate impact distances
    impact_far, impact_small = get_vertical_impact_distance(ball, win)

    # get y coordinate
    center_point = ball.getCenter()  # get the center point of ball
    center_x_value = center_point.getX()  # get x-coord of ball

    if center_x_value >= impact_far:  # test if hit one side
        vertical_hit = True
    elif center_x_value <= impact_small:  # test if hit other side
        vertical_hit = True
    else:  # didn't hit either
        vertical_hit = False
    return vertical_hit


def hit_horizontal(ball, win):  # determine if the ball hit the top or bottom*
    # calculate impact distances
    impact_far, impact_small = get_horizontal_impact_distance(ball, win)

    # get x coordinate
    center_point = ball.getCenter()  # get the center point of ball
    center_y_value = center_point.getY()  # get y-coord of ball

    if center_y_value >= impact_far:  # test if hit one side
        horizontal_hit = True
    elif center_y_value <= impact_small:  # test if hit other side
        horizontal_hit = True
    else:  # didn't hit either wall
        horizontal_hit = False
    return horizontal_hit


def wall_hit(horizontal_hit, vertical_hit):  # combine tests for hitting walls
    hit = bool(horizontal_hit or vertical_hit)
    return hit


def bounce_off_wall(ball, win):  # change direction after a ball hit a wall
    # calculate impact distances
    impact_far, impact_small = get_horizontal_impact_distance(ball, win)

    # get coords from balls
    center_x_value, center_y_value = get_center_point(ball)

    # change the direction values
    # check the top and bottom !
    if center_x_value <= impact_small:
        x_direction = randint(0, 10)
    elif center_x_value >= impact_far:
        x_direction = randint(-10, 0)
    else:
        x_direction = get_random(10)

    # check the sides !
    if center_y_value <= impact_small:
        y_direction = randint(0, 10)
    elif center_y_value >= impact_far:
        y_direction = randint(-10, 0)
    else:
        y_direction = get_random(10)

    return x_direction, y_direction


def collision_bounce(ball_1, ball_2):
    # get coords from balls
    # ball 1
    center_point = ball_1.getCenter()  # get the center point of ball 1
    b1_center_x_value = center_point.getX()  # get x-coord of ball 1
    # ball 2
    center_point = ball_2.getCenter()  # get the center point of ball 2
    b2_center_x_value = center_point.getX()  # get x-coord of ball 2

    # bounce balls different ways based on where they are
    if b1_center_x_value < b2_center_x_value:  # ball 1 is to the right
        b1_x = randint(-10, 0)
        b1_y = get_random(10)
        b2_x = randint(0, 10)
        b2_y = get_random(10)
    else:  # ball 1 is to the left
        b1_x = randint(0, 10)
        b1_y = get_random(10)
        b2_x = randint(-10, 0)
        b2_y = get_random(10)

    return b1_x, b1_y, b2_x, b2_y


def main():
    # Create Graphics Window
    win = GraphWin("Bumper", 600, 600)
    win.setBackground("thistle1")  # set background color

    # Select ball colors
    color_1 = get_random_color()  # run function to get a random color
    color_2 = get_random_color()

    # Create balls
    ball_1 = draw_ball(200, 300, color_1, win)
    ball_2 = draw_ball(400, 300, color_2, win)

    # Make movement
    b1_x, b1_y, b2_x, b2_y = get_random_directions(10)
    while win.checkMouse() is None:  # make a movement, repeatedly.
        # MAKE MOVEMENT
        ball_1.move(b1_x, b1_y)
        ball_2.move(b2_x, b2_y)
        time.sleep(.05)

        # CHECK IF HIT ANYTHING
        # Ball1-to-wall hit:
        horizontal_hit = hit_horizontal(ball_1, win)  # test if ball1 hit a horizontal wall
        vertical_hit = hit_vertical(ball_1, win)  # test if ball1 hit top/bottom
        hit = wall_hit(horizontal_hit, vertical_hit)  # true if hit any wall
        if hit:
            b1_x, b1_y = bounce_off_wall(ball_1, win)

        # Ball2-to-wall hit:
        horizontal_hit = hit_horizontal(ball_2, win)
        vertical_hit = hit_vertical(ball_2, win)
        hit = wall_hit(horizontal_hit, vertical_hit)
        if hit:
            b2_x, b2_y = bounce_off_wall(ball_2, win)

        # Ball-to-ball collision:
        # check the distance between them
        collision = did_collide(ball_1, ball_2)
        # change directions if true so they bounce off each other:
        if collision:
            b1_x, b1_y, b2_x, b2_y = collision_bounce(ball_1, ball_2)
    win.close()


if __name__ == '__main__':
    main()
