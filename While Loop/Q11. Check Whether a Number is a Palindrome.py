# n=int(input("Enter Number :"))
# str1=str(n)[::-1]
# if n == int(str1):
#     print("It's a Palindrome")
# else:
#     print("It's Not a Palindrome")

n=int(input("Enter Number : "))
rev=0
i=n
while i>=1:
    dig=i%10
    i=i//10
    rev= rev*10 + dig
if n == rev:
    print("It's a Palindrome")
else:
    print("It's Not a Palindrome")

