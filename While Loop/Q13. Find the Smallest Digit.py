# n=int(input("Enter Number :"))
# li=list(str(n))
# smallest=eval(min(li))
# print(smallest)

n=int(input("Enter Number : "))
smallest=9 # start with the largest possible digit... because(0-9)
i=n
while i>=1:
    digit=i%10
    if digit < smallest:
        smallest=digit
    i=i//10
print(smallest)