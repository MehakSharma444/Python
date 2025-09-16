# class employee:
#     companyy = "Micorsoft"
#     def __init__(self,ID,name,salary,company=""): #dunder method which is automatically called when object is created
#         self.id = ID
#         self.name = name
#         self.sal = salary
#         self.comp = company if company else employee.companyy
#         print(f"id is : {self.id}\n"
#               f"name is : {self.name} \n"
#               f"salary is : {self.sal}\n"
#               f"company is : {self.comp}\n")
#
# mehak = employee(1,"ms",12343311212)
# print(mehak.id,mehak.name,mehak.sal,mehak.comp)


# class employee:
#     company = "Micorsoft"
#     def __init__(self,ID,name,salary,comp=""):
#         self.id = ID
#         self.name = name
#         self.sal = salary
#         self.company = comp
#         print(f"id is : {self.id}\n"
#               f"name is : {self.name} \n"
#               f"salary is : {self.sal}\n"
#               f"company is : {self.company}\n")
#
# mehak = employee(1,"ms",12098874899)


# class calculator:
#     def __init__(self,n):
#         self.n = n
#     def square(self):
#         print(f"square of {self.n} is {self.n*self.n}")
#     def cube(self):
#         print(f"cube of {self.n} is {self.n*self.n*self.n}")
#     def sqroot(self):
#         print(f"sqroot of {self.n} is {self.n**1/2}")
# p = calculator(4)
# p.square()
# p.cube()
# p.sqroot()