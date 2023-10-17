# python program to find all lucky numbers before N

# take number input
num = int(input("Enter number: "))

# create list and fill it with numbers from 1 to num
arr = [i+1 for i in range(num)]

# loop to find the lucky number
for step in range(2, num//2):
    count = 0
    for i in range(num):
        # count is used to get the correct non-zero element
        if arr[i] != 0:
            count += 1
        # if count is divisible by step, then change the element to 0
        if count % step == 0:
            arr[i] = 0

# print the lucky number
for i in range(num):
    if arr[i] != 0:
        print(arr[i], end=" ")
print()
