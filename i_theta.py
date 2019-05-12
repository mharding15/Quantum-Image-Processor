
# coding: utf-8
# In[40]:
import qiskit as qk
from qiskit import Aer,execute
from math import pi, sqrt, acos
from image_testing import r_num, g_num, b_num

num_shots = 100000

def probs(results):

	prob = {}
	
	chars = ["0", "1"]
	for c in chars:
		for d in chars:
			for e in chars:
				state = c + d + e
				if (state in results):
					prob[state] = results[state]/num_shots
				else:
					prob[state] = 0.

	angles = []
	for c in chars:
		for d in chars:
			zero = "0" + c + d
			one = "1" + c + d
			zero_prob = prob[zero]/(prob[zero] + prob[one])
			angles.append(acos(sqrt(zero_prob)))
	
	return angles

def probs4(results):

	prob = {}
	
	chars = ["0", "1"]
	for c in chars:
		for d in chars:
			for e in chars:
				for f in chars:
					for g in chars:
						state = c + "000" + d + e + f + g
						if (state in results):
							prob[state] = results[state]/num_shots
						else:
							prob[state] = 0.
	
	angles = []
	for c in chars:
		for d in chars:
			for e in chars:
				for f in chars:
					zero = "0000" + c + d + e + f
					one = "1000" + c + d + e + f
					zero_prob = prob[zero]/(prob[zero] + prob[one])
					angles.append(acos(sqrt(zero_prob)))
	
	return angles
	
def run(angles):

	qr =qk.QuantumRegister(3)
	cr = qk.ClassicalRegister(3)

	qc= qk.QuantumCircuit(qr,cr)

	#Creating the Hadamard State
	qc.h(qr[0])
	qc.h(qr[1])

	# Circuit for I(theta) starts here
	qc.x(qr[0])
	qc.x(qr[1])

	#pi/4=0.7853
	qc.cu3(angles[0],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[0],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[0],0,0,qr[1],qr[2])

	#pi/12=0.2617
	qc.x(qr[0])

	qc.cu3(angles[1],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[1],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[1],0,0,qr[1],qr[2])

	#pi/6=0.5234
	qc.x(qr[0])
	qc.x(qr[1])

	qc.cu3(angles[2],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[2],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[2],0,0,qr[1],qr[2])

	#pi/16=0.1963
	qc.x(qr[0])

	qc.cu3(angles[3],0,0,qr[0],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(-angles[3],0,0,qr[1],qr[2])
	qc.cx(qr[0],qr[1])
	qc.cu3(angles[3],0,0,qr[1],qr[2])

	qc.barrier(qr)
	qc.measure(qr,cr)

	# In[41]:
	backend_sim = Aer.get_backend('qasm_simulator')
	job_sim = execute(qc, backend_sim, shots=num_shots)
	result_sim = job_sim.result()

	# In[42]:
	counts = result_sim.get_counts(qc)

	new_angles = probs(counts)

	return new_angles

def run_4(angles):

	# can just pass in the same angles as I did for 2x2. No need to double them.
	for i in range(len(angles)):
		angles[i] = 2 * angles[i]

	# we are including 3 ancilla qubits
	qr =qk.QuantumRegister(8)
	cr = qk.ClassicalRegister(8)

	qc= qk.QuantumCircuit(qr,cr)

	#Creating the Hadamard State
	qc.h(qr[0])
	qc.h(qr[1])
	qc.h(qr[2])
	qc.h(qr[3])

	# angle to manipulate the colors by

	for i in range(16):

		qc.x(qr[0])
	
		if (i % 4 == 2):
			qc.x(qr[1])

		if (i == 0 or i == 8):
			qc.x(qr[1])
			qc.x(qr[2])
			qc.x(qr[3])

		if (i == 4 or i == 12):
			qc.x(qr[1])
			qc.x(qr[2])

		qc.ccx(qr[0], qr[1], qr[4])
		qc.ccx(qr[2], qr[4], qr[5])
		qc.ccx(qr[3], qr[5], qr[6])

		qc.cu3(angles[i],0,0,qr[6],qr[7])

		qc.ccx(qr[3], qr[5], qr[6])
		qc.ccx(qr[2], qr[4], qr[5])
		qc.ccx(qr[0], qr[1], qr[4])
		
	"""
	################
	# pixel shifting

	#C3not
	qc.ccx(qr[0], qr[1], qr[4])
	qc.ccx(qr[2], qr[4], qr[5])

	qc.cx(qr[5], qr[3])

	qc.ccx(qr[2], qr[4], qr[5])
	qc.ccx(qr[0], qr[1], qr[4])

	#C2not
	qc.ccx(qr[0], qr[1], qr[2])

	#CNOT
	qc.cx(qr[0], qr[1])

	#NOT
	qc.x(qr[0])

	################
	"""

	qc.barrier(qr)
	qc.measure(qr,cr)

	# In[41]:
	backend_sim = Aer.get_backend('qasm_simulator')
	job_sim = execute(qc, backend_sim, shots=num_shots)
	result_sim = job_sim.result()

	# In[42]:
	counts = result_sim.get_counts(qc)

	#print(counts)

	new_angles = probs4(counts)

	return new_angles




"""
def test():

	for i in range(16):

		angles = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		angles[i] = pi/2

		run_4(angles)
		#print("==============\n", i, "\n==============")

		break
"""
	
def get_xs():

	chars = ["0","1"]
	vals = []

	for i in chars:
		for j in chars:
			for k in chars:
				for l in chars:
					for m in chars:
						for n in chars:
							vals.append(i + j + k + l + m + n)

	total = []
	for i in range(64):

		x_vals = []
		word = vals[i]
		for j in range(6):
			if(word[j] == '0'):
				x_vals.append('x')
			else:
				x_vals.append('_')

		total.append(x_vals)

		for k in range(64):
			for q in range(6):
				if (x_vals[q] == 'x'):
					if (vals[k][q] == '0'):
						new_val = []
						for r in range(6):
							if (r != q):
								new_val.append(vals[k][r])
							else:
								new_val.append('1')
						vals[k] = new_val
					else:
						new_val = []
						for r in range(6):
							if (r != q):
								new_val.append(vals[k][r])
							else:
								new_val.append('0')
						vals[k] = new_val

		#print("================ ", i, " =================")
		#print(vals)

	print(total)

	