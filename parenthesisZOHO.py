InputString = "HELLO AND WELCOME )(TO THE) TCEA (CONTEST)TODAY()IS (SATURDAY())"
braceCount = 0
for i in InputString:
    if i== "(":
        braceCount+=1
    elif i==")" and braceCount==0:
        braceCount+=1
        break
    elif i==")":
        braceCount-=1
if braceCount==0:
    print("Yes")
else:
    print("No")