startingAmount=float(input("Enter the starting amount:"))
years=int(input("Enter the number of year:"))
interestRate=float(input("Enter the rate of interest:"))

endingAmount=startingAmount
interest=startingAmount*interestRate/100

print("Year\tStarting Amount\tEnding Amount\tInterest")

for i in range(1,years+1):
    endingAmount+=interest
    print(i,"\t",startingAmount,"\t",endingAmount,"\t",interest)

print("The Amount at the end of",years,"years is",endingAmount)
print("The interest earned is",endingAmount-startingAmount)
