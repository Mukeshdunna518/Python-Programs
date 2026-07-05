# n=int(input("Enter Number :"))
# i=n
# arm=0
# count=len(str(n))
# while n>0:
#     digit=n%10
#     arm=arm+digit**count
#     n=n//10
# if arm ==i:
#     print("Arm")
# else:
#     print("Not Arm")


# n=int(input("Enter Number :"))
# i=n
# arm=0
# count=0
# j=n
# while j>=1:
#     j=j//10
#     count=count+1
# while n>=1:
#     digit=n%10
#     arm=arm+digit**count
#     n=n//10
# if arm ==i:
#     print("Arm")
# else:
#     print("Not Arm")


# n=int(input("Enter Number :"))

# i=n
# arm=0
# count=0
# j=n
# while j>=1:
#     j=j//10
#     count=count+1
# while n>=1:
#     digit=n%10
#     arm=arm+digit**count
#     n=n//10
# if arm ==i:
#     print("Arm")
# else:
#     print("Not Arm")

# n=int(input("Enter Number : "))
# n1=int(input("enter Second number:"))
# for j in range(n,n1):
#     if j==1:
#         continue;
#     count=0
#     for x in range(2,j):
#         if j%x==0:
#             count+=1
            
#     if count == 0:
#         print(j)


# odd=0
# even=0
# def even_odd():
#     for i in range(1,num+1):
#         if i%2==0:
#             even=even+1
#         else:
#             odd=odd+1
# print("Even Numbers count ",even)
# print("odd Numbers count ",odd)
# num=int(input("Enter Number :"))
# even_odd()


# a,b=3,2
# a=8

# print(a)
# print(b)

# You can also use * to capture “the rest”:

# numbers = [1, 2, 3, 4,2,5]
# a, *b, c = numbers
# print(a)   # 1
# print(b)   # [2, 3, 4]
# print(c)   # 5

# t = (1, 2, 3)
# t = t + (4)   # create a new tuple
# print(t)       # (1, 2, 3, 4)
