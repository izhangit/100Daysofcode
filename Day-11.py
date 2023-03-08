# How many seconds in a year!

leapyear = input("Is this year a leap year?: ") 
if leapyear == "Yes" or leapyear == "yes":
    minute = 1*60
    hour = minute*60 
    day = hour*24
    year = day*366
    
    print("there are",year,"seconds in one year") 
else:
    minute = 1*60
    hour = minute*60
    day = hour*24
    year = day*365

    print("there are",year,"seconds in one year")
