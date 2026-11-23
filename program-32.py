# Expand a compressed string.
# Input: a3b2c4

# Output: aaabbcccc

s = "a3b2c4"

result = ""

i = 0

while i < len(s):

    alpha = s[i]
    num = s[i+1]

    result += alpha * int(num)

    i += 2

print(result)

# str=a3b2c4
# str2=""
# for i in range(len(str)):
#     if str[i].isalpha():
#         str2+=str[i]


