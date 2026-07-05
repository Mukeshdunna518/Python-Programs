# li=[2,5,8,11,14,17]
# count=0
# for i in li:
#     if i%2==1:
#         count=count+1
# print(count)


# By using Index

li=[2,5,8,11,14,17]
count=0
for i in range(len(li)):
    if li[i]%2==1:
        count=count+1
print(count)