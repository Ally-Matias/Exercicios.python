from math import sqrt

xa = float(input(""))
ya = float(input(""))
xb = float(input(""))
yb = float(input(""))

resultado = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print("{:.2f}".format(resultado))
