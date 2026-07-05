li=[2,2,5,8,11,14,17,17]
n=int(input("Which element do you want to find firstoccurence index : "))
for i in range(len(li)-1,-1,-1):
    if li[i]==n:
        print(i)
        break