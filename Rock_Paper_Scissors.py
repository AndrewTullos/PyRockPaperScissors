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
   try:
      comp_choice = random.randrange(1, 4)
      if comp_choice == 1:
         comp_output = 'rock'
      elif comp_choice == 2:
         comp_output = 'paper'
      else: comp_output == 'scissors'
      
      user_input = input("Rock, Paper or Scissors? ").lower()

      if user_input == 'paper' and comp_output == 'rock':
         print('You chose 📃 \n Computer chose 🪨 \n You win!')
      elif user_input == 'scissors' and comp_output == 'paper':
         print('You chose ✂️ \n Computer chose 📃 \n You win!')
      elif user_input == 'rock' and comp_output == 'scissors' :
         print('You chose 🪨 \n Computer chose ✂️ \n You win!')
      elif user_input == 'rock' and comp_output == 'paper':
         print('You chose 🪨 \n Computer chose 📃 \n You lose!')
      elif user_input == 'paper' and comp_output == 'scissors':
         print('You chose 📃 \n Computer chose ✂️ \n You lose!')
      elif user_input == 'scissors' and comp_output == 'rock':
         print('You chose ✂️ \n Computer chose ✂️ \n You lose!')
      else: print("It's a draw! You both chose the same.")



   except:
      print("Please select 'rock', 'paper', or 'scissors'")

      # Convert choice to number
      # if user_input == rock:
      #    user_choice = 1



game_start()



