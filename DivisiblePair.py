Array = [4,9,7,1,2,2,13,3,15]
x = 6
y = 2
BeautifulPair = 0
for i in range(len(Array)-1):
    for j in range(i+1,len(Array)):
        sum = Array[i]+Array[j]
        minus = Array[i]-Array[j]
        if(sum%x==0 and minus%y==0):
            BeautifulPair+=1
            print("sum ",sum," and minus ",minus)
print(BeautifulPair)
    