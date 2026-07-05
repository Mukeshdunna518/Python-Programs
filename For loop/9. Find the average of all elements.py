print("-----First Way-----")
li=[2,5,8,11,14,17]
sum=0
length=len(li)
for i in li:
    sum=sum+ i
    avg= sum/length
print("Average :",avg)


print()

print("-----Second Way-----")
#By Using index
li=[2,5,8,11,14,17]
sum=0
length=len(li)
for i in range(length):
    sum=sum+li[i]
    avg= sum/length
print("Average :",avg)