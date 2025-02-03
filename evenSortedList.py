list=[]
while True:
    num=int(input("Enter a number:"))
    list.append(num)
    contin=input("Do you wish to continue(y/n):")
    if contin.lower() !="y":
        break


list2=[]
for i in list:
    if i%2==0:
        list2.append(i)

list2.sort()
print("The new list is:",list2)