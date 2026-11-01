# Check whether two strings are anagrams
# Anagrams contain the same characters in a different order.
# text
# String 1: listen
# String 2: silent
# Output: Anagram

str1="listen"
str2="silent"
list1=sorted(str1) #it's an built-in method like (len)
list2=sorted(str2)
if list1==list2:
    print("It's an Anagram .")
else:
    print("It's no an anagram")    
