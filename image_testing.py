from PIL import Image
import numpy as np
from math import pi, floor

r_num = 16
g_num = r_num ** 2
b_num = r_num ** 3

"""
img = Image.new('RGB', (60, 30), color = 'red')
img.save('pil_red.png')
"""
# Create a NumPy array, which has four elements. The top-left should be pure red, the top-right should be pure blue, the bottom-left should be pure green, and the bottom-right should be yellow
def double_size(im):

	rows = len(im)
	cols = len(im[0])

	#half_r = rows/2
	#half_c = cols/2

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
"""
[[[250, 5, 5], [5, 250, 5], [250, 5, 5], [5, 250, 5]]
[[5, 5, 250], [250, 250, 5], [250, 5, 5], [5, 250, 5]]
[[250, 5, 5], [5, 250, 5], [250, 5, 5], [5, 250, 5]]
[[250, 5, 5], [5, 250, 5], [250, 5, 5], [5, 250, 5]]]
"""
def double_size4(im):

	rows = len(im)
	cols = len(im[0])

	new_im = np.zeros(((rows * 2, cols * 2, 3)))

	r = im[0]
	first = r[0]
	second = r[int(cols/4)]
	third = r[int(cols/2)]
	fourth = r[int(3 * cols/4)]
	
	for i in range(int(rows/2)):
		for j in range(int(cols/2)):
			for k in range(3):
				new_im[i][j][k] = first[k]
		for j in range(int(cols/2), cols):
			for k in range(3):
				new_im[i][j][k] = second[k]
		for j in range(cols, int(cols * (3/2))):
			for k in range(3):
				new_im[i][j][k] = third[k]
		for j in range(int(cols * (3/2)), cols * 2):
			for k in range(3):
				new_im[i][j][k] = fourth[k]
	
	r = im[int(rows/4)]
	first = r[0]
	second = r[int(cols/4)]
	third = r[int(cols/2)]
	fourth = r[int(3 * cols/4)]
	
	for i in range(int(rows/2), rows):
		for j in range(int(cols/2)):
			for k in range(3):
				new_im[i][j][k] = first[k]
		for j in range(int(cols/2), cols):
			for k in range(3):
				new_im[i][j][k] = second[k]
		for j in range(cols, int(cols * (3/2))):
			for k in range(3):
				new_im[i][j][k] = third[k]
		for j in range(int(cols * (3/2)), cols * 2):
			for k in range(3):
				new_im[i][j][k] = fourth[k]

	
	r = im[int(rows/2)]
	first = r[0]
	second = r[int(cols/4)]
	third = r[int(cols/2)]
	fourth = r[int(3 * cols/4)]

	for i in range(rows, int(rows * (3/2))):
		for j in range(int(cols/2)):
			for k in range(3):
				new_im[i][j][k] = first[k]
		for j in range(int(cols/2), cols):
			for k in range(3):
				new_im[i][j][k] = second[k]
		for j in range(cols, int(cols * (3/2))):
			for k in range(3):
				new_im[i][j][k] = third[k]
		for j in range(int(cols * (3/2)), cols * 2):
			for k in range(3):
				new_im[i][j][k] = fourth[k]

	r = im[int(3 * rows/4)]
	first = r[0]
	second = r[int(cols/4)]
	third = r[int(cols/2)]
	fourth = r[int(3 * cols/4)]

	for i in range(int(rows * (3/2)), rows * 2):
		for j in range(int(cols/2)):
			for k in range(3):
				new_im[i][j][k] = first[k]
		for j in range(int(cols/2), cols):
			for k in range(3):
				new_im[i][j][k] = second[k]
		for j in range(cols, int(cols * (3/2))):
			for k in range(3):
				new_im[i][j][k] = third[k]
		for j in range(int(cols * (3/2)), cols * 2):
			for k in range(3):
				new_im[i][j][k] = fourth[k]

	return new_im
	
# given an rgb image as a regular python list, converts it into a numpy array image
def make_image(rgbs):

	rows = len(rgbs)
	cols = len(rgbs[0])

	new_im = np.zeros(((rows, cols, 3)))

	# convert to numpy array and scale the image back up
	for i in range(rows):
		for j in range(cols):
			for k in range(3):
				new_im[i][j][k] = rgbs[i][j][k]

	new_im = scale_up(new_im)

	return new_im
	
