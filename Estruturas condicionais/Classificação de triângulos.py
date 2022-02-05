l1 = int(input(""))
l2 = int(input(""))
l3 = int(input(""))

if (l1 + l2) >= l3 and (l1 + l3) >= l2 and (l2 + l3) >= l1:
	if l1 == l2 and l2 == l3:
		print ("EQ")	
	elif l1 == l2 and l2 != l3 or l2 == l3 and l3 	!= l1 or l1 == l3 and l1 != l2:
		print ("IS")
	elif l1 != l2 and l2 != l3:
		print ("ES")
else:
	print ("NT")
