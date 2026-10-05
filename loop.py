# x = ["ffhfue",1,4.57,4,"hfdjdv"]
# for i in x:
#     print(i)

# x = "sohomishika"
# for i in x:
#     print(i,end = '')
#     print()

# sum = 0
# for i in range(0,11):
#     if i%2 == 0:
#         sum = sum+i
# print(sum) 

# x = int(input("enter the number:"))
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" ",end = '')
#     print("*",end = '')
#     print()

# n = 6
# for i in range(n):
#     for j in range(i,n):
#         print("*",end = ' ')
#     print() 

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end = ' ')
#     for j in range(i+1):
#         print("*",end = ' ')
#     print()
    
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ",end = ' ')
#     for j in range(i,n):
#         print("*",end = ' ')
#     print()

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end = ' ')
#     for j in range(i+1):
#         print("*",end = ' ')
#     for j in range(i):
#         print("*",end = ' ')
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end = ' ')
#     for j in range(i,n):
#         print("*",end = ' ')
#     for j in range(i,n-1):
#         print("*",end = ' ')
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end = ' ')
#     for j in range(i):
#         print("*",end = ' ')
#     for j in range(i+1):
#         print("*",end = ' ')
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=' ')
#     for j in range(i,n-1):
#         print("*",end=' ')
#     for j in range(i,n):
#         print("*",end=' ')
#     print()


# while loop

# n=1
# while n <= 100:
#     print(n)
#     n+=1

# n = int(input("enter number:"))
# i = 1
# while i<=10:
#     print(n*i)
#     i += 1

# list = [1,4,9,16,25,36,49,64,81,100]
# index = 0
# while index <= len(list)-1:
#     print(list[index])
#     index += 1
 
tup = (1,4,9,16,25,36,64,81,100,)
x = 36
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("found at index",i)
        break
    else:
        print("finding...")
    i += 1