#Find the last occurrence of a particular character in a string.
str=input("Enter a string: ")
str2=input("Enter a character: ")
occ=-1
for i in range(len(str)):
    if str2.lower()==str[i].lower():
        occ=i
if occ>-1:
    print(f"The last occurrance is {occ}.")      
else:
    print("Character is not found")

