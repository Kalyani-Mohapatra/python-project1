# write a program, by using import time to get present time for wising user good morning, goodafternoon, good evening, good night.

import time 
present_time=time.strftime('%H:%M:%S')
print(f"The current time is: {present_time}")
Time=int(time.strftime('%H'))
print(f"The current hour is: {Time}")
if 4<=Time<12:
    print("Hello, Good Morning!! Have a great day.")
elif 12<=Time<16:
    print("Hello,Good Afternoon") 
elif 16<Time<20:
    print("Hello, Good Evening") 
elif 20<Time<24:
    print("Hello, Good Night") 
else:
    print("Hello,Take care")           


print("Thank you")
