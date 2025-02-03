list=[]
while True:
    num=int(input("Enter a number:"))
    list.append(num)
    contin=input("Do you wish to continue(y/n):")
    if contin.lower() !="y":
        break

if len(list)<2:
    print("Less than 3 elements")

else:
    # num=max(list)
    # list.remove(num)
    # num=max(list)
    # list.remove(num)
    # thirdLargest=max(list)
    # print("The third largest element:",thirdLargest)
    list.sort(reverse=True)
    thirdLargest=list[2]
    print("The third largest element:",thirdLargest)