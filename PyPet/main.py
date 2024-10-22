import time
import random

pet_food = ['chicken', 'fish', 'dog food', 'cat food', 'turtle food']

pets_list = [
    'cat', 'dog', 'fish', 'hamster', 'bird', 'rabbit', 'hamster', 'snake',
    'lizard', 'squirrel', 'chipmunk'
]

favorite_food_pet = random.choice(pet_food)


def feed_pet():
  print("Feeding your pet...")
  time.sleep(34)
  print("Your pet is full!")


def walk_pet():
  print("You pet is walking outside...")
  time.sleep(20)


def play_pet():
  print("You pet is playing with a ball...")
  time.sleep(12)


def pet():
  print("tapping on its head...")
  time.sleep(3)


def throw_pet():
  print("Opening the window, since you are living in a apartment")
  time.sleep(5)
  print(f"taking your {user_actions} to the window")
  time.sleep(3)
  print("Throw your pet...")
  time.sleep(2)
  print("Guess what?")
  time.sleep(2)
  print("You are going to jail")


class Animal:

  def __init__(self, name, age, favor_food):
    self.name = name
    self.age = age
    self.favor_food = favor_food

  def eat(self):
    return f"{self.name} is eating {self.favor_food}"


user_input = input("Enter a pet you wanted: ")
while True:

  animal_actions = Animal(user_input, random.randint(1, 10), favorite_food_pet)

  if user_input in pets_list:
    print(f"Animal: {animal_actions.name}")
    print(f"Age: {animal_actions.age}")
    print(f"Favorite Food: {animal_actions.favor_food}")
    print(f"You have selected: {user_input}")
  else:
    print("Please enter a valid pet")

  user_actions = input("What do you want to do with your pet?: ")

  if user_actions == 'feed it':
    feed_pet()
  elif user_actions == 'walk with it':
    walk_pet()
  elif user_actions == 'play with it':
    play_pet()
  elif user_actions == 'pet it':
    pet()
  elif user_actions == 'throw it':
    throw_pet()
    break
  elif user_actions == 'quit':
    break
  else:
    print("Please enter a valid options")
