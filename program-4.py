# How to calculate birth year using datetime

from datetime import datetime
current_year=datetime.now().year
print(current_year)
birth_year=int(input("Enter your birth year: "))
age=current_year-birth_year
print(f"Your current age is {age}.")