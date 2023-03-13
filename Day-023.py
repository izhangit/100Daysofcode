# Subroutines

def rollDice():
  import random
  dice = random.randint(1,6)
  print("You rolled",dice)
  
for i in range(50):
  rollDice()
