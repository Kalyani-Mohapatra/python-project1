# Reverse a string without using slicing
# Input: Python
# Output: nohtyP
txt="python"
reverse=" "
# for i in txt:
#     reverse= i+reverse

# print(reverse)

for i in range(len(txt)-1,-1,-1):
    
    reverse+=txt[i]
print(reverse)    