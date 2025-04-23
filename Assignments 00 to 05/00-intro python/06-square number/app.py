# Problem Statement
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0
def main():
    # Ask the user for a number
    num: float = float(input("Type a number to see its square: "))

    # Calculate the square and print the result
    print(str(num) + " squared is " + str(num ** 2))


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()