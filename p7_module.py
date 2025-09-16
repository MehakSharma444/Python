# from p7_name_main import myfunc
# print(__name__)
from logging import exception


# def division(num, demo):
#     try:
#         if demo == 0:
#             raise ZeroDivisionError("infinite, so division by zero not possible")
#         else:
#             print(num / demo)
#         return
#     except ZeroDivisionError as e:
#         print(e)
#         return
#     finally:
#         print("over")
#
# division(10, 5)  # Output: 2.0


def division(num, demo):
    try:
        if demo == 0:
            raise exception("infinite, so division by zero not possible")
        else:
            print(num / demo)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("over")

division(10, 0)  # Output: 2.0
