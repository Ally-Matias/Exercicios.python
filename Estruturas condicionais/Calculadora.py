num1 = float(input(""))
num2 = float(input(""))
dig = input("")
cont = 0

if dig == "+":
	cont = num1 + num2
	print("{:.6f}".format(cont))
	
elif dig == "-":
	cont = num1 - num2
	print("{:.6f}".format(cont))
	
elif dig == "*":
	cont = num1 * num2
	print("{:.6f}".format(cont))
	
elif dig == "/" and num2 > 0:
	cont = num1 / num2
	print("{:.6f}".format(cont))
	
elif dig != "+" or "-" or "*" or "/" and num2 == 0.00:
	print("Operacao invalida")
