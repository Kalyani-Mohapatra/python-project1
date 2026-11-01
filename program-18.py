# Level 2: Advanced string logic
# 9. Find the longest word in a sentence
# text
# Input: Python is a powerful programming language
# Output: programming

input="Python is a powerful programming language"
words=input.split()
length=""
for i in words:
    if len(i)>len(length):
        length =i
# break
print(length)        


