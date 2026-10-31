# Count the frequency of each character
# Input: programming
# p = 1
# r = 2
# o = 1
# g = 2
# a = 1
# m = 2
# i = 1
# n = 1
input="programming"
seen=""

for ch in input:
    if ch not in seen:
        print(ch,"=",input.count(ch))
    seen+=ch
    
   
       