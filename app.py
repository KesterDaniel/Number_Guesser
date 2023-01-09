# Number guesser 
import random

# random number between 1 an 100
magic_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100")

# ask for difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def play_game():
  game_over = False

  # setting difficulty level
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5

  