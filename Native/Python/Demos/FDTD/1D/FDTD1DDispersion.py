#!/usr/bin/python
import matplotlib.pyplot as plt
import math

Points = 200
Ex = [0 for x in range(Points)]
Dx = [0 for x in range(Points)]
Hy = [0 for x in range(Points)]
Ix = [0 for x in range(Points)]
Sx = [0 for x in range(Points)]
gax = [0 for x in range(Points)]
gbx = [0 for x in range(Points)]
gcx = [0 for x in range(Points)]

bound = 100
epsr = 2;  sigma = 0.01;  chi1 = 2; t0 = 0.001*10**-6
source = 20

c = 3.0*10**8
f0 = 10.0*10**9
Nt = 300

lambda0 = c/f0
dx = lambda0/10.0
dt = dx/c/2.0

#Absorb Boundary
Ex0_1 = 0; Ex0_2 = 0
ExN_1 = 0; ExN_2 = 0

#Init
del_exp = math.exp(-dt/t0)
for k in range(Points):
	if k >= bound:
		#sigma*dt/epsz = 0.01
		gax[k] = 1/(epsr+sigma+(chi1*dt/t0))
		gbx[k] = sigma
		gcx[k] = chi1*dt/t0
	else:
		gax[k] = 1

#FDTD
for n in range(Nt):
	for k in range(1,Points):
		Dx[k] = Dx[k] + 0.5*(Hy[k-1]-Hy[k])
		Ex[k] = gax[k]*(Dx[k] - Ix[k] - del_exp*Sx[k])
		Ix[k] = Ix[k] + gbx[k]*Ex[k]
		Sx[k] = del_exp*Sx[k] + gcx[k]*Ex[k]
	Ex[source] = math.exp(-0.5*(n-40.0)**2/(12.0)**2)
	#Ex[source] = Ex[source] + math.cos(2*math.pi*f0*n*dt)
	Ex[0] = Ex0_1; Ex0_1 = Ex0_2; Ex0_2 = Ex[1]
	Ex[Points - 1] = ExN_1; ExN_1 = ExN_2; ExN_2 = Ex[Points - 2]
	for k in range(Points - 1):
		Hy[k] = Hy[k] + 0.5*(Ex[k] - Ex[k+1])
plt.subplot(211)
plt.axis([0,Points,-1,1])
plt.plot(range(Points),Ex)
plt.subplot(212)
plt.plot(range(Points),Hy)
plt.axis([0,Points,-1,1])
plt.show()
