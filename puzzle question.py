# a = "html"
# if a == "html" and "python":
#     print("toe")

a = "hello world this is long"
b = "hello world this is long"
print(a is b)
a = "hello"
b = "hello"
print(a is b)

a = [1, 2, 3]
b = a
b.append(4)
print(a)

a = "html"
if a == "html" and None:
    print("tac")

a = "html"
if a == "html" and []:
    print("tick")