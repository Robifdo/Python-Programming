number = [24,70,3,55,48]
alphabets = "abcdefghijklmnopqrstuvwxyz"

for i in number:
    condition = True
    for firstNumber in range(1,27):
        if(condition):
            for SecondNumber in range(1,27):
                if(condition):
                    for ThirdNumber in range(1,27):
                        if((firstNumber+SecondNumber+ThirdNumber)==i):
                            outputString = alphabets[firstNumber-1]+alphabets[SecondNumber-1]+alphabets[ThirdNumber-1]
                            condition = False
                            print(outputString)
                            break
                else:
                    break
        else:
            break

        