#  Find the first non-repeating character
# text
# Input: programming
# Output: p

input="programming"
duplicate=""
for i in input:
    if (input.count(i)==1):
        print(i)
        duplicate+=i
        break  # brebreak indented inside if → stops only when the condition is satisfied.

#break aligned with if → stops after the first loop iteration, regardless of the condition.
    