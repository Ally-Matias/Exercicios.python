import math

abc = [float(x) for x in input("").split()]

def formula(abc):
	delta = (abc[1]**2) - (4*abc[0]*abc[2])

	if delta > 0:
	   r1 = (-abc[1] + math.sqrt(delta)) / (2*abc[0])
	   r2 = (-abc[1] - math.sqrt(delta)) / (2*abc[0])
	   return ("{:.2f} {:.2f}".format(r1, r2))
	elif delta == 0:
	    r = (-abc[1] + math.sqrt(delta)) / (2*abc[0])
	    return ("{:.2f} {:.2f}".format(r, r))
	elif delta < 0:
		return ("None")
		
		
resul = formula(abc)
print(resul)
