from random import randint
from art import logo

TURNS_EASY = 10
TURNS_HARD = 5

turns = 0
def check_number(guess, number, turns):
  if guess > number:
    print("Too high.")
    return turns - 1
  elif guess < number:
    print("Too low.")
    return turns - 1
  else:
    print(f"Congrats! The answer was {number}.")

def difficulty_level():
    level = input("Choose your difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
      return TURNS_EASY
    else:
      return TURNS_HARD

def game():
  print(logo)
  print("Welcome to Guess The Number! \nI'm thinking of a number between 1 and 100.") 
  number = randint(1,100)
  
  turns = difficulty_level()
  guess = 0
  while guess != number:
    print(f"You have {turns} chances left to guess the number.")
    
    guess =  int(input("Make a guess: "))
    turns = check_number(guess, number, turns)
    if turns == 0:
      print("You've run out of guesses. Too bad!")
      return
    elif guess != number:
      print("Try again.")
      
game()