# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

# x = 3.1415926
# rounded_x = round(x, 2) # rounds x to 2 decimal places 
# print(rounded_x) 

# # This would print out out 3.14

# x = 2.71828
# rounded_x = round(x, 4)
# print(rounded_x)

# # This would print out 2.7183

# x = 3
# rounded_x = round(x, 4)
# print(rounded_x) 

# # This would print 3
# # Note that the round function does not add on decimal places that are not there already 

# Sample Run

# $ python marsweight.py

# Enter a weight on Earth: 120

# The equivalent on Mars: 45.36 

# Sample Run

# $ python marsweight.py

# Enter a weight on Earth: 186

# The equivalent on Mars: 70.31
# Milestone #2: Adding in All Planets
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.
# ✅ Mars Weight Solution (Milestone #1)

"""
Prompts the user for a weight on Earth and prints the equivalent weight on Mars.
"""

# Constant for Mars gravity
MARS_MULTIPLE = 0.378

def main():
    # Prompt user for Earth weight
    earth_weight_str = input('Enter a weight on Earth: ')
    
    # Convert to float
    earth_weight = float(earth_weight_str)
    
    # Calculate Mars weight
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)
    
    # Display the result
    print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

if __name__ == '__main__':
    main()
# ✅ Planetary Weights Solution (Milestone #2)

"""
Prompts the user for a weight on Earth and a planet (in separate inputs). 
Then prints the equivalent weight on that planet.
"""

# Gravitational constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Prompt user for Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt user for planet name
    planet = input("Enter a planet: ")
    
    # Determine gravity constant using if-elif
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate equivalent weight
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)
    
    # Print result
    print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight))

if __name__ == '__main__':
    main()