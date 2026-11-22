#Remove all vowels from a given string.
str=input("Enter a string: ")
str2=""
for i in range(len(str)):
    
    if str[i].lower() not in "aeiou":
        str2+=str[i]
       
   
print(f"The final srting is {str2}.")  

