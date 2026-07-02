#To generate the random numbers or to fix the secret number between 1 to 100
import random

# stores user guessing attempts
user_scores = []
# stores computer guessing attempts
computer_scores = []    

#Initialized secret number between 1 to 100
secret_number_between = random.randint(1,100) 
#Initialize the attempts to 0
attempts = 0 

# Just to tell what you have to do
print("Guess the number between 1 to 100!") 

#This is the while loop. Let's start to loop until guessing is True
while True : 
    try:
        # initialized input guessing number to "guess"
        guess = int (input("Enter your guess: ")) 

        #Let's start comparison with random number generated to guessing number
        if guess < 1 or guess > 100:
            #if it is greater than 100 or less than 100, this sentence pop_up
            print("Please enter a number between 1 and 100.") 
            continue #Let's continue

        #If guessed number is wrong attempt initialized to +=1
        attempts += 1 

        # Calculate how far the guess is from the secret number
        difference = abs(secret_number_between - guess)

        #if guessed value less than secret number
        if guess < secret_number_between: 
            #To tell user to "You are guessing number which is lower than secret number
            print("You are guessing too low!") 

        # if guessed number is greater than secret number
        elif guess > secret_number_between: 
            # To tell user to "You are guessing number which is greater than secret number"
            print("You are guessing too high!") 

        else: #Else for guessing is correct with number of attempts
            #To know user to tell you are guessed correct!
            print(f"correct! You are guessed it in {attempts} attempts.")
           
            #Save score
            user_scores.append(attempts)

            #else will end here or break here
            break

    # A ValueError when user give ValueError happens when the type is correct, but the value cannot be converted or makes no sense
    except ValueError: 
        print("\nPlease enter the valid integer.")
        # It do not count invalid inputs as an attempt
        print("\nBe cool! I am not counting your invalid attempt")
        attempts -= 1 


########################################Computer Turn to Guess Now######################################

# We are writing a program here to computer to guess number what user thinking
print("\n\n\n Hey! It's My turn to Guess")
# It is telling user to think of a number
print("\n Think of a number between 1 and 100.")
#Telling to user to "Enter" once done with thinking:)
input("\n Press Enter when you're ready...")

#Initializing low is 1
low = 1
#Initializing high is 100
high = 200
#Initializing attempts is 0
attempts = 0

#Run the loop as long as low is less than or equal to high means 1<=100 or our range is valid 
while low <= high:
    # Increase the attempt counter for each guess
    attempts += 1

    # Calculate the middle value of the current range
    guess = (low + high) // 2

    # Show the computer's current guess
    print(f"\nMy guess is: {guess}")
    # Ask the user whether the guess is high, low, or correct
    feedback = input("Is it (H)igh, (L)ow, or (C)correct? ").lower()

    # If the guess is correct
    if feedback == "c":
        # Print success message with number of attempts
        # Exit the loop because the game is finished
        print(f"\n I guessed your number in {attempts} attempts!")

        #Save computer score
        computer_scores.append(attempts)

        break

      # If the user says the guess is too high
    elif feedback == "h":
        high = guess - 1

    # Reduce the upper limit because the number must be smaller
    elif feedback == "l":
        low = guess + 1

     # If input is invalid
    else:
        # Ask user to enter valid input
        print("Please enter H, L, or C.")

# If the loop ends without a correct guess
else:
    # Print error message for inconsistent answers
    print("\nHmm... Something doesn't add up.")
    # Explain possible issue with user feedback
    print("Did you change your number or give inconsistent hints?")

#######################################SCORE BOARD###################################################

# Final Scoreboard
print("\n+--------------------------------------+------------+")
print("| Game                                 | Attempts   |")
print("+--------------------------------------+------------+")

# User Guessing Game
if user_scores:
    print(f"| {'User Guessing Game':<36} | {user_scores[0]:<10} |") #36 is column width
else:
    print(f"| {'User Guessing Game':<36} | {'Not Played':<10} |")

# Computer Guessing Game
if computer_scores:
    print(f"| {'Computer Guessing Game':<36} | {computer_scores[0]:<10} |")
else:
    print(f"| {'Computer Guessing Game':<36} | {'Not Played':<10} |")

print("+--------------------------------------+------------+")