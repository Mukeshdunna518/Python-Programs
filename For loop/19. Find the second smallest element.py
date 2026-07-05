l = [10, 20, 30,50,40]
smallest=l[0]
second =l[0]
for i in range(len(l)):
    if l[i]<smallest:
        second=smallest
        smallest=l[i]
    elif l[i]<second and l[i]!=smallest:
        second= l[i]
print(smallest)
print(second)

