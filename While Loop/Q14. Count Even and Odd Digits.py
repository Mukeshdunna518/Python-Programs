n=int(input("Enter Number : "))
odd=0
even=0
while n>=1:
    digit =n%10
    if digit %2==0:
        even=even+1
    else:
        odd=odd+1
    n=n//10
print(f"{even} Even digits and {odd} Odd digits are there in Given number")