#Mr. Ramesh is a bank manager and is handling many branches of a bank. Frequently he wants to
#know the overview of a specific branch.
#He needs following information frequently.
#1) How many accounts are there in a branch.
#2) Average balance of all accounts in a branch
#3) Highest balance among all accounts in a branch.
#4) Lowest balance among all account in a branch.
#Write a program which takes branch name as an input and display summary as above.
#- If user does not provide a branch name then display : "Missing required inputs"
#- If user provides a branch name which does not exist in a file then display : "No such branch"
#- display balance precise to 2 decimal point.

file = open("accounts.txt", "r")
account_number=[]
branch_name=[]
balance=[]
fields=[]
sum=0
list_balance=[]
for line in file:
    fields=line.split(" ")
    account_number.append(fields[0])
    branch_name.append(fields[1].lower())
    balance.append(fields[2])
branch_name2=set(branch_name)
branch=input("enter branch name:").lower()
if branch=="":
    print("missing required inputs")
elif branch.lower() not in branch_name2:
    print("no such branch")
else:
    for i in range(len(account_number)):
        if(branch_name[i]==branch):
            list_balance.append((balance[i]))
            sum+=eval(balance[i])
    average=round(sum/len(list_balance),2)
    for i in range(len(list_balance)-1):
        if list_balance[i]>list_balance[i+1]:
            list_balance[i],list_balance[i+1]=list_balance[i+1],list_balance[i]
    print("Total Account:{}".format(len(list_balance)))
    print("Average Balance:{}".format(average))
    print("Highest Balance:{}".format(list_balance[len(list_balance)-1]))
    print("Lowest Balance:{}".format(list_balance[0]))