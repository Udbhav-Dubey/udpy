'''Exercise 10: Call Function using both positional and keyword arguments

Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function using both positional and keyword arguments.'''

def describe_pet(animal_type, pet_name):
  print(f"\nI have a {animal_type} named {pet_name}.")
describe_pet('hamster', 'Harry')
describe_pet('dog', 'Lucy')
describe_pet(animal_type='cat', pet_name='Whiskers')
describe_pet(pet_name='Buddy', animal_type='goldfish')
