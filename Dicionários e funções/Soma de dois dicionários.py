dict1 = {int(c[0]): float(c[1]) for c in [x.split(":") for x in input("").split(",")]}
dict2 = {int(c[0]): float(c[1]) for c in [x.split(":") for x in input("").split(",")]}

def funcao(dict):
	chaves = list(dict.keys())
	chaves.sort()
	for c in chaves:
		print("{}:{:.2f}".format(c, dict[c]))
		
dict = {}

for c in dict1:
	if c in dict2:
		dict[c] = dict1[c] + dict2[c]
	else:
		dict[c] = dict1[c]
		
for x in dict2:
	if x not in dict1:
		dict[x] = dict2[x]
		
	
funcao(dict)
