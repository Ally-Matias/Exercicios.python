from math import sqrt

a = int(input(""))
b = int(input(""))
c = int(input(""))

delta=(b**2)-(4*a*c)

if delta < 0:
    print("NTR")
elif delta == 0:
    x1 = ((-b)+sqrt(delta))/(2*a)
    x2 = ((-b)-sqrt(delta))/(2*a)
    print("{:.2f}".format(x1))
else:
    x1=((-b)+sqrt(delta))/(2*a)
    x2=((-b)-sqrt(delta))/(2*a)
    print("{:.2f}".format(x1))
    print("{:.2f}".format(x2))
