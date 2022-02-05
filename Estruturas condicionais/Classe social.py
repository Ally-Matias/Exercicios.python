r = float(input(""))

if r <= 324:
	print ("Extremamente pobre")
	
elif r >= 324 and r <= 648:
	print("Pobre")

elif r >= 648 and r <= 1164:
	print("Vulneravel")

elif r >= 1164 and r <= 1764:
	print("Baixa classe media")
	
elif r >= 1764 and r <= 2564:
	print("Media classe media")
	
elif r >= 2564 and r <= 4076:
	print("Alta classe media")

elif r >= 4076 and r <= 9920:
	print("Baixa classe alta")
	
elif r >= 9920:
	print("Alta classe alta")
