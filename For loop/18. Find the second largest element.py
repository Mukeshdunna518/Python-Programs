# l = [10, 20, 30,50,40]
# largest=l[0]
# second =l[0]
# for i in range(len(l)):
#     if l[i]>largest:
#         second=largest
#         largest=l[i]
#     elif l[i]>second and l[i]<largest:
#         second= l[i]
# print(largest)
# print(second)



li=[2,2,5,8,11,14,17,17]
smallest=li[0]
largest=li[0]
for i in range(len(li)):
    if li[i]>largest:
        largest=li[i]
    elif li[i]<smallest:
        smallest=li[i]
print(f"Maximum : {largest} and Minimum :{smallest}")
