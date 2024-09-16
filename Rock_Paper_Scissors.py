# Ask user input for rock paper scissors
   # Correct if user inputs response not permitted
# Generate a computerized choice for one of the choices
# Compare the choices of the user vs the computer
# Genrater a response // logic
   # Rock beats Scissors
   # Scissors beats Paper
   # Paper beats Rock
   # Tie if choices are same

import random

def game_start():
   while True:
      try:
         comp_choice = random.choice(["rock", "paper", "scissors"])
         user_input = input("Rock, Paper or Scissors? ").lower()

         if user_input not in ["rock", "paper", "scissors"]:
            raise ValueError("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")

         if user_input == comp_choice:
            print("It's a draw! You both chose the same.")
         elif (user_input == "rock" and comp_choice == "scissors") or \
            (user_input == "paper" and comp_choice == "rock") or \
            (user_input == "scissors" and comp_choice == "paper"):

            print(f"You chose {user_input}. Computer chose {comp_choice}. You win!")
         else:
            print(f"You chose {user_input}. Computer chose {comp_choice}. You lose!")

         play_again = input("Would you like to play again? (Yes/No) ").lower()
         if play_again not in ["yes", "no"]:
            raise ValueError("Invalid input. Please type 'yes' or 'no'.")
         if play_again == "no":
            print("Thanks for playing!")
            break
      except ValueError as e:
         print(e)

game_start()