# class number:
#     def __init__(self,n):
#         self.n = n;
#     def __add__(self, other):
#         return self.n + other.n
#     def __sub__(self, other):
#         return self.n - other.n
#     def __mul__(self, other):
#         return self.n * other.n
#     def __truediv__(self, other):
#         return self.n / other.n
#     def __floordiv__(self, other):
#         return self.n // other.n
#     def __str__(self):
#         return f"{self.n}"
#     def __len__(self):
#         return self.n
#
# a = number(2)
# b = number(3)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# c = number("mehak")
# print(type(c))
# print(c)
# c = number(6)
# print(c)



class Person:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
p = Person("mehak")
# print(p.__name)
print(p.name)
p.name = "Ms.Sharma"
print(p.name)