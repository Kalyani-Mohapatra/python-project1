#Take a string and convert every alternate character into uppercase.
str=input("Enter a string: ")
str2=""
for i in range(len(str)):
    if i%2==0:
        str2+=str[i].upper()
    else:
        str2+=str[i]

print(f"The converted string is {str2}.")
