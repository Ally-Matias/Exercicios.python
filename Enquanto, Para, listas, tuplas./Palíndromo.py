palavras = input("")

characters = ".', !?"

palavras = ''.join( x for x in palavras if x not in characters)

palavras = palavras.lower()
		
elem = ""

elem = ' '.join(c[::-1] for c in palavras.split())

if palavras == elem:
	print("SIM")
else:
	print("NAO")

