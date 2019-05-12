import cirq
from cirq.ops import H, CZ, CNOT, X, RotYGate
from math import pi, sqrt, acos
from utils import r_num, g_num, b_num

def probs(results, num_shots):

	# obtain all results for each qubit in each measurement
	a_meas = results.measurements['a']
	b_meas = results.measurements['b']
	c_meas = results.measurements['c']

	# will store the number of times '0' and '1' are measured for each pixel
	measurements = {}
	for i in range(4):
		measurements[i] = []
		measurements[i].append(0)
		measurements[i].append(0)

	# for each measurement that was made
	for i in range(num_shots):

		# obtain the results for each qubit in the current measurement
		a_res = a_meas[i][0]
		b_res = b_meas[i][0]
		c_res = c_meas[i][0]

		# if 'row' qubit is 0
		if (b_res == False):
			# pixel is 00
			if (a_res == False):
				# increment the measurements for the pixel for either '0' or '1'
				if (c_res == False):
					measurements[0][0] += 1
				else:
					measurements[0][1] += 1
			# pixel is 01	
			else:
				if (c_res == False):
					measurements[1][0] += 1
				else:
					measurements[1][1] += 1	

		# if 'row' qubit is 1
		else:
			# pixel is 10
			if (a_res == False):
				if (c_res == False):
					measurements[2][0] += 1
				else:
					measurements[2][1] += 1
			# pixel is 11	
			else:
				if (c_res == False):
					measurements[3][0] += 1
				else:
					measurements[3][1] += 1	

	# using the probability of measuring zero for each pixel, can estimate theta
	angles = []
	for i in range(4):
		zero_prob = measurements[i][0]/(measurements[i][0] + measurements[i][1])
		angles.append(acos(sqrt(zero_prob)))

	return angles

# this function creates the FRQI state for the image
def run(angles, num_shots):

	# create the qubits to be used in the circuit
	a = cirq.NamedQubit("a")
	b = cirq.NamedQubit("b")
	c = cirq.NamedQubit("c")

	# store the gates to be used when creating the circuit
	x = cirq.X
	CRy = []
	NegCRy = []
	# need to store a controlled Ry gate for each angle, as well as a negative angle one
	for ang in angles:
		CRy.append(cirq.ControlledGate(RotYGate(rads=ang)))
		NegCRy.append(cirq.ControlledGate(RotYGate(rads=-ang)))
	
	# create the circuit and add H operations to it
	circuit = cirq.Circuit()
	circuit.append(H.on(a))
	circuit.append(H.on(b))

	# for every angle, add to the circuit the encoding of that angle
	for i in range(len(angles)):

		# to make sure we are transforming the correct vector, need to NOT certain qubits
		circuit.append(x.on(a))

		if(i%2 == 0):
			circuit.append(x.on(b))

		# The C^2-Ry operation
		circuit.append(CRy[i].on(a, c))
		circuit.append(CNOT.on(a, b))
		circuit.append(NegCRy[i].on(b, c))
		circuit.append(CNOT.on(a, b))
		circuit.append(CRy[i].on(b, c))

	# measure all of the qubits
	circuit.append(cirq.measure(a))
	circuit.append(cirq.measure(b))
	circuit.append(cirq.measure(c))

	simulator = cirq.google.XmonSimulator()

	# run the circuit and get measurements
	trials = simulator.run(circuit, repetitions=num_shots)

	# use the measurements to recover the angles encoding the colors
	recovered_angles = probs(trials, num_shots)

	return recovered_angles