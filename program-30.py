#Count how many times a particular character appears in a string without using count().
str=input("Enter a sring: ")
str2=input("Enter a character: ")
char=0 # becoz our expected output is to find the occurrance of a perticular character 
for i in range(len(str)):
    if str2.lower()== str[i].lower(): # this makes the string casesensitive 
        char+=1 # this +=1 count the total occurrance 
if char>0: 
    print(f"The no of occerrance is {char}.")
else:
    print("It's not in the string.")    
#print(f"The final output is {char}.")        