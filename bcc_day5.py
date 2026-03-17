#nested for loop
# for i in range(1, 4): #outer loop => rows
#     for j in range(1, 4): #inner loop => columns
#         print("i", end=" ")
#         print() 

# n=int(input("Enter the number of rows: ")) #5
# for i in range(1, n+1): #i=1
#     for j in range(1, i+1): #j=2
#         print(chr(64+i,end=" ")) #ASCII
#     print() 

# n = int(input("Enter number of rows: "))
# for i in range(1,n+1): 
#         for j in range(1,n+2-i):
#             print("*",end=" ")
#         print() 
    
#function
# def add(): # called function
#     n1 = int(input("Enter the value of n1:"))
#     n2 = int(input("Enter the value of n2:"))
#     print("Add=", n1+n2)
    
# add()

#how to return multiple value
# def add(): # called function
#     n1 = int(input("Enter the value of n1:"))
#     n2 = int(input("Enter the value of n2:"))
#     sum = n1+n2
#     mul = n1*n2
#     sub = n1-n2
#     div = n1/n2
#     return sum, sub, mul, div

# result = add()
# print(result)

#positional argument
# def personalInfo(fname, lname):
#     print("First Name:", fname)
#     print("Last Name:", lname)
    
# personalInfo("Samruddhi", "Sawarkar")

#keyword argument
# def personalInfo(fname, lname):
#     print("First Name:", fname)
#     print("Last Name:", lname)
    
#     fname ="Samruddhi"
#     lname ="Sawarkar"
#     personalInfo(fname, lname)

#default argument
# def cityName(city="Nagpur"):
#     print(city)
    
# cityName("Mumbai")
# cityName("Delhi")
# cityName()

#variable length argument
# def studentNames(*name):
#     print(name)
    
# studentNames("Samruddhi", "Ashish", "Sandip")

# mylist = [5,2,9,7,5,6]
# #search element 7
# n =len(mylist)
# print(n)


# mylist = [5,2,9,7,5,6]
# #search element 7
# def searchElement(target):
#     for i in range(len(mylist)): #mylist = 6
#         if target == mylist[i]:
#             print("Element found at index number =",i)
# searchElement(7) # 7 this element we have to search


# mylist = [5,2,9,7,5,6]
# #search element 7
# def searchElement(target):
#     for i in range(len(mylist)): #mylist = 6
#         if target == mylist[i]:
#             return i
#     return -1 
        
# result = searchElement(10) # 7 this element we have to search
    
# if result != -1:
#         print("Element found at index number =",result)
# else:
#         print("Element not found")