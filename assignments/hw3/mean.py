"""
    Name: Emily Turner
    mean.py

    Problem: This program will take any given number of values inputted by user,
    calculate the RMS average, Harmonica mean and Geometric mean,
    then output the mean values.

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
import math  # so i can use square root function


def main():
    # set initial values to be updated with user input
    running_sum = 0  # so user's input can be added to it
    denominator = 0  # so reciprocals can be added
    product = 1  # so user's inputs can be multiplied

    # Get number of values to be inputted
    number = eval(input("enter the number of values to be entered: "))

    # Loop
    for i in range(number):
        # INPUT VALUES
        value = eval(input("enter value "))  # get the user input (and will repeat n times)

        # CALCULATIONS
        # RMS Average
        running_sum = running_sum + (value ** 2)
        rms = round(math.sqrt(running_sum / number), 3)

        # Harmonica Mean
        recip = 1 / value
        denominator = denominator + recip
        harmonica = round((number / denominator), 3)

        # Geometric Mean
        product = product * value
        geometric = round(product ** (1 / number), 3)
        # End loop

    # PRINT RESULTS
    print(rms)  # RMS average
    print(harmonica)  # Harmonica mean
    print(geometric)  # Geometric mean


if __name__ == '__main__':
    main()
