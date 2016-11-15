#!/usr/bin/python
import matplotlib.pyplot as plt
import math

Points = 500
Ex = [0 for x in range(Points)]
Dx = [0 for x in range(Points)]
Sx = [0 for x in range(Points)]
Smx1 = [0 for x in range(Points)]
Smx2 = [0 for x in range(Points)]
Hy = [0 for x in range(Points)]

bound1 = 300
bound2 = 400
source = 50
wp = 2000.0*10**12
vc = 57.0*10**12

c = 3.0*10**8
f0 = 4000.0*10**12
lambda0 = c/f0
dx = lambda0/10.0
dt = dx/c/2.0

Nt = 1000
#Absorb Boundary
Ex0_1 = 0
Ex0_2 = 0
ExN_1 = 0
ExN_2 = 0
#FDTD
for n in range(Nt):
	for k in range(1, Points):
		Dx[k] = Dx[k] + 0.5*(Hy[k-1]-Hy[k])
		if (k >= bound1) and (k<=bound2):
			Ex[k] = Dx[k] - Sx[k]
			Sx[k] = (1.0 - math.exp(-vc*dt))*Smx1[k]- math.exp(-vc*dt)*Smx2[k] + (wp**2*dt/vc)*(1.0 - math.exp(-vc*dt))*Ex[k]
			Smx2[k] = Smx1[k]
			Smx1[k] = Sx[k]
		else:
			Ex[k] = Dx[k]
	Ex[source] = math.sin(2*math.pi*f0*n*dt)*math.exp(-0.5*(n-100.0)**2/(30.0)**2)
	#Absorb
	Ex[0] = Ex0_1; Ex0_1 = Ex0_2; Ex0_2 = Ex[1]
	Ex[Points - 1] = ExN_1; ExN_1 = ExN_2; ExN_2 = Ex[Points - 2]
	for k in range(Points - 1):
		Hy[k] = Hy[k] + 0.5*(Ex[k] - Ex[k+1])
plt.subplot(211)
plt.axis([0,Points,-1,1])
plt.plot(range(Points),Ex)
plt.subplot(212)
plt.plot(range(Points),Hy)
plt.show()
