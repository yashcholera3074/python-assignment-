#Maulik is a student in the department of Mathematics and Statistics. He is working on properties of
#a median of a set of numbers.
#He has set of distinct numbers and he wants to find out K numbers from that set which are closest
#to the median of the set of numbers.
#He wants all these K numbers in ascending order.
#The median of the set of number is found by following procedure:
#- Step1 First of all the numbers are sorted in ascending order
#- Step2.1 the total numbers in the set are odd then the median is the middle number in the set.
#- Step2.2 If the total numbers in the set are even then the median is the mean of two middle most numbers.
#Design a program which takes set of numbers and value of K as an argument and display K numbers
#which are closest to the median of the set of numbers.
#Restriction:
#- If while selecting K numbers, if you find two numbers which are equally closest to the median then
#select the lowest number out of those two numbers.
#- The numbers must be displayed in ascending order

num=eval(input("how many elements?"))
numbers2=[]
numbers=[]
median=0
for i in range(num):
    numbers2.append(input())

for i in numbers2:
    if i not in numbers:
        numbers.append(i)

numbers=list(map(int,numbers))
numbers=sorted(numbers)
print(numbers)

if(len(numbers)%2==0):
    median=(numbers[len(numbers)//2]+numbers[(len(numbers)//2)-1])/2
else:
    median=numbers[len(numbers)//2]
print("median is:",median)
diff=[]
for i in range(len(numbers)):
    if numbers[i]>median:
        diff.append(numbers[i]-median)
    else:
        diff.append(median-numbers[i])
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):

        if diff[i]>diff[j]:
            diff[i],diff[j]=diff[j],diff[i]
            numbers[i],numbers[j]=numbers[j],numbers[i]

for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if(diff[i]==diff[j] and numbers[i]>numbers[j]):
            numbers[j],numbers[i]=numbers[i],numbers[j]
k=eval(input("how many closet element you want to find?"))
closet=[]
for i in range(k):
    closet.append(numbers[i])
closet=sorted(closet)
for i in closet:
    print(i,end=" ")