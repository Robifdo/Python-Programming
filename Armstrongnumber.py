number = 158
DuplicateNumber = number
finalOutput = 0
for i in range(len(str(number))):
    Remainder = DuplicateNumber%10
    finalOutput += Remainder**(len(str(number)))
    DuplicateNumber = DuplicateNumber//10
if(finalOutput == number):
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
