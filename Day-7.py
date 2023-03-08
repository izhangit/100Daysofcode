# Nesting 
# If Inside If

x = int(input("Enter the Number : "))

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("But not above 20.")