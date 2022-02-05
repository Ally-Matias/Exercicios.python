lista = []
n = int(input(""))
count = 0

while count < n:
	count += 1
	num = int(input(""))
	lista.append(num)
	
op = int(input(""))
valor = int(input(""))

if op == 1:
	lista.append(valor)
	print (lista)
elif op == 2:
	del lista[valor]
	print(lista)	
