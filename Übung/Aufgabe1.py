# Schreibe ein Programm, dass ermittelt, ob ein Jahr ein Schaltjahr ist.
# 1. Jahr muss durch 4 teilbar sein. 
# 2. Ist das Jahr durch 100 teilbar, ist es kein Schaltjahr. 
# 3. Ist das Jahr 400 teilbar, ist es trotzdem ein Schaltjahr.

leap_year = False

def check_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False



print("Leap Year Checker")

while True:

    user_input = int(input("Please enter a year (yyyy): "))

    leap_year = check_year(user_input)

    if leap_year == True:
        print(f"{user_input} is a leap year")
    else:
        print(f"{user_input} is not a leap year")