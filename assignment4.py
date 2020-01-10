#Manoj,compress the string by replacing same consecutive characters by its count as below:
# - string 'aaaabbbccc' can be stored as a4b3c3
# - string 'abcccdd' can be stored as abc3d2
#write a program which takes a compressed string as an input and decompress it
import re
from ast import literal_eval
string=input("enter compressed string:")
string=string.replace(" ","")
num=re.findall('\d+',string)
char=re.findall('[a-z]',string)
list1=list(string)
if(len(num)!=len(char)):
    for i in range(2*len(list1)):
        if i%2!=0:
            try:
                literal_eval(list1[i])
            except:
                list1.insert(i,"1")
        if i==len(list1)-1:
            try:
                literal_eval(list1[i])
                break
            except:
                list1.insert(i+1,"1")
                break

string=""
for ele in list1:
    string+=ele
num=re.findall('\d+',string)
char=re.findall('[a-z]',string)
i=0
while i<len(num):
    for j in range(eval(num[i])):
        print(char[i],end="")
    i+=1