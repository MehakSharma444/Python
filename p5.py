# class employee:
#     def __init__(self):
#         self.company = "TCS"
#     def show(self):
#         print(f" my company is {self.company}")
# class coder(employee):
#     def __init__(self):
#         self.company = "MICROSOFT"
#         # super().__init__()
#     def show(self):
#         print(f" my company is {self.company}")
# class programmer(coder,employee):
#     def __init__(self):
#         self.company = "TCS ION"
#         super().__init__()
#     def show(self):
#         print(f" my company is {self.company}")
# a= programmer()
# a.show()
# b = employee()
# b.show()
# c = coder()
# c.show()

# class demo:
#     company = "TCS"
#     @classmethod
#     def show(cls):
#         print(f" my company is {cls.company}")
#     @property
#     def name(self):
#         return f"name is {self.ename}"
#
#
#
# a = demo()
# a.company = "google"
# a.ename = "Mehak Sharma"
# print(a.name)
# a.show()


# class demo:
#     company = "TCS"
#     def __init__(self,value):
#         self.ename = value
#     @classmethod
#     def show(cls):
#         print(f" my company is {cls.company}")
#     @property
#     def name(self):
#         return f"name is {self.ename}"
#
#
#
# a = demo("Mehak Sharma")
# a.company = "google"
# a.show()
# print(a.name)


class demo:
    company = "TCS"
    @classmethod
    def show(cls):
        print(f" my company is {cls.company}")
    @property
    def name(self):
        return f"name is {self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

a = demo()
a.company = "google"
a.name = "mehak sharma"
a.show()
print(a.name)
print(a.fname)

