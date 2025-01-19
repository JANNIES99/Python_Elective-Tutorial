num=int(input("Enter a number  :"))
if num<2:
    print(num)
else:
    num1 = num
    num2 = (num1 + (num/num1)) / 2
    while abs(num1 - num2) >= 0.00001:
        num1 = num2
        num2 = (num1 + (num/num1)) / 2
    print(num2)