# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2
def main():
    # Ask the user for the number to be divided (dividend)
    dividend: int = int(input("Please enter an integer to be divided: "))
    
    # Ask the user for the number to divide by (divisor)
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient (integer division)
    quotient: int = dividend // divisor
    
    # Calculate the remainder (modulo)
    remainder: int = dividend % divisor
    
    # Print out the result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# This line calls the main() function to run the program
if __name__ == '__main__':
    main()