# n=int(input("Enter Number : "))
# i=2
# if n<=1:
#     print("Prime Number Is always Greaterthan 1")
# else:
#     if n%i==0 and i*i<=n:
#         print("Not A Prime")
#     else:
#         print("It's a prime Number")
  
n=int(input("Enter Number : "))
n1=int(input("enter Second number:"))
for j in range(n,n1):
    if j==1:
        continue;
    count=0
    for x in range(2,j):
        if j%x==0:
            count+=1
            
    if count == 0:
        print(j)

    
  
  

