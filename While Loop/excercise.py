# n=int(input("Enter Number : "))
# i=1

# while i<=n:
#     j=i
#     while j<=n:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1

# output:
# Enter Number : 5
# 12345
# 2345
# 345
# 45
# 5

# n=int(input("Enter Number : "))
# i=1

# while i<=n:
#     j=1
#     while j<=n:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1

# output:
# Enter Number : 5
# 12345
# 12345
# 12345
# 12345
# 12345

# n=int(input("Enter Number : "))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1
# output:
# Enter Number : 5
# 11111
# 22222
# 33333
# 44444
# 55555

# while True:
#     age=int(input("Enter Age: "))
#     if age>0 and age<=120:
#         print("Valid Input")

# while True:
#     char=input("Enter character :")
#     if char in "AEIOUaeiou":
#         print("Vowel Detected")
#         break


# n=int(input("Enter Number :"))
# i=1
# while i<=n:
#     print(i**2,end=" ")

#     i=i+1


while True:
    str1=input("Enter String : ")
    if len(str1)>=6:
        print("Username accepted")
        break

# x="Mukesh"
# if x:
#     print("True")
# else:
#     print("False")


n=int(input("Enter Number :"))
while True:
    if n%3==0 and n%7==0:
        print(n)
        break
    n=n+1
