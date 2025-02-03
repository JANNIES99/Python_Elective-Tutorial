list=[]
while True:
    num=int(input("Enter a number:"))
    list.append(num)
    contin=input("Do you wish to continue(y/n):")
    if contin.lower() !="y":
        break

# largest=max(list)
# smallest=min(list)
largest=list[0]
smallest=list[0]

for i in list:
    if largest<i:
        largest=i
    if smallest>i:
        smallest=i

print("The largest element:",largest)
print("The smallest element:",smallest)