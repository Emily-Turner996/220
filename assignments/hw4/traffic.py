"""
    Name: Emily Turner
    traffic.py

    Problem: determine the avg number of vehicles on different roads daily and the total and
    avg numbers of cars on all roads

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""


def main():
    total_count = 0  # set default value for total_count, to be updated everytime sub-loop runs

    number_roads_surveyed = eval(input("How many roads were surveyed? "))  # input number of roads

    # MAIN LOOP
    for _ in range(number_roads_surveyed):
        # set default value for road_sum, to be updated when sub-loop runs and reset for each road
        road_sum = 0

        # Get input for number of days surveyed
        days_surveyed = eval(input("How many days was road surveyed? "))

        # SUB-LOOP
        for _ in range(days_surveyed):
            # Get input for # of cars that traveled in one day
            daily_car_count = eval(input("How many cars traveled on day? "))

            # Update values
            road_sum = road_sum + daily_car_count
            total_count = total_count + daily_car_count

            # end of sub loop

        # Calculate the road's avg vehicles/day
        avg_count_of_road = round((road_sum / days_surveyed), 2)

        # Print result
        print("Road average vehicles per day:", avg_count_of_road)

        # end of main loop

    # Calculation
    avg_per_road = round((total_count / number_roads_surveyed), 2)

    # Print Final Outputs
    print("Total number of vehicles traveled on all roads:", total_count)
    print("Average number of vehicles per road:", avg_per_road)


if __name__ == '__main__':
    main()
