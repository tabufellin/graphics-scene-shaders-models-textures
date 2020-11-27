from render import *
from Texture import Texture

def stars(r):
  for i in range(0,r.width-1):
    for j in range(0,r.height-1):
      if(random.randint(0,i)==i and i>(0.01*j + 400)):
        r.pixels[i][j] = color(255,255,255)

def water(r):
  for i in range(0,r.width-1):
    for j in range(0,r.height-1):
      if(i>(0.01*j + 400)):
        pixels = r.pixels[i][j]
        red = pixels[0]+5 if pixels[0]<250 else 255
        green = pixels[1]+2 if pixels[1]<253 else 255
        blue = pixels[2]+12 if pixels[2]<235 else 255
        r.pixels[400-(i-400)][j] = bytes([blue,green,red]) 

def moon(render, **kwargs):

  w, v, u = kwargs['bar']

  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)

  # normales
  nA, nB, nC = kwargs['varying_normals']

  #luz
  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC
  intensity = intensity**3
  if(tcolor):
    return color(
        int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
        int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
        int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
      )
  else:
    return color(0,0,0)

def mountain(render, **kwargs):

  w, v, u = kwargs['bar']

  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)

  nA, nB, nC = kwargs['varying_normals']


  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC
  intensity = intensity**3
  if(tcolor):
    return color(
        int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
        int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
        int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
      )
  else:
    return color(0,0,0)

def planet(render, **kwargs):

  w, v, u = kwargs['bar']

  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)

  nA, nB, nC = kwargs['varying_normals']

  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC
  intensity = intensity**3
  if(tcolor):
    return color(
        int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
        int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
        int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
      )
  else:
    return color(0,0,0)

import random

def fragment(render, **kwargs):
  w, v, u = kwargs['bar']
  tx, ty = kwargs['texture_coords']
  grey = int(ty * 100)
  tcolor = color(grey, 50, 15)
  nA, nB, nC = kwargs['varying_normals']

  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC

  if (intensity>0.85):
    intensity = 1
  elif (intensity>0.60):
    intensity = 0.80
  elif (intensity>0.45):
    intensity = 0.60
  elif (intensity>0.30):
    intensity = 0.45
  elif (intensity>0.15):
    intensity = 0.30
  else:
    intensity = 0

  return color(
      int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
      int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
      int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
    )



def ground(render, **kwargs):

  w, v, u = kwargs['bar']
  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)
  nA, nB, nC = kwargs['varying_normals']

  iA, iB, iC = [ dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC
  intensity = intensity/4
  if(tcolor):
    return color(
        int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0,
        int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0,
        int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
      )
  else:
    return color(0,0,0)

def table(render, **kwargs):
  tx, ty = kwargs['texture_coords']
  return color(255,255,255)

r = Render(800, 800)
t = Texture('./models/model.bmp')
r.light = V3(0, 1, 1)

r.active_texture = t
r.active_shader = fragment

r.pov(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/model.obj', translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')
r.display('out.bmp')