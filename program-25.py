# Find the most frequently occurring character
# text
# Input: programming
# Output: Most frequent character: r

Input="programming"
result=""
max_fre=0
for i in Input:
    fre=Input.count(i)
    if fre>max_fre:
        max_fre=fre
        result=i
        
print(f"Most frequent character :{result}")        