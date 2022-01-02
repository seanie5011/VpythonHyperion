#Project Hyperion 

from vpython import *

scene.autoscale = False,
#sphere(pos = vector(0,0,0), radius = 25, shininess = 0, texture = https://i.imgur.com/OCxjT4W.jpg)

t = 0
dt = 0.0002
x = 1
y = 0
vx = 0
vy = 8
l = 0.1
theta = 0
w = 0

centreball = sphere(pos = vector(0, 0, 0), radius = 0.15, color = color.yellow)#texture = https://i.imgur.com/fq4oFHb.jpg)
ballmass1 = sphere(pos = vector(x, y, 0) + vector(l*cos(theta), l*sin(theta), 0), radius = 0.05, color = color.red, make_trail=True, trail_type='points', interval=50, retain=500)
ballmass2 = sphere(pos = vector(x, y, 0) - vector(l*cos(theta), l*sin(theta), 0), radius = 0.05, color = color.blue)
comass = cylinder(pos = ballmass2.pos, axis = 2*vector(l*cos(theta), l*sin(theta), 0), radius = 0.01, make_trail=False, interval=10, retain=350)

                    
while t<60:
    rate(1000)
    t = t + dt
    vx = vx - dt * ((4*pi*pi*x)/(((x**2 + y**2)**0.5)**3))
    x = x + vx * dt
    vy = vy - dt * ((4*pi*pi*y)/(((x**2 + y**2)**0.5)**3))
    y = y + vy *dt
    w = w + dt * ((-12*pi*pi/((x**2 + y**2)**0.5)) * (x*sin(theta - y*cos(theta))) * (x*cos(theta) + y*sin(theta)))
    theta = theta + w * dt
    ballmass1.pos = vector(x, y, 0) + vector(l*cos(theta), l*sin(theta), 0)
    ballmass2.pos = vector(x, y, 0) - vector(l*cos(theta), l*sin(theta), 0)
    comass.pos = ballmass2.pos
    comass.axis = 2*vector(l*cos(theta), l*sin(theta), 0)
