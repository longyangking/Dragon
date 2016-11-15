#!/usr/bin/python
import matplotlib.pyplot as plt
import math

pointsX = 100
pointsY = 100
Dz = [[0 for y in range(pointsY)] for x in range(pointsX)]
Ez = [[0 for y in range(pointsY)] for x in range(pointsX)]
Hx = [[0 for y in range(pointsY)] for x in range(pointsX)]
Hy = [[0 for y in range(pointsY)] for x in range(pointsX)]

c = 3.0*10**8
f0 = 10.0*10**9
lambda0 = c/f0
dx = lambda0/10; dy = dx
dt = dx/c/2.0

Nt = 100
sourceX = 50; sourceY = 50
##No absorb temperaily...
for n in range(Nt):
    for i in range(1,pointsX):
        for j in range(1,pointsY):
		Dz[i][j] = Dz[i][j] + 0.5*(Hy[i][j] - Hy[i-1][j] - Hx[i][j] + Hx[i][j-1])
		Ez[i][j] = Dz[i][j]
    Ez[sourceX][sourceY] = math.exp(-0.5*(n - 50.0)**2/(20.0)**2)
    for i in range(pointsX-1):
        for j in range(pointsY-1):
                Hx[i][j] = Hx[i][j] + 0.5*(Ez[i][j] - Ez[i][j+1])
                Hy[i][j] = Hy[i][j] + 0.5*(Ez[i+1][j] - Ez[i][j])
plt.imshow(Ez)
plt.show()
