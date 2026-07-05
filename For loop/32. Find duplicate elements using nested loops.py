li=list(eval(input("Enter list : ")))
new=[]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] == li[j] and li[i] not in new:
            new.append(li[i])
print(new)