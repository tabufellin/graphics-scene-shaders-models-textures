import math
import random

def color(r,g,b):
  return bytes([b,g,r])

class Shader(object):
	def __init__(self):
		self.red = [3,14,80]
		self.blue = [130,88,44]
		self.blue2 = [255,0,44]
		self.gray = [200,200,200]

	def move(self):
		current = self.next_count
		self.next_count += self.current_count
		self.current_count = current

	def normal(self,x,y):
		return int(math.sqrt(x*x + y*y))



	def Gliese(self,x, y, tx, ty, intensity):
		#Change the intesity to simulate a star on Gliese
		intensity = 9*y*y*intensity/(x*x*40)
		normal=self.normal(x,y)
		if(random.randint(0,normal)<100):
			tx=tx*500
			ty=ty*500
			if x*tx%55>8:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity*(x/400) > 0 else 0, self.blue))
				except:
					pass
			elif tx%144>21:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue2))
				except:
					pass
			else:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue2))
				except:
					pass
		elif(random.randint(0,normal)<200):
			tx=tx*500
			ty=ty*500
			if(x/y<400 or random.randint(0,normal)<100):
				if x*tx%21>13:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity*(x/400) > 0 else 0, self.blue))
					except:
						pass
				elif tx%144>21:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.gray))
					except:
						pass
				else:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue2))
					except:
						pass
		else:
			tx=tx*500
			ty=ty*500
			if x*tx%55>8:
				if(self.drawAmerica(x,y)):
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.red))
					except:
						pass
				else:
					try:
						return bytes(map(lambda b: round(b*intensity) if b*intensity*(x/400) > 0 else 0, self.blue))
					except:
						pass
			elif tx%89>55:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.red))
				except:
					pass
			else:
				try:
					return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.blue))
				except:
					pass