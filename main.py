#Sebas Gonzalez 18588
#takes around 4 mins to run, go for a cup of coffe :3
from render import Render, color
from Texture import Texture
from math_things import V3, norm
from shaders import mountain, fragment, moon, planet, stars, water
import random
import math

r = Render(800, 800)
r.pov(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))

#stars in the sky
stars(r)
		
#Draw a moon
t = Texture('./models/red.bmp')
r.active_texture = t
r.active_light = norm(V3(0, 20, 0))
r.load('./models/sphere.obj', [-0.30, 0.60, 0] , [0.18, 0.18, 0.18], [0, 0.2, 0])
r.active_shader = moon
r.draw_arrays('TRIANGLES') 

#Draw another moon with diferent texture
t = Texture('./models/arcoiris.bmp')
r.active_texture = t
r.load('./models/sphere.obj', [-0.55, 0.70, 0], [0.20, 0.20, 0.20], [0, 0.2, 0])
r.active_shader = planet
r.draw_arrays('TRIANGLES') 


#draw giant rock man
t = Texture('./models/fire2.bmp')
r.active_texture = t
r.load('./models/stone_man.obj', [0.5, 0, 0], [0.05, 0.05, 0.05], [0, 0.2, 0])
r.active_shader = planet
r.draw_arrays('TRIANGLES') 

#D ground is like creating a lot of little objects
t = Texture('./models/model.bmp')
r.active_texture = t
r.active_shader = mountain
random.seed(1)
for i in range(0,30):
	size = random.random()/4
	r.load('./models/model.obj', [-i/30, math.sin((30*i))*0.1, 0], [size,size, size], [0, 1.7, 1.1])
	r.draw_arrays('TRIANGLES')

#Draw trees we use for because we want to draw a lot in diferent positions
#we use two fors because we want some of hen a little bit back
for x in range(-90, 90, 10):
	print("three")
	t = Texture('./models/fire2.bmp')
	r.active_texture = t
	r.active_light = norm(V3(10, 20, 0))
	x = x/100
	r.load('./models/Tree.obj', [x, 0, 2], [0.02, 0.02, 0.02], [0, 0.7, 0])
	r.active_shader = fragment
	r.draw_arrays('TRIANGLES') 

for x in range(-80, 80, 10):
	print("three")
	t = Texture('./models/fire2.bmp')
	r.active_texture = t
	r.active_light = norm(V3(10, 20, 0))
	x = x/100
	r.load('./models/Tree.obj', [x, 0, 1], [0.02, 0.02, 0.02], [0, 0.7, 0])
	r.active_shader = fragment
	r.draw_arrays('TRIANGLES') 

#add a reflective water to the scene
water(r)

#out
r.display('out.bmp')