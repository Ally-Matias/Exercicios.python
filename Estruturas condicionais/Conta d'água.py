num = int(input(""))
cont = 7

if num >= 11:
	if num >= 30:
		cont += 20
	else:
		cont += (num - 11 + 1)
		
if num >= 31:
	if num >= 100:
		cont += (100 - 31 + 1) * 2
	else:
		cont += (num - 31 + 1) * 2
		
if num >= 101:
	cont += (num - 101 + 1) * 5
			
print("R$ {}".format(cont))
	
