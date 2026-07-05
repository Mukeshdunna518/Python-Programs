li=[2,2,5,8,11,14,17,17]
smallest=li[0]
largest=li[0]
for i in range(len(li)):
    if li[i]>largest:
        largest=li[i]
    elif li[i]<smallest:
        smallest=li[i]
print(f"Maximum : {largest} and Minimum :{smallest}")