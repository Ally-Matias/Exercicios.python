produto = float(input(""))
chute1 = float (input (""))
chute2 = input ("")

if chute1 > produto and chute2 == "maior":
    print("primeiro")
elif chute1 < produto and chute2 == "menor":
    print("primeiro")
elif chute1 > produto and chute2 == "menor":
    print ("segundo")
elif chute1 < produto and chute2 == "maior":
    print ("segundo")
else:
	print("empate")
