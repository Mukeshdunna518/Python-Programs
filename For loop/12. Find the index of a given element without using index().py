li=[2,2,5,8,11,14,17]
print(li)
n=int(input("Enter Element which you want to Find index in given list : "))
for i in range(len(li)):
    if li[i] == n:
        print(i)


# li=[2,2,5,8,11,14,17]
# print(li)
# n=int(input("Enter Element which you want to Find index in given list : "))
# i=0
# while i< len(li):
#     if li[i] == n:
#         print(i)
#     i=i+1

# li=[2,2,5,8,11,14,17]
# print(li)
# n=int(input("Enter Element which you want to Find index in given list : "))
# i=0
# while i<=len(li):   # <-- problem
#     if li[i] == n:
#         print(i)
#     i=i+1

# Why <= len(li) is wrong
# len(li) = 7 (because there are 7 elements).

# Valid indices go from 0 to 6.

# When i = 7, the loop condition i <= len(li) is still true, so Python tries li[7] → IndexError.

# That’s why we must use:

# python
# while i < len(li):
# This ensures the loop runs for indices 0, 1, 2, 3, 4, 5, 6 only.

# Why it still works when i = 0
# Don’t worry — using < len(li) does not skip index 0.

# At the start, i = 0.

# Condition: 0 < 7 → True.

# Loop runs, checks li[0].
# So index 0 is included correctly.