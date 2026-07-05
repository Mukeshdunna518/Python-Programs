# Spy Number
# strong Number
# perfect number or not
# neon number

n=int(input("Enter Number: "))
sum=0
pro=1
i=n
while i>=1:
    dig = i % 10      
    sum += dig 
    pro=pro*dig       
    i //= 10
    if sum==pro:
        print("Spy Number")
        break
else:
    print("Not Spy Number")

