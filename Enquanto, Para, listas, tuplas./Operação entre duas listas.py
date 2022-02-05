n = int(input(""))
lista1 = [int(x) for x in input("").split()]
lista2 = [int(x) for x in input("").split()]

cod = input("")

cont = []

for c in range (0, n):
	if cod == "+":
		cont.append(lista1[c] + lista2[c])
	if cod == "-":
		cont.append(lista1[c] - lista2[c])
	if cod == "*":
		cont.append(lista1[c] * lista2[c])
	if cod == "/":
		cont.append(int(lista1[c] / lista2[c]))

for c in cont:
    print("{}".format(c), end=" ")
