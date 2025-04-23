
# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.
import random

NUM_SIDES = 6

def main():
    while True:
        user_input = input("Type 'roll' to roll the dice or 'exit' to quit: ").lower()
        if user_input == 'roll':
            die1 = random.randint(1, NUM_SIDES)
            die2 = random.randint(1, NUM_SIDES)
            total = die1 + die2
            print("First die:", die1)
            print("Second die:", die2)
            print("Total of two dice:", total)
        elif user_input == 'exit':
            print("Exiting the dice roller. Goodbye!")
            break
        else:
            print("Please type 'roll' or 'exit'.")

if __name__ == '__main__':
    main()