input = [".@@*@.**@@",".@@..@***..@@@*",".@@@@"]
for i in input:
    ThronPosition = i.find("**")
    if(ThronPosition ==  None):
        print(i.count('@'))    
    else:
        NewString = i[:ThronPosition]
        print(NewString.count('@'))        