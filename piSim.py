#Monte Carlo Simulation
#Ethan Brown
#Scientific Computing
#Python Mini-Project

import math
import random

#Variable Declaration
N = 30
counter = 0
x = 0
y = 0
i = 0
dist = 0

#While loop
while (i < N):
	x = random.random()
	y = random.random()
	dist = math.sqrt((x**2) + (y**2))
	if (dist <= 1):
		counter += 1
		i += 1
	else:
		i += 1

#Errors and Aproximation
pi = 4 * (counter/N)
absE = abs(math.pi - pi)
realE = absE / math.pi

#Print statements
print("The number of points used, N, is: " + str(N))
print("The measured pi is: " + str(pi))
print("The absolute error is: " + str(absE))
print("The relative error is: " + str(realE))
