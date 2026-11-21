#Take a string from the user and count the total number of uppercase and lowercase letters.
str=input("Enter a string: ")
upper=0
lower=0
for i in str:
    if i.isupper():
        upper+=1
    else:
        i.islower()
        lower+=1   
print(f"The total number of uppercase & lowercase are{upper} & {lower}")        