income=int(input("Enter your income:"))
if income<300000:
    print("NILL")
elif income<700000:
    print("Your tax:",(income-300000)*0.05)
elif income<1000000:
    print("Your tax:",20000+(income-700000)*0.1)
elif income<1200000:
    print("Your tax:",50000+(income-1000000)*0.15)
elif income<1500000:
    print("Your tax:",80000+(income-1200000)*0.2)
else:
    print("Your tax:",140000+(income-1500000)*0.3)