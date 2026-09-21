# match case
number=int(input("Enter a number: "))

match number:
      case 1:
            print("Today is Monday")
      case 2:
            print("Today is Tuesday")
      case 3:
            print("Today is Wednesday")
      case 4:
            print("Today is Thursday")
      case 5:
            print("Today is Friday")
      case 6:
            print("Today is Saturday") 
      case 7:
            print("Today is Sunday")
      case _:
            print("This is invalid number.")                       
