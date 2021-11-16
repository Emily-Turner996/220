"""
    Name: Emily Turner
    weighted_average.py

    Problem: calculate student and class averages from external file

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""


def break_down_lines(sublist, name_number, first_w, first_g):  # make w & g lists and set name
    """
    make lists for weight and grades and set the name
    """
    name_list = sublist[0:name_number]  # name in a list
    name = " ".join(name_list)  # name as a string
    name = name.replace(":", "'s average: ")  # make outputting the text easier
    w_list = sublist[first_w::2]  # list of weights
    w_list = list(map(int, w_list))  # convert w list to ints
    g_list = sublist[first_g::2]  # list of grades
    g_list = list(map(int, g_list))  # convert to ints
    return name, w_list, g_list


def weighted_average(in_file_name, out_file_name):  # required by directions
    """
    opens files, formats input info, computes student and class average, outputs to
    external file, then closes both files
    """
    # Open Files
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    content = in_file.readlines()  # to turn input file into list of lines
    stripped_list = [x.strip() for x in content]  # remove whitespace characters like \n

    class_grades = []  # default value for a list to be updated w/ ea. student

    # COMPUTE STUDENT AVG
    for each_value in stripped_list:
        # split them up
        sublist = each_value.split()  # make list for each person

        # get name, w_list, and g_list
        try:  # for people with 2 names
            name, w_list, g_list = break_down_lines(sublist, 2, 2, 3)
        except ValueError:  # for people with 3 names
            name, w_list, g_list = break_down_lines(sublist, 3, 3, 4)

        # DECISION STRUCTURE - determine need for error message
        weight_total = sum(w_list)
        if weight_total < 100:
            student_result = "Error: The weights are less than 100."  # setting result variable
        elif weight_total > 100:
            student_result = "Error: The weights are more than 100."  # setting result variable
        else:
            # COMPUTE STUDENT AVG
            product_list = [a * b for a, b in zip(w_list, g_list)]  # multiply w and g lists
            sum_of_products = sum(product_list)  # add all items in product list together
            student_avg = sum_of_products / 100  # divide by 100
            # student_avg = round(student_avg, 1)  # correct decimal places
            student_result = str(round(student_avg, 1))  # set result variable & change to string

            class_grades.append(student_avg)  # updates list of student averages

        # OUTPUT STUDENT AVG
        print(name + student_result, file=out_file)

    # COMPUTE CLASS AVG
    class_sum = sum(class_grades)
    class_avg = class_sum / len(class_grades)
    class_avg = round(class_avg, 1)
    class_avg = str(class_avg)  # change to string so can write

    # OUTPUT CLASS AVG
    print("Class average:", class_avg, file=out_file)

    # Close Files
    in_file.close()
    out_file.close()


def main():
    """
    runs the program
    """
    # run required function
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()
