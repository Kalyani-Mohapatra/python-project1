#  Remove duplicate characters
# text
# Input: programming
# Output: progamin

input="programming"
duplicate=""
for i in input:
    if i not in duplicate:
        duplicate+=i
print(duplicate)