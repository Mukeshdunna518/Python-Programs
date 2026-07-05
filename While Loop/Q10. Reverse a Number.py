# n=int(input("Enter Number :"))
# str1=str(n)[::-1]
# print(int(str1))

# n=int(input("Enter Number : "))
# rev=0
# i=n
# while i>=1:
#     dig=i%10
#     i=i//10
#     rev= rev*10 + dig
# print(rev)

n=int(input("Enter Number : "))
rev=0
while n>=1:
    dig=n%10
    n=n//10
    rev= rev*10 + dig
print(rev)
# for i in str(rev):
#     print(int(i))


n=int(input("Enter Number : "))
rev=0
i=n
while i>=1:
    dig=i%10
    i=i//10
    rev= rev*10 + dig
print(rev)
