import sys
import utils
import frqi_cirq
import time

# return the average difference between the entries in two lists
def avg_diff(list1, list2):

	size = len(list1)

	sum = 0
	for i in range(size):
		sum += abs(list1[i] - list2[i])

	return sum/size

def run(num_shots):

	image = utils.get_image()
	size = len(image)

	angles = []
	# convert all rgb pixel values into angles in [0, pi/2]
	for i in range(size):
		for j in range(size):
			angles.append((utils.rgb_to_theta(image[i][j])))

	new_angles, totalTime = frqi_cirq.run(angles, num_shots)

	diff = avg_diff(angles, new_angles)

	return totalTime, diff