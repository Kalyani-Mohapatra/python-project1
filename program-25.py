# Find the most frequently occurring character
# text
# Input: programming
# Output: Most frequent character: r

Input="programming"
result=""
for i in Input:
    if Input.count(i)==2:
        result+=i
        break
print(f"Most frequent character :{result}")        