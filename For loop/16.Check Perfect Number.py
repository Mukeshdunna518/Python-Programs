n=int(input("Enter Number :"))
num=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==num:
    print("Perfect Number")
            

