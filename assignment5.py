#Prof. Rajyaguru is working on creating encryption techniques to encrypt the messages he sends to his colleague.
#He encrypts the message by following procedure
#-He replaces all the spaces in message by '*' character.
#-He takes characters of message and puts it in a grid of K columns(where K > 1).
#-He fills remaining character in a grid by '$' character
#-He then reads the message by column wise and from the bottom of the grid.
#Write a program to perform above task

k=int(input("Number of columns:"))
string=input("enter a string:")
string=string.replace(" ","*")
list1=list(string)
if len(list1)%k!=0:
    for i in range(len(list1)%k):
        list1.insert(len(list1),"$")
i=0
while i<k:
    j=len(list1)-k+i
    while j<=len(list1)-1 and j>=0:
        print(list1[j],end="")
        j-=k
    i+=1

