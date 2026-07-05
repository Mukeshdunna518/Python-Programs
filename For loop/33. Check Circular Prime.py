
n=int(input("Enter Number: "))
string =str(n)
for i in range(len(string)):
    rot=string[i:]+string[:i]
    num=int(string)
    count=0
    for j in range(1,num+1):
        if num%j==0:
            count=count+1
            if count ==2:
                pass
print("It's a Circular Prime Number")