from PIL import Image
import numpy as np
from math import pi, floor

"""
img = Image.new('RGB', (60, 30), color = 'red')
img.save('pil_red.png')
"""
# Create a NumPy array, which has four elements. The top-left should be pure red, the top-right should be pure blue, the bottom-left should be pure green, and the bottom-right should be yellow
def double_size(im):

	rows = len(im)
	cols = len(im[0])

	half_r = rows/2
	half_c = cols/2

	new_im = np.zeros(((rows * 2, cols * 2, 3)))

	r = im[0]
	first = r[0]
	second = r[int(cols/2)]

	for i in range(rows):
		for j in range(cols):
			for k in range(3):
				new_im[i][j][k] = first[k]
		for j in range(cols, cols * 2):
			for k in range(3):
				new_im[i][j][k] = second[k]

	r = im[int(rows/2)]
	first = r[0]
	second = r[int(cols/2)]

	for i in range(rows, rows * 2):
		for j in range(cols):
			for k in range(3):
				new_im[i][j][k] = first[k]
		for j in range(cols, cols * 2):
			for k in range(3):
				new_im[i][j][k] = second[k]

	return new_im
	
def make_image(pixels):

	# Create a PIL image from the NumPy array
	image = Image.fromarray(pixels.astype('uint8'), 'RGB')

	# Save the image
	#image.save('image.png')
	image.show()

def get_smallest():

	pixels = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]])

	return pixels

"""
pixels = np.array([[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]], 
	[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]], 
	[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
	[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]], 
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]],
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]],
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]]])
	"""
"""
def rgb_to_theta(rgb):

	r, g, b = rgb
	theta = (pi/2) * ((r/2) + (g/4) + (b/8))
	#print("Theta is ", theta)
	return theta

def theta_to_rgb(theta):

	r = floor(theta/(pi/4))

	theta = theta - r*(pi/4)

	g = floor(theta/(pi/8))

	theta = theta - g*(pi/8)

	b = floor(theta/(pi/16))
	print("rgb = ", [r, g, b])

def test_it():

	list = []
	for i in range(2):
		for j in range(2):
			for k in range(2):
				list.append([i, j, k])

	i = 0
	for elem in list:
		print("i ============== ", i)
		i += 1
		print(elem)
		theta = rgb_to_theta(elem)
		theta_to_rgb(theta)
"""

def rgb_to_theta(rgb):

	r, g, b = rgb
	theta = (pi/2) * ((r/256) + (g/(256**2)) + (b/256**3))
	print("Theta is ", theta)
	return theta

def theta_to_rgb(theta):

	r = floor(theta/((pi/2) * (1/256)))
	theta = theta - r*((pi/2) * (1/256))
	print("After R, theta is ", theta)

	g = floor(theta/((pi/2) * (1/256**2)))
	theta = theta - g*((pi/2) * (1/256**2))
	print("After G, theta is ", theta)

	b = floor(theta/((pi/2) * (1/256**3)))

	print("rgb = ", [r, g, b])

def test_it():

	list = []
	for i in range(5):
		for j in range(5):
			for k in range(5):
				list.append([i, j, k])

	i = 0
	for elem in list:
		print("i ============== ", i)
		i += 1
		print(elem)
		theta = rgb_to_theta(elem)
		theta_to_rgb(theta)

=========================================


# coding: utf-8
# In[40]:
import qiskit as qk
from qiskit import Aer,execute
from math import pi
#pi = 3.14159

def run():

	qr =qk.QuantumRegister(3)
	cr = qk.ClassicalRegister(3)

	qc= qk.QuantumCircuit(qr,cr)

	#Creating the Hadamard State
	qc.h(qr[0])
	qc.h(qr[1])

	# Circuit for I(theta) starts here
	#qc.x(qr[0])
	#qc.x(qr[1])
	
	angles = [pi/2, 0, pi/2, 0]
	#pi/4=0.7853
	qc.cu3(angles[0],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[0],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[0],0,0,qr[0],qr[2])
	
	###
	qc.barrier(qr)
	qc.measure(qr,cr)

	# In[41]:
	backend_sim = Aer.get_backend('qasm_simulator')
	job_sim = execute(qc, backend_sim, shots=10000)
	result_sim = job_sim.result()

	# In[42]:

	counts = result_sim.get_counts(qc)
	print(counts)
###

	"""

	#pi/12=0.2617

	qc.x(qr[1])

	qc.cu3(angles[1],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[1],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[1],0,0,qr[0],qr[2])

	#pi/6=0.5234

	qc.x(qr[0])
	qc.x(qr[1])

	qc.cu3(angles[2],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[2],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[2],0,0,qr[0],qr[2])

	#pi/16=0.1963

	qc.x(qr[1])

	qc.cu3(angles[3],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[3],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[3],0,0,qr[0],qr[2])

	qc.barrier(qr)
	qc.measure(qr,cr)

	# In[41]:
	backend_sim = Aer.get_backend('qasm_simulator')
	job_sim = execute(qc, backend_sim, shots=10000)
	result_sim = job_sim.result()

	# In[42]:

	counts = result_sim.get_counts(qc)
	print(counts)
"""
======================

