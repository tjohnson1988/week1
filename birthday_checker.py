#Take a users input and return their name + birthday. If today is there
# birthday output “Happy Birthday!”

# use .strftime to formats dates in a specific manner
# https://www.programiz.com/python-programming/datetime
# https://www.youtube.com/watch?v=hj6Tgc4hEU0&ab_channel=CleverProgrammer

from datetime import datetime

current_day = datetime.now().day
#print(current_day)
current_month = datetime.now().month
#print(current_month)

name = input("Enter your name:")
#print(name)
birth_month = int(input("Enter your birth month (01-12):"))
#print(birth_month)
birth_day = int(input("Enter your day of birth:"))
#print(birth_day)
birth_year = input("Enter your birth year:")

if (current_day == birth_day) and (current_month == birth_month):
    print("Happy Birthday!")
else:
    print("Hi", name + ". Your birthday is", str(birth_month) + "-" + str(birth_day) + "-" + birth_year + ".")