# Input:987654

# Output : 6

# n=int(input("Enter A Number : "))
# str1=str(n)
# count=len(str1)
# print(count)

n=int(input("Enter A Number : "))
count=0
i=n
while i>=1:
    i=i//10
    count+=1
print(count)



