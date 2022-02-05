lista = []
n = int(input(""))
count = 0

while count < n:
	count += 1
	num = int(input(""))
	lista.append(num)
	
i1 = int(input(""))
i2 = int(input(""))

nlista = lista[i1:i2+1]
print (nlista)
