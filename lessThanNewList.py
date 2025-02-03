list=[]
while True:
    num=int(input("Enter a number:"))
    list.append(num)
    contin=input("Do you wish to continue(y/n):")
    if contin.lower() !="y":
        break

X=int(input("Enter the value of X:"))

list2=[]
for i in list:
    if i<X:
        list2.append(i)


print("The new list is:",list2)