def probs(results):

	angles = []
	if ("000" in results):
		prob = results["000"]/num_shots
		# to get the angle back cos^-1(sqrt(probability))
		angles.append(acos(sqrt(4 *prob)))
	else:
		angles.append(pi/2)

	if ("001" in results):
		probs.append(results["001"]/num_shots)
	else:
		probs.append(0.)

	if ("010" in results):
		probs.append(results["010"]/num_shots)
	else:
		probs.append(0.)

	if ("011" in results):
		probs.append(results["011"]/num_shots)
	else:
		probs.append(0.)

	print(probs)

========
	if ("000" in results):
		prob = results["000"]/num_shots
		# to get the angle back cos^-1(sqrt(4 * probability))
		angles.append(acos(sqrt(4 *prob)))
	else:
		angles.append(pi/2)


#converting from rgb to theta and vice versa in degrees
====================
# function to convert an rgb value into an angle, theta
def rgb_to_theta(rgb):

	r, g, b = rgb
	# storing the angle in degrees instead of radians
	theta = (90) * ((r/256) + (g/(256**2)) + (b/256**3))
	return theta

# function to convert the angle theta back into an rgb value
def theta_to_rgb(theta):

	# recovering the value of r
	r = floor(theta/(90/256))
	# subtracting from theta to get the angle to be in the first region of the quadrant
	theta = theta - r*(90/256)
	# now that the angle is in the first region, can multiply to get it to the proper region for the g value
	theta *= 256

	# recovering the value of g
	g = floor(theta/(90/256))
	theta = theta - g*(90/256)
	theta *= 256

	b = floor(theta/(90/256))

	return [r,g,b]

"""
pixels = np.array([[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]], 
	[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]], 
	[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
	[[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]], 
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]],
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]],
	[[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0]]])
	"""

	"""
	# I can put this into a for loop if I need to.
	# probs for 1st pixel
	if ("000" in results):
		prob["000"] = results["000"]/num_shots
	else:
		prob["000"] = 0.

	if ("100" in results):
		prob["100"] = results["100"]/num_shots
	else:
		prob["100"] = 0.

	# probs for 2nd pixel
	if ("001" in results):
		prob["001"] = results["001"]/num_shots
	else:
		prob["001"] = 0.

	if ("101" in results):
		prob["101"] = results["101"]/num_shots
	else:
		prob["101"] = 0.

	# probs for 3rd pixel
	if ("010" in results):
		prob["010"] = results["010"]/num_shots
	else:
		prob["010"] = 0.

	if ("110" in results):
		prob["110"] = results["110"]/num_shots
	else:
		prob["110"] = 0.

	# probs for 4th pixel
	if ("011" in results):
		prob["011"] = results["011"]/num_shots
	else:
		prob["011"] = 0.

	if ("111" in results):
		prob["111"] = results["111"]/num_shots
	else:
		prob["111"] = 0.
	

	angles = []
	# now need to recover the angles
	zero_prob = prob["000"]/(prob["000"] + prob["100"])
	angles.append(acos(sqrt(zero_prob)))

	zero_prob = prob["001"]/(prob["001"] + prob["101"])
	angles.append(acos(sqrt(zero_prob)))

	zero_prob = prob["010"]/(prob["010"] + prob["110"])
	angles.append(acos(sqrt(zero_prob)))

	zero_prob = prob["011"]/(prob["011"] + prob["111"])
	angles.append(acos(sqrt(zero_prob)))
	"""

===========================

qc.ccx(qr[0], qr[1], qr[4])
qc.ccx(qr[2], qr[4], qr[5])
qc.ccx(qr[3], qr[5], qr[6])

qc.cu3(angles[0],0,0,qr[6],qr[7])

qc.ccx(qr[3], qr[5], qr[6])
qc.ccx(qr[2], qr[4], qr[5])
qc.ccx(qr[0], qr[1], qr[4])

===========================
pixels = np.array([[[250, 5, 5], [5, 250, 5], [5, 5, 250], [250, 250, 5]], 
		[[250, 5, 250], [5, 250, 250], [100, 50, 5], [5, 100, 50]], 
		[[100, 100, 100], [100, 150, 200], [200, 100, 150], [150, 200, 150]], 
		[[75, 180, 105], [180, 105, 75], [105, 180, 75], [128, 128, 128]]])

===========================

def get_xs():

	chars = ["0","1"]
	vals = []

	for i in chars:
		for j in chars:
			for k in chars:
				for l in chars:
					vals.append(i + j + k + l)

	total = []
	for i in range(16):

		x_vals = []
		word = vals[i]
		for j in range(4):
			if(word[j] == '0'):
				x_vals.append('x')
			else:
				x_vals.append('_')

		total.append(x_vals)

		for k in range(16):
			for q in range(4):
				if (x_vals[q] == 'x'):
					if (vals[k][q] == '0'):
						new_val = []
						for r in range(4):
							if (r != q):
								new_val.append(vals[k][r])
							else:
								new_val.append('1')
						vals[k] = new_val
					else:
						new_val = []
						for r in range(4):
							if (r != q):
								new_val.append(vals[k][r])
							else:
								new_val.append('0')
						vals[k] = new_val

		print("================ ", i, " =================")
		print(vals)

	print(total)