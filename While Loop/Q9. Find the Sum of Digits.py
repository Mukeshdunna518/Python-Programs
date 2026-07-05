n=int(input("Enter Number: "))
sum=0
i=n
while i>=1:
    dig = i % 10      
    sum += dig        
    i //= 10         
print(sum)

