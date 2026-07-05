li=[2,2,5,8,11,14,17]
print(li)
n=int(input("Enter Element which you want Find count in given list : "))
count=0
for i in li:
    if i == n:
        count=count+1
print(count)
