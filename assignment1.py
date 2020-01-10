#Write a python program that takes two numbers as command line argument and display whether
#they are amicable numbers or not.
#Amicable numbers are pair of
#numbers such that sum of all proper divisor of the first number (excluding number itself) exactly
#equal to the second number and sum of all proper divisor of the second number(excluding number
#itself) exactly equals to the first number.

x=input("enter first number:")
y=input("enter second number:")
if(x=="" or y==""):
    print("missing required inputs")
else:
    x=int(x)
    y=int(y)
    divisor_x=[]
    divisor_y=[]
    for i in range(1,(x//2)+1):
        if (x%i==0):
            divisor_x.append(i)
    for i in range(1,(y//2)+1):
        if(y%i==0):
            divisor_y.append(i)
    sum_x=0
    sum_y=0
    for i in divisor_x:
        sum_x+=(i)
    for i in (divisor_y):
        sum_y+=(i)
    if(sum_x==y and sum_y==x):
        print("{} and {} are Amicable Numbers".format(x,y))
    else:
        print("{} and {} are not amicable numbers".format(x,y))