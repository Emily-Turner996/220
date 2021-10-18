"""
    Name: Emily Turner
    vigenere.py

    Problem: implement the Vigenere cypher

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
from graphics import *


def prgm_txt(x, y, message, win):  # draws text
    item_text = Text(Point(x, y), message)
    item_text.draw(win)


def item_input_box(x, y, width, win):  # creates input boxes
    message_box = Entry(Point(x, y), width)
    message_box.draw(win)
    return message_box


def get_input(input_box):
    message = input_box.getText()  # reads the input, converts to string
    return message


def format_input(message):  # formats the input
    message = message.upper()  # change to caps
    message = message.replace(" ", "")  # get rid of spaces
    return message


def code(message, keyword):
    # formatting:
    message = format_input(message)  # formats the message input
    keyword = format_input(keyword)  # formats the codeword input

    # encrypting:
    encrypted_letters = []  # empty list so letters can be collected
    for i in range(len(message)):
        letter = message[i]
        keyword_repeated = i % len(keyword)  # to help the keyword loop as needed

        # convert letters into numbers:
        message_transversed = ord(letter) - 65
        keyword_transversed = ord(keyword[keyword_repeated]) - 65

        # shift numbers and convert back into letters:
        encoded_letter = chr(((message_transversed + keyword_transversed) % 26) + 65)

        encrypted_letters.append(encoded_letter)  # collect the new letters
    encrypted_text = "".join(encrypted_letters)  # combine letters into a string
    return encrypted_text


def main():
    win = GraphWin("Vigenere", 700, 500)
    win.setCoords(0, 0, 10, 10)

    # create button
    button_text = Text(Point(5, 6), "Encode")
    button_outline = Rectangle(Point(4, 7), Point(6, 5))
    button_text.draw(win)
    button_outline.draw(win)

    # creating entry boxes and obtain input
    prgm_txt(2, 9, "Message to code", win)
    message_input_box = item_input_box(6, 9, 45, win)
    prgm_txt(2, 8, "Enter Keyword", win)
    codeword_input_box = item_input_box(6, 8, 45, win)
    win.getMouse()  # needed (here) so there's time to enter text before anything else happens

    # get inputs
    message = get_input(message_input_box)  # gets the message input
    codeword = get_input(codeword_input_box)  # gets the codeword input

    # undraw button
    button_text.undraw()
    button_outline.undraw()

    # encrypt
    result = code(message, codeword)  # run code function to get output

    # display output and final messages
    prgm_txt(5, 5, "Resulting Message", win)
    prgm_txt(5, 4, result, win)
    prgm_txt(5, 1, "Click Anywhere to Close Window", win)

    win.getMouse()  # close program


if __name__ == '__main__':
    main()
