#Approx e Simulation
#Ethan Brown
#Scientific Computing
#Python Mini-Project

import sys
import math
outFile = open("approxEOut.txt","w")
#Variable Declaration
N=1
TOL = float(sys.argv[1])
appE = ((1+(1/N))**N)
absEr = abs(math.e - appE)
#Errors and Approximation
while (absEr > TOL):
	N += 1
	appE = ((1+(1/N))**N)
	absEr = abs(math.e - appE)

realEr = absEr / math.e
#Print statements
outFile.write("The number of points used, N, is: " + str(N)+"/n")
outFile.write("The measured e is: " + str(appE) + "/n")
outFile.write("The absolute error is: " + str(absEr) + "/n")
outFile.write("The relative error is: " + str(realEr) + "/n")
