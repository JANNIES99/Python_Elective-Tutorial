income=int(input("Enter your income:"))
if income<250000:
    print("NILL")
elif income<500000:
    print("Your tax:",income*0.05)
elif income<1000000:
    print("Your tax:",income*0.2)
else:
    print("Your tax:",income*0.3)