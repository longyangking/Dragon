#!/usr/bin/python
import matplotlib.pyplot as plt
import math

#FDTD Region
pointsX = 100; pointsY = 120
Dz = [[0 for y in range(pointsY)] for x in range(pointsX)]
Ez = [[0 for y in range(pointsY)] for x in range(pointsX)]
Hx = [[0 for y in range(pointsY)] for x in range(pointsX)]
Hy = [[0 for y in range(pointsY)] for x in range(pointsX)]

totalX1 = 20; totalX2 = pointsX - totalX1 - 1
totalY1 = 20; totalY2 = pointsY - totalY1 - 1
PMLcells = 10

#Incident Plane Wave
planewaveY = 15
Ez_inc = [0 for y in range(pointsY)]
Hx_inc = [0 for y in range(pointsY)]
Ez_incE01 = 0; Ez_incE02 = 0
Ez_incEN1 = 0; Ez_incEN2 = 0

#Main Parameters
c = 3.0*10**8
f0 = 10.0*10**9; lambda0 = c/f0
dx = lambda0/10.0; dt = dx/2.0/c

Nt = 200
##Init Material
print 'Init Material...'
ga = [[1.0 for y in range(pointsY)] for x in range(pointsX)]
gi2 = [1.0 for x in range(pointsX)]; gi3 = list(gi2)
gj2 = [1.0 for y in range(pointsY)]; gj3 = list(gj2)
fi1 = [0.0 for x in range(pointsX)]
fi2 = list(gi2); fi3 = list(gi2)
fj1 = [0.0 for y in range(pointsY)]
fj2 = list(gj2); fj3 = list(gj2)
ihx = [[0 for y in range(pointsY)] for x in range(pointsX)]
ihy = [[0 for y in range(pointsY)] for x in range(pointsX)]

for i in range(PMLcells):
    xnum = PMLcells - i; xd = PMLcells
    xxn = (1.0*xnum)/(1.0*xd); xn = 0.25*xxn**3
    gi2[i] = 1.0/(1.0+xn); gi2[pointsX-1-i] = 1.0/(1.0+xn);
    gi3[i] = (1.0 - xn)/(1.0 + xn); gi3[pointsX - 1 - i] = (1.0 - xn)/(1.0 + xn)
    xxn = (xnum - 0.5)/xd; xn = 0.25*xxn**3
    fi1[i] = xn; fi1[pointsX-2-i] = xn
    fi2[i] = 1.0/(1.0 + xn); fi2[pointsX-2-i] = 1.0/(1.0+xn)
    fi3[i] = (1.0 - xn)/(1.0 + xn); fi3[pointsX-2-i] = (1.0 - xn)/(1.0 + xn)

for j in range(PMLcells):
    xnum =PMLcells - j; xd = PMLcells
    xxn = (1.0*xnum)/(1.0*xd); xn =  0.25*xxn**3   
    gj2[j] = 1.0/(1.0+xn); gj2[pointsY-1-j] = 1.0/(1.0+xn)
    gj3[j] = (1.0 - xn)/(1.0 + xn); gj3[pointsY - 1 - j] = (1.0 - xn)/(1.0 + xn)
    xxn = (xnum - 0.5)/xd; xn = 0.25*xxn**3
    fj1[j] = xn; fj1[pointsY-2-j] = xn
    fj2[j] = 1.0/(1.0 + xn); fj2[pointsY-2-j] = 1.0/(1.0+xn)
    fj3[j] = (1.0 - xn)/(1.0 + xn); fj3[pointsY-2-j] = (1.0 - xn)/(1.0 + xn)

#Calculation
print 'Start to calculate...'
for n in range(Nt):
    #Incident Field
    for j in range(1,pointsY):
        Ez_inc[j] = Ez_inc[j] + 0.5*(Hx_inc[j-1]-Hx_inc[j])
    #Absorption for Incident Wave
    Ez_inc[0] = Ez_incE02; Ez_incE02 = Ez_incE01; Ez_incE01 = Ez_inc[1];
    Ez_inc[pointsX-1] = Ez_incEN2; Ez_incEN2 = Ez_incEN1; Ez_incEN1 = Ez_inc[pointsX-2]
    #Total Dz Field 
    for i in range(1,pointsX):
        for j in range(1,pointsY):
            Dz[i][j] = gi3[i]*gj3[j]*Dz[i][j] + gi2[i]*gj2[j]*0.5*(Hy[i][j]-Hy[i-1][j]-Hx[i][j]+Hx[i][j-1])
    
    Ez_inc[planewaveY] = math.cos(2*math.pi*0.8*f0*n*dt)
    for i in range(totalX1,totalX2+1):
        Dz[i][totalY1] = Dz[i][totalY1] + 0.5*Hx_inc[totalY1-1]
        Dz[i][totalY2] = Dz[i][totalY2] - 0.5*Hx_inc[totalY2]
    #Total Ez Field
    for i in range(1,pointsX-1):
        for j in range(1,pointsY-1):
            Ez[i][j] = ga[i][j]*Dz[i][j]
    #Incident Hx Field
    for j in range(pointsY-1):
        Hx_inc[j] = Hx_inc[j] + 0.5*(Ez_inc[j]-Ez_inc[j+1])
    #Total Hx Field
    for i in range(pointsX):
        for j in range(pointsY-1):
            curl_E = Ez[i][j] - Ez[i][j+1]
            ihx[i][j] = ihx[i][j] + fi1[i]*curl_E
            Hx[i][j] = fj3[j]*Hx[i][j] + fj2[j]*0.5*(curl_E + ihx[i][j])
    for i in range(totalX1,totalX2+1):
        Hx[i][totalY1-1] = Hx[i][totalY1-1] + 0.5*Ez_inc[totalY1]
        Hx[i][totalY2] = Hx[i][totalY2] - 0.5*Ez_inc[totalY2]
    #Total Hy Field
    for i in range(pointsX-1):
        for j in range(pointsY):
            curl_E = Ez[i+1][j] - Ez[i][j]
            ihy[i][j] = ihy[i][j] + fj1[j]*curl_E
            Hy[i][j] = fi3[i]*Hy[i][j] + fi2[i]*0.5*(curl_E + ihy[i][j])
    for j in range(totalY1,totalY2+1):
        Hy[totalX1-1][j] = Hy[totalX1-1][j] - 0.5*Ez_inc[j]
        Hy[totalX2][j] = Hy[totalX2][j] + 0.5*Ez_inc[j]
plt.imshow(Ez)
plt.show()
