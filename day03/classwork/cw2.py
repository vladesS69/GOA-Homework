# number = int(input())
# for i in range(0, number):
#     print(i)


# num1 = int(input("შეიყვანეეთ რიცხვი: "))
# num2 = int(input("შეიყვანეეთ რიცხვი: "))

# if num1 % 2 == 0 and num2 % 2 == 0:
#     sum = num1 + num2
#     print("ჯამი არის: ", sum)
# else:
#     print("The given numbers are not even so they will not be summed")

# sa = "5"
# sb = "3"

# ia=5
# ib=3

# print(int(sa) + ib)

# ans1=int(sa) + ib
# print(ans1)
# print(type(ans1))
# ans2=sb+str(ia)
# print(ans2)
# print(type(ans2))

import random

def myfunc(a):
    x=random.randint(1,10)
    ans=x
    for i in range (a-1):
        ans*=x
    return ans

print(myfunc(2))











