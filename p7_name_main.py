def myfunc():
    print("hello world")
    print(__name__)
myfunc()

if __name__ == "__main__":
    print("running code inside the its own module")
    myfunc()