# Number guesser 
import random

# random number between 1 an 100
magic_number = random.randint(1, 100)
print(magic_number)

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

  while attempts != 0 and not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    choice = int(input("Take a guess: "))

    if choice > magic_number:
      print("Too high")
      attempts -= 1
    elif choice < magic_number:
      print("Too low")
      attempts -= 1
    else:
      game_over = True
  
  if game_over == True:
    print("You guessed right")
    print(magic_number)
  else:
    print("You guessed wrong")
    print(magic_number)

play_game()