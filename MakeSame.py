containers = [46]
TotalUnits = sum(containers)
OutputUnit = TotalUnits/len(containers)
Checker = True
for i  in range(len(containers)-1):
    if(containers[len(containers)-1] > OutputUnit):
        print("No")
        break
    elif(containers[i] > OutputUnit):
        RemWater = containers[i] -OutputUnit
        for j in range(i+1,len(containers)):
            if(containers[j]<OutputUnit):
                while(RemWater!=0):
                    containers[j]+=1
                    RemWater-=1
                    containers[i]-=1
                    if(containers[j]==OutputUnit):
                        break
        if(RemWater!=0):
            print("No")
            Checker = False
if Checker:
    print("Yes")
else:
    print("No")