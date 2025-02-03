print("Enter the element of the first list")
list1=[]
while True:
    num=int(input("Enter a number:"))
    list1.append(num)
    contin=input("Do you wish to continue(y/n):")
    if contin.lower() !="y":
        break

print("Enter the element of the second list")
list2=[]
while True:
    num=int(input("Enter a number:"))
    list2.append(num)
    contin=input("Do you wish to continue(y/n):")
    if contin.lower() !="y":
        break

list3=[]

for i in list1:
    if i in list2:
        list3.append(i)

print("The new list is:",list3)