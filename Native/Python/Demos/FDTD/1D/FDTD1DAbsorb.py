#!/usr/bin/python
import math
import matplotlib.pyplot as plt

cells = 200
Ex = [0 for x in range(0,cells)]
Hy = [0 for x in range(0,cells)]

c = 3.0*10**8
f0 = 10.0*10**9
source = cells/2
lambda0 = c/f0

dx = lambda0/10
dt = dx/2/c

T = 2/f0
Nt = int(T/dt)
Nt = 250
Ex0 = [0 for x in range(Nt)]
ExN = [0 for x in range(Nt)]
for n in range(Nt):
	for k in range(1,cells):
		Ex[k] = Ex[k] + 0.5*(Hy[k-1]-Hy[k])
	Ex[source] = math.exp(-0.5*(n-40.0)**2/(12)**2)
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
plt.axis([0,200,-1,1])
plt.plot(range(cells),Hy)
plt.show()
