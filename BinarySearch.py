Numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
Key = 17
First = 0
last = len(Numbers)
while(First<=last):
    Middle = (First+last)//2
    if(Middle==Key):
        print("Number Found")
        break
    elif(Key<Middle):
        last = Middle-1
    elif(Key>Middle):
        First = Middle+1
    
        