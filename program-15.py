#  Find the first non-repeating character
# text
# Input: programming
# Output: p

input="programming"
duplicate=""
for i in input:
    if (input.count(i)==1):
        print(i)
        duplicate+=i
    break
    
