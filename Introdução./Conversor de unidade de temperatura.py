celsius = float(input(""))
fahrenheit = float(input(""))

fahren = (celsius * 9 / 5) + 32
cels = (fahrenheit - 32) * 5 / 9

print("{:.2f} C = {:.2f} F".format (celsius, fahren))

print("{:.2f} F = {:.2f} C".format (fahrenheit, cels))
