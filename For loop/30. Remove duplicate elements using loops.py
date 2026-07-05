li=list(eval(input("Enter list : ")))
new=[]
for i in li:
    if i not in new:
        new.append(i)
print(new)

# li=list(eval(input("Enter list : ")))
# new=[]
# for i in li:
#     if i not in new:
#         new.append(i)
# largest=new[0]
# second=new[0]
# for i in new:
#     if i>largest:
#         second=largest
#         largest=i
#     if i>second and i<largest:
#         second=i
# print(largest)
# print(second)

# a=3
# b=4
# c=1
# li=list([a,b,c])
# li.remove(max(li))
# print(f"Second Largest is {max(li)}")


a=3
b=4
c=1
if a<b and a>c:
    print(a,"Second Largest")
elif b<a and b<c:
    print(b,"Second Largest")
else:
    print(c,"Second Largest")


