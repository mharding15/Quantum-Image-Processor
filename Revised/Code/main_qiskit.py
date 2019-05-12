import sys
import utils
import frqi_qiskit

def main():

	# if no command line argument is give, use 10,000 shots
	if (len(sys.argv) == 1):
		num_shots = 10000
	else:
		num_shots = int(sys.argv[1])

	image = utils.get_image()
	size = len(image)

	angles = []
	# convert all rgb pixel values into angles in [0, pi/2]
	for i in range(size):
		for j in range(size):
			angles.append((utils.rgb_to_theta(image[i][j])))

	new_angles = frqi_qiskit.run(angles, num_shots)

	im = []
	i = 0
	# converting all the recovered angles, back into rgb values
	for ang in new_angles:

		rgb = utils.theta_to_rgb(ang)
		if (i % 2 == 0):
			row = []

		row.append(rgb)

		if (i % 2 != 0):
			im.append(row)

		i += 1

	# make an image using the recovered RGB values
	new_image = utils.make_image(im)

	# double the size of the image 7 times, so that it is larger enough to actually see what the colors are
	for i in range(7):
		new_image = utils.double_size(new_image)

	utils.show_image(new_image)
	

if __name__ == "__main__":
    main()