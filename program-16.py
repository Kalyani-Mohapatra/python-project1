# Find the first repeating character
# Input: programming
# Output: r

input="Programming"
duplicate=""
for i in input:
    if (input.count(i)==2):
        # duplicate+=i  #+= i → Adds the current character or word to the existing string. It keeps collecting.
                        # = i → Replaces the previous value with the current character or word.
                        # here both duplicate will give the same output
        duplicate=i
        break        
print(duplicate)    
