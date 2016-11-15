#!/usr/bin/python
import math
import matplotlib.pyplot as plt

cells = 200
Ex = [0 for x in range(0,cells)]
Hy = [0 for x in range(0,cells)]

c = 3.0*10**8
f0 = 10.0*10**9
source = 20
lambda0 = c/f0

dx = lambda0/10.0
dt = dx/2.0/c

Nt = 400
Ex0 = [0 for x in range(Nt)]
ExN = [0 for x in range(Nt)]
for n in range(Nt):
	for k in range(1,cells):
		if k>=100:
			Ex[k] = Ex[k] + 0.5/4*(Hy[k-1]-Hy[k])
		else:
			Ex[k] = Ex[k] + 0.5*(Hy[k-1]-Hy[k])
	Ex[source] = Ex[source] + math.sin(2.0*math.pi*f0*n*dt)
	Ex[0] = Ex0[n]
	Ex[cells - 1] = ExN[n]
	for k in range(cells-1):
		Hy[k] = Hy[k] + 0.5*(Ex[k] - Ex[k+1])
	if n+2 < Nt:
		Ex0[n+2] = Ex[1]
		ExN[n+2] = Ex[cells-2]
plt.subplot(211)
plt.axis([0,200,-1,1])
plt.plot(range(cells),Ex)
plt.subplot(212)
plt.axis([0,200,-2,2])
plt.plot(range(cells),Hy)
plt.show()
