#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Created: Nov 8, 2022
# A program which takes a user's input and
# lists the numbers from it to the power of 2


def main():

    # Spacer
    print("")

    # Tries to get the user's number as an integer.
    try:
        user_input = int(input("Enter a positive integer: "))
    # Exception used when the user failed to enter a number.
    except ValueError:
        input("Invalid input, input a positive number only!: ")
    # If statement in case of negative inputs.
    if user_input < 0:
        print("Input must not be a negative number, try again!")

    # Initializing counter
    counter = 0

    # Code ran until it's equal  with both the user input and counter.
    for counter in range(user_input + 1):
        power_of_two = counter**2
        print("{}^2 = {}".format(counter, power_of_two))


if __name__ == "__main__":
    main()
