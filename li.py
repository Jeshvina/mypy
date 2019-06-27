a=int(input())
b=int(input())
for i in range((a+1),b):
    flag=0
    if(i>2):
        for j in range(2,i):
            if((i%j)==0):
                flag=1
                break
    else:
        print(i)
    if(flag==0):
        print(i)
