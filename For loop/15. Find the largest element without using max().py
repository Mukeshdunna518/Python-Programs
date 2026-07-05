li=[2,2,5,8,11,14,17,17]
largest=li[0]
for i in range(len(li)):
    if li[i]>largest:
        largest=li[i]
print(largest)



li=[2,2,5,8,11,14,17,17]
largest=li[0]
for i in li:
    if i>largest:
        largest= i
print(largest)