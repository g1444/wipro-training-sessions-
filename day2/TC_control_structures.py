import keyboard
import time
num=4567
if num%2==0:
    print(num,"is even number")
else:
    print(num,"is a odd number")

marks=79
if marks >80:
    print('Grade A')
elif marks>=70:
    print("Grade B")
else:
    print("Fail")
k=5
i=0
while i!=k:
    print("kkk")
    i+=1

day=9
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("invalid")