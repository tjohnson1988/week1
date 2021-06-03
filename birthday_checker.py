#Take a users input and return their name + birthday. If today is there
# birthday output “Happy Birthday!”

#test interpreter (this was giving me a major headache)
name = input("Enter your name:")
print(name)
birth_month = input("Enter your birth month (01-12):")
print(birth_month)
birth_day = input("Enter your day of birth:")
print(birth_day)
birth_year = input("Enter your birth year:")

print("Hi", name + ". Your birthday is", birth_month + "-" + birth_day + "-" + birth_year + ".")