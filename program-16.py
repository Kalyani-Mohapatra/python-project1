# Find the first repeating character
# Input: programming
# Output: r

input="Programming"
duplicate=""
for i in input:
    if (input.count(i)==2):
        duplicate+=i
        
        break        
print(duplicate)    
