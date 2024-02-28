inputString = "aeroplanp"
vowels = "aeiou"
outputString = ""
for i in range(len(inputString)):
    if(i==len(inputString) and inputString[i] not in vowels):
        outputString += inputString[i]
    elif(inputString[i] in vowels and inputString[i+1] in vowels):
        outputString+=inputString[i]+inputString[i+1]
    elif(inputString[i] not in vowels):
        outputString += inputString[i]
print(outputString)
