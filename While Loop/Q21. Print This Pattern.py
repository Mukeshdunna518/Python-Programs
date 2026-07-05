# Input :5

# Output
# 1
# 12
# 123
# 1234
# 12345
n=int(input("Enter Number : "))
i=1

while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1

# n = int(input("Enter Number: "))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(j, end="")  # print numbers on the same line
#         j += 1
#     print()  # move to the next line
#     i += 1