def show_image(pixels, name):

	# Create a PIL image from the NumPy array
	image = Image.fromarray(pixels.astype('uint8'), 'RGB')

	image_name = 'images/' + name + '.png'

	# Save the image
	image.save(image_name)
	image.show()

def scale_up(image):

	rows = len(image)
	cols = len(image[0])
	scale = 256/r_num
	new_im = np.zeros(((rows, cols, 3)))

	for i in range(rows):
		for j in range(rows):
			for k in range(3):
				new_im[i][j][k] = image[i][j][k] * scale

	return new_im

# since we're having to use a scaled down version (only 64 or 16 color values), need to scale down image
def scale_down(image):

	rows = len(image)
	cols = len(image[0])
	scale = 256/r_num
	new_im = np.zeros(((rows, cols, 3)))

	for i in range(rows):
		for j in range(rows):
			for k in range(3):
				new_im[i][j][k] = floor(image[i][j][k] / scale)

	return new_im

def get_image():

	pixels = np.array([[[17, 17, 17], [240, 17, 17]], [[17, 240, 17], [17, 17, 240]]])
	scaled = scale_down(pixels)

	"""
	# Windows looking symbol
	pixels = np.array([[[250, 5, 5], [5, 250, 5]], [[5, 5, 250], [250, 250, 5]]])
	scaled = scale_down(pixels)
	"""

	return scaled

def get_image4():

	pixels = np.array([[[239, 239, 239], [239, 239, 239], [239, 239, 239], [239, 239, 239]], 
		[[239, 239, 239], [239, 239, 239], [239, 239, 239], [239, 239, 239]], 
		[[239, 239, 239], [239, 239, 239], [239, 239, 239], [239, 239, 239]], 
		[[239, 239, 239], [239, 239, 239], [239, 239, 239], [239, 239, 239]]])

	"""
	# 4test w16 and changed to less extreme vals
	pixels = np.array([[[239, 16, 16], [239, 100, 100], [239, 175, 175], [230, 230, 230]], 
		[[175, 16, 16], [16, 16, 100], [16, 16, 239], [175, 239, 175]], 
		[[100, 16, 16], [16, 16, 150], [16, 16, 200], [100, 239, 100]], 
		[[16, 16, 16], [16, 100, 16], [16, 175, 16], [16, 239, 16]]])
	"""
	"""
	# 4test
	pixels = np.array([[[250, 5, 5], [250, 100, 100], [250, 175, 175], [235, 235, 235]], 
		[[175, 5, 5], [5, 5, 100], [5, 5, 250], [175, 250, 175]], 
		[[100, 5, 5], [5, 5, 150], [5, 5, 200], [100, 250, 100]], 
		[[5, 5, 5], [5, 100, 5], [5, 175, 5], [5, 250, 5]]])
	"""

	"""
	pixels = np.array([[[250, 5, 5], [200, 5, 5], [150, 5, 5], [100, 5, 5]], 
		[[200, 5, 5], [5, 5, 100], [5, 5, 250], [150, 5, 5]], 
		[[150, 5, 5], [5, 5, 150], [5, 5, 200], [200, 5, 5]], 
		[[100, 5, 5], [150, 5, 5], [200, 5, 5], [250, 5, 5]]])
	"""

	scaled = scale_down(pixels)

	return scaled


def rgb_to_theta(rgb):

	r, g, b = rgb
	theta = (pi/2) * ((r/r_num) + (g/g_num) + (b/b_num))
	#print("Theta is ", theta)
	return theta

def theta_to_rgb(theta):

	r = floor(theta/(pi/(r_num * 2)))
	theta = theta - r*(pi/(r_num * 2))

	g = floor(theta/(pi/(g_num * 2)))
	theta = theta - g*(pi/(g_num * 2))

	b = floor(theta/(pi/(b_num * 2)))

	return [r,g,b]

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

def test_image():

	im = get_image()
	im = scale_up(im)

	for i in range(7):
		im = double_size(im)

	show_image(im, "aman_test")
	