#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 8, 2023
# This program gets a number from the user and will use a
# while true in place of a do..while statement to find the factorial of a number.


def main():
    # introduce program to user
    print("This program gets the input from the user and tells them the factorial.")

    # declare variables
    factorial = 1
    counter = 0

    # get user input
    user_num_str = input("Please enter a positive integer: ")

    # try converting user input to an integer
    try:
        user_num_int = int(user_num_str)

        # check if user number is negative
        if user_num_int >= 0:
            # do..while loop
            while True:
                # increment counter by 1
                counter = counter + 1

                # factorial multiplied by counter
                factorial = factorial * counter

                print("Tracking {} times through loop.".format(counter))

                # condition for loop to run
                if counter >= user_num_int:
                    break

                # display the factorial of user number
            print("The factorial of {} is {}.".format(user_num_int, factorial))

        # if user number is a negative tell user
        else:
            print("{} is not a positive integer.".format(user_num_int))

    # catching invalid user inputs
    except Exception:
        print("{} is not a positive integer".format(user_num_str))


if __name__ == "__main__":
    main()
