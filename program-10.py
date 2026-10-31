# Take a string from the user and count:
# Total vowels
# Total consonants
# Total digits
# Total spaces

name=input("Enter a name: ")
vowels="aeiou"
v_count=0
c_count=0
d_count=0
s_count=0
for ch in (name):
    if ch in vowels:
        v_count+=1
    
    elif ch.isalpha():
        c_count+=1
    elif ch.isdigit():
        d_count+=1
    elif ch.isspace():
        s_count+=1        
print(f"vowels:{v_count}") 
print(f"Consonant:{c_count}")  
print(f"Digit:{d_count}")
print(f"Space:{s_count}")     