# What grade did I get?

import time

print("This program will generate grade according percentage of exam.")
time.sleep(1)
print("")
time.sleep(1)
name_of_exam= input("Please, type the name of exam subject: ")
time.sleep(1)
print("")
max_possible_score = int(input("Input the maximum possible score of the exam: "))
time.sleep(1)
print("")
your_score = int(input("Write your score of the exam: "))
time.sleep(2)
print("")
grade_in_percentage = round((your_score * 100)/max_possible_score,2)

print(grade_in_percentage) 
grade = (" ")
if grade_in_percentage >= 90:
    print (grade="AA")

    if grade_in_percentage >= 80: print (grade = "A")

    if grade_in_percentage >= 70: print (grade ="B")

    if grade_in_percentage >= 60:
        print(grade="C")

    if grade_in_percentage >= 50:

        print(grade = "D")

    if grade_in_percentage >= 40: 
        print (grade = "U")
        print("Exam Grade generator")

time.sleep(1)

print("Name of the exam subject: " + name_of_exam)

time.sleep

print("Max. Possible score" + str(max_possible_score))

time.sleep(1)

print("Your score is: "+ str(your_score)) 

time.sleep(1)

print("Your got " + str(grade_in_percentage) +"%, "+"which is a grade " + grade)
