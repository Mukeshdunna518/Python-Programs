li=[2,2,5,8,11,14,17,17]
smallest=li[0]
for i in range(len(li)):
    if li[i]<smallest:
        smallest=li[i]
print(smallest)


li=[2,2,5,8,11,14,17,17]
smallest=li[0]
for i in li:
    if i<smallest:
        smallest=i
print(smallest)

