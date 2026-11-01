# Capitalize the first letter of every word without using title()
# text
# Input: python programming language
# Output: Python Programming Language

Input="python programming language"
words=input.split()
result=""
for i in words:
    i=i.capitalize()
    result +=i+" "

print(result)    