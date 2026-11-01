# Find the shortest word in a sentence
# text
# Input: I love learning Python programming
# Output: I

input="I love learning python programming"
words=input.split()
short=words[0]   #The important concept: We initially assume the first word is the shortest. As we go through the list, we replace it whenever we find a shorter word.  
for i in words:
    if len(i)<len(short):
        short =i

print(short)        