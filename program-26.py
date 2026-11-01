# 17. Password strength checker
# Ask the user to enter a password and check whether it contains:
# At least 8 characters
# One uppercase letter
# One lowercase letter
# One digit
# One special character
# Example:
# text
# Enter password: Python@123
# Password strength: Strong

password=input("enter  Password:")
upper=False
lower=False
digit=False
special=False
# if (len(password)>=8):
for i in password:
    if i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i.isdigit():
        digit=True
    elif not i.isalnum():
        special=True
if (len(password)>=8 and upper and lower and digit and special) :
    print("Strong")

else:
    print("Enter strong password")    

            

             

    

