N = int(input())
sum = 0
mylist = []  # 10,11,7,12,14

N = int(input("Enter number of elements: "))

for i in range(N):
    a = int(input("Enter a value: "))
    mylist.append(a)

for j in range(len(mylist)):
    if j+1 < len(mylist):   # fixed condition
        sum = sum + abs(mylist[j] - mylist[j+1])

print(sum)