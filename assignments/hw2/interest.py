"""
    Name: Emily Turner
    interest.py

    Problem: this program will calculate the monthly interest charge on a credit card account

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""


def main():

    # GET INPUTS
    annual_rate = eval(input("What is the annual interest rate? "))  # annual interest rate
    cycle_length = eval(input("What is the cycle length? "))  # number of days in cycle
    net_balance = eval(input("What is the net (previous) balance? "))  # previous (net) balance
    net_payment = eval(input("What is the payment amount? "))  # payment amount
    payment_day = eval(input("What day (numerical) was the payment made? "))  # day of payment
    # RUN CALCULATIONS
    step_one_answer = net_balance * cycle_length  # step 1 calculations
    days_left = cycle_length - payment_day
    step_two_answer = net_payment * days_left  # step 2 calculations
    step_three_answer = step_one_answer - step_two_answer  # step 3 calculations
    avg_daily = step_three_answer / cycle_length  # step 4
    monthly_rate = annual_rate / 12 * .01
    monthly_charge = avg_daily * monthly_rate
    monthly_charge = round(monthly_charge, 2)  # trying to get correct decimals

    # PRINT RESULTS
    print(monthly_charge)


if __name__ == '__main__':
    main()
