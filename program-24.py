# Remove all special characters from a string
# text
# Input: Hello@123#Python!
# Output: Hello123Python

input="Hello@123#Python!"

result=""
for i in input:
    if i.isalnum():
        result+=i
print(result)    
