# for i in range(0):   # output
#     print(i)

# for i in range(1):   # output:0
#     print(i)

# t = frozenset([1,2,5,4,1,2,3])
# for i in t:
#     print(i)

# n= int(input("enter : "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

# t = ["mehak","shaam","mehar"]
# for i in t:
#     if(i.startswith("m")):
#         print(f"helllo {i}")

# n= int(input("enter : "))
# i =1;
# while(i<11):
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# n = int(input("enter : "))
# # for i in range(2,n):
# #     if n%i == 0:
# #         print("not prime")
# #         break;
# # else:
# #         print("prime")

# import math
# n = int(input("enter : "))
# if n<=1:
#     print("not prime")
# else:
#     for i in range(2,math.sqrt(n)+1):
#         if n%i == 0:
#             print("not prime")
#             break;
#     else:
#         print("prime")

# n = int(input("enter : "))
# i=1
# sum=0
# while(i<=n):
#     sum += i
#     i +=1
#
# print(sum)

# n = int(input("enter : "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)

# n = int(input("enter : "))
# for i in range(1,n+1):
#     print(" " *(n-i),end =" ")
#     print("*" * (2*i-1),end=" ")
#     print("")

# n = int(input("enter : "))
# for i in range(1,n+1):
#     print("*" * (i),end=" ")
#     print("")


# n = int(input("enter : "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*" * n,end=" ")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print(" ")


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n * factorial(n-1)
#
# n= int(input("enter : "))
# fact = factorial(n)
# print(fact)


# def largestNumber(a,b,c):
#     if(a>b and a>c):
#         print(f"{a} is largest")
#     elif(b > a and b > c):
#         print(f"{b} is largest")
#     else:
#         print(f"{c} is largest")
# a= int(input("enter : "))
# b= int(input("enter : "))
# c= int(input("enter : "))
# largestNumber(a,b,c)


# def degreeConv(f):
#     c = 5*(f-37)/9
#     return c
# f= int(input("enter : "))
# res = degreeConv(f)
# print(f"{round(res,2)} degree C")

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n
# n= int(input("enter : "))
# res = int(sum(n))
# print(res)

# def pattern(n):
#     for i in range(1,n+1):
#         print("* " * (n-i+1))
#
# pattern(5)

# def pattern(n):
#     if(n==0):
#         return
#     print("* " * (n))
#     pattern(n-1)
#
# pattern(5)

# def inch_to_cm(inch):
#     return inch * 2.54
# print(inch_to_cm(7))

def rem(ls,word):
    ls1 = []
    for i in ls:
        if(i != word):
            ls1.append(i.strip(word))
    return ls1
ls = ["mehak","an","ram","rohan","mohan"]
print(rem(ls,"an"))