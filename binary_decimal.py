binary=input("Enter the binary number:")
exponent=0
decimal=0
for i in range((len(binary)-1),-1,-1):
    decimal+=int(binary[i])*2**exponent
    exponent+=1

print(decimal)
