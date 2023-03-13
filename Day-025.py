# Return Command
# Random Pin Generate

def pinPicker(number):
  import random
  pin = ""
  for i in range(number):
    pin += str(random.randint(0,9))
  return pin

mypin = pinPicker(4)
print("")
print("")
print("Your random pin is",mypin)
print("")
print("")