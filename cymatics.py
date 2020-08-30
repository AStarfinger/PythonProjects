import numpy as np
from PIL import Image
import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import *
import subprocess


subprocess.run(["rm","pictures/cymatics","-r"])
subprocess.run(["mkdir","pictures/cymatics"])
width, height = 1500,1000
data = None	
i=5
# for j in range(100):
data = np.zeros((height, width,3), dtype=np.uint8)

# data[0:2000:i, 0:3000] = [255, 255, 255] # red patch in upper left
# img = Image.fromarray(data, 'RGBA')
# img.save('pictures/cymatics/my.png')
# img.show()
i+=10
# time.sleep(2)
alpha = np.array(80,dtype=np.uint8)
class Particle:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		# self.pos = np.array((x,y))
		self.vel = np.array((0,0))


particles = []

num_particles = 10000
for i in range(num_particles):
	particles.append(Particle(random.uniform(-width/2,width/2),random.uniform(-height/2,height/2)))

def updateData():
	global alpha
	# data = np.zeros((height, width,3), dtype=np.uint8)
	global data
	data = np.zeros((height, width,3), dtype=np.uint8)
	# data[:,:,3]=255
	# data=np.divide(data,1.2)
	# print(data)
	for p in particles:
		# if p.y < height and p.y>0 and p.x<width and p.x > 0:
			# data[int(p.y),int(p.x)] = (255,255,255)
		# for j in range(-1,2):
		# 	for k in range(-1,2):
		j,k=0,0
		y = max(min(p.y+j+height/2,height-1),0)
		x = max(min(p.x+k+width/2,width-1),0)

		data[int(y),int(x)] = (255,255,255)
				# if data[int(y),int(x)][1] > 0:
				# 	data[int(y),int(x)] = (180,180,180,255)
				# if data[int(y),int(x)][1] > 180:
				# 	data[int(y),int(x)] = (255,255,255,255)

	return data



# plt.plot(data)
# plt.show()
# fig = plt.figure(figsize=(6,6), facecolor='black')
# im = plt.imshow(data)
running = True
num_iterations = 100000
magnitude = 10
random_number= random.random()*magnitude-magnitude/2
random_number2= random.random()*magnitude-magnitude/2
# random_number=-0.061341077060526494
# random_number2=-0.6018394998166046
print(random_number)
print(random_number2)
i=0
modulo=1
magnitude_inside = random.randrange(10,70)
print("magnitude: ",magnitude_inside)
for t in range(num_iterations):
	beta = 4
	alpha = 3

	for p in particles:

		dx=random_number*alpha*0.01*p.y+beta*sin(magnitude_inside*p.x/width)*random_number2
		# dx=.1*p.y+height/4*sin(p.y/height)
		dy=-random_number*alpha*0.01*p.x+beta*cos(magnitude_inside*p.y/width)*random_number2
		# dy=-0.1*p.x+height/4*cos(p.x/width)
		p.x+=dx
		p.y+=dy
	if t%modulo==0:

		updateData()
		img = Image.fromarray(data, 'RGB')
		img.save('pictures/cymatics/my'+str(i)+'.png')	
		i+=1
		if(i%40):
			modulo+=1
	# img.show()

# im.set_data(data)
subprocess.run(["eog", "pictures/cymatics/my0.png"])
# while running:
# 	update()
# animation = FuncAnimation(fig, update,init_func=init, interval=10, blit=True,frames=200)#, frames=30)
# plt.show()
