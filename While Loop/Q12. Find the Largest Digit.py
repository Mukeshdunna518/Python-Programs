# n=int(input("Enter Number :"))
# li=list(str(n))
# largest=eval(max(li))
# print(largest)

# n=int(input("Enter Number :"))
# largest=0
# i=n
# while i>=1:
#     digit=i%10
#     if digit>largest:
#         largest=digit
#     i=i//10
# print(largest)


n=int(input("Enter Number :"))
largest=0
while n>=1:
    digit=n%10
    if digit>largest:
        largest=digit
    n=n//10
print(largest)


