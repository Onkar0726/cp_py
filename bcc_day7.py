# Description program
# SecretMessage agency provides message encoding and decoding services for secure data transfer. 
# The first step in decoding includes removal of special characters and the whitespaces from the message, 
# as special characters and whitespaces do not hold any meaning
# Write an algorithm to help the agency find the number of special characters and whitespaces in a given message

# Input
# The input consists of a string message, representing the message that need to be decoded by the agency

# import re
# var = 'gasgg54@#vscsd!s*'
# count =0
# for i in var :
#     # z = re.findall('[a-z,0-9]',i)
#     z =ord(i)
#     # print(z)
#     #if z:
#     if z>97 and z>=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1
# print(count)
#-----------------------------------------------------------------------------------------------------------------------------
#wap find intersection of three array
#question:- find the common element in three array
#---------------------------------------------------------------------------------------------------
#wap move zero to the end
#given an array, move all the zeros to the end without changing the order of non-zero element

# arr = [0, 1, 0, 3, 12]
# for i in arr:
#     if i == 0:
#         arr.remove(i)
#         arr.append(i)
# print(arr)
#----------------------------------------------------------------------------------------------
#wap find the second largest element in the array
# arr = [5, 2, 9, 7, 5, 6]
# arr.sort() 
# print(arr)                   
# print(arr[-2])  
#---------------------------------------------------------------------------------------------
# wap                               
# N = int(input())
# sum = 0
# mylist = []  # 10,11,7,12,14

# N = int(input("Enter number of elements: "))

# for i in range(N):
#     a = int(input("Enter a value: "))
#     mylist.append(a)

# for j in range(len(mylist)):
#     if j+1 < len(mylist):   # fixed condition
#         sum = sum + abs(mylist[j] - mylist[j+1])

# print(sum)

