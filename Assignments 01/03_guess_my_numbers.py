# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48
import random

def main():
    random_number = random.randint(1, 100)
    
    print("I'm thinking of a magical number between 1 and 100... Can you read my mind? 😜")
    
    while True:
        user_input = input("Take a wild guess! (or type 'hint' for a secret clue, or 'c' to chicken out): ")
        
        if user_input.lower() == "c":
            print("Running away, huh? Maybe next time you'll be braver! 😆 Bye-bye!")
            break

        if user_input.lower() == "hint":
            print(f"Okay, okay... I'll whisper a secret: The number is {random_number}! 🤫")
            continue
        
        try:
            guess = int(user_input)
        except ValueError:
            print("Oops! That's not a number! Try again, you silly goose. 🦢")
            continue
        
        if guess < random_number:
            print("Too low! Aim higher, champion! 🚀")
        elif guess > random_number:
            print("Whoa! That's too high! Come back down to Earth! 🌍")
        else:
            print(f"🎉 Woohoo! You did it! The number was {random_number}! You are officially a mind reader! 🧙‍♂️")
            break

if __name__ == "__main__":
    main()