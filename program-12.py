# Input: madam
# Output: Palindrome

txt="python"
reverse=""
# for i in range(len(txt)-1,-1,-1):
#     reverse+=txt[i]
for i in txt:
    reverse=i+reverse    
print(reverse)  
if reverse==txt:
    print("It's an palindrome word")
else:
    print("error")    
   