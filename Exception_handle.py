def divide(n):
    n= int(input("Enter a number"))
    print(100/n)


try:
    divide(10)


except ZeroDivisionError as er:
    print(er)


except ValueError:
    print("Not valid integer")

finally:
    print("Finally")
