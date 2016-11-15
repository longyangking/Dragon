#!/usr/bin/python
import matplotlib.pyplot as plt
import math

points = 200
Ex = [0 for x in range(points)]
Hy = [0 for x in range(points)]

source = 100

c = 3.0*10**8
f0 = 10.0*10**9
lambda0 = c/f0
dx = lambda0/10.0
dt = dx/c/2.0

Nt = 100
Fn = 100
freqs = [2*f0*i/Fn for i in range(Fn)]
real_pt = [[0 for f in range(points)] for k in range(Fn)]
imag_pt = [[0 for f in range(points)] for k in range(Fn)]
Ex0_1 = Ex0_2 = ExN_1 = ExN_2 = 0
for n in range(Nt):
	for k in range(1,points):
		Ex[k] = Ex[k] + 0.5*(Hy[k-1] - Hy[k])
	#Ex[source] = math.exp(-0.5*(n-40.0)**2/(12)**2)
	Ex[source] = Ex[source] + math.cos(2*math.pi*f0*n*dt)
	Ex[0] = Ex0_1; Ex0_1 = Ex0_2; Ex0_2 = Ex[1]
	Ex[points - 1] = ExN_1; ExN_1 = ExN_2; ExN_2 = Ex[points - 2]
	for k in range(points - 1):
		Hy[k] = Hy[k] + 0.5*(Ex[k] - Ex[k+1])
	for m in range(Fn):
		for k in range(points):	
			real_pt[m][k] = real_pt[m][k] + Ex[k]*math.cos(2*math.pi*freqs[m]*dt*n)
			imag_pt[m][k] = imag_pt[m][k] + Ex[k]*math.sin(2*math.pi*freqs[m]*dt*n)
#PLOT
tf = Fn/2
plt.subplot(411)
plt.axis([0,points,-1,1])
plt.plot(range(points),Ex)
plt.subplot(412)
plt.plot(range(points),Hy)
plt.subplot(413)
plt.plot(range(points),real_pt[tf])
plt.subplot(414)
plt.plot(range(points),imag_pt[tf])
plt.show()
