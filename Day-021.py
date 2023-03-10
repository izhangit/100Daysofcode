# Math Facts Game!

print("Math Game")
n = int(input("Enter multiple: "))
score = 0
for i in range(10):
    ask = int(input(f'{i} x {n} = '))
    if ask == i*n:
        print("Correct Answer!")
        score += 1
    else:
        print(f'Incorrect answer! the correct ans is {i*n}')
        print(f'Your score is {score} out of 10')
