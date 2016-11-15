#!/usr/bin/python
import matplotlib.pyplot as plt
import math

points = 200
Dx = [0 for x in range(points)]
Ex = [0 for x in range(points)]
Hy = [0 for x in range(points)]
Ix = [0 for x in range(points)]

bound = 100
source = 20

c = 3.0*10**8
f0 = 10.0*10**9
lambda0 = c/f0
dx = lambda0/10.0
dt = dx/c/2.0

Nt = 400
#Absorb Boundary
Ex0_1 = 0
Ex0_2 = 0
ExN_1 = 0
ExN_2 = 0
for n in range(Nt):
	for k in range(1, points):
		Dx[k] = Dx[k] + 0.5*(Hy[k-1]-Hy[k])
		if k >= bound:
			#sigma*dt/epsilon0 = 0.02
			Ex[k] = 1/(4+0.02)*(Dx[k]-Ix[k])
			Ix[k] = Ix[k] + 0.02*Ex[k]
		else:
			Ex[k] = Dx[k]
	#Ex[source] = math.exp(-0.5*(n-40.0)**2/(12)**2)
	Ex[source] = Ex[source] + math.cos(2*math.pi*f0*n*dt)
	#Absorb
	Ex[0] = Ex0_1; Ex0_1 = Ex0_2; Ex0_2 = Ex[1]
	Ex[points - 1] = ExN_1; ExN_1 = ExN_2; ExN_2 = Ex[points - 2]
	for k in range(points - 1):
		Hy[k] = Hy[k] + 0.5*(Ex[k] - Ex[k+1])
plt.subplot(211)
plt.axis([0,points,-1,1])
plt.plot(range(points),Ex)
plt.subplot(212)
plt.plot(range(points),Hy)
plt.show()
