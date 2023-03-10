
# While Ture loop

# while True:
#     print("This program is running")
#     goAgain = input("Go again?: ")
#     if goAgain == "no":
#         print("Aww, I was having a good time! ")


# Program
counter = 0
while True:
    answer = int(input("Enter a number: "))
    print("Adding it up!")
    counter += answer
    print("Current total is", counter)
    addAnother = input("Add another?")
    if addAnother == "no":
        break
print("Bye!")



