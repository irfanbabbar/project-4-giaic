
# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


"""
An example program that converts feet to inches using constants.
"""

# Constant: Number of inches in one foot
INCHES_IN_FOOT: int = 12  

def main():
    # Prompt the user to enter the number of feet
    feet: float = float(input("Enter number of feet: "))  
    
    # Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT  
    
    # Output the result
    print("That is", inches, "inches!")
    

# Required line to call the main() function when the script runs
if __name__ == '__main__':
    main()