
# coding: utf-8
# In[40]:
import qiskit as qk
from qiskit import Aer,execute

pi = 3.14

def run():
	qr =qk.QuantumRegister(3)
	cr = qk.ClassicalRegister(3)

	qc= qk.QuantumCircuit(qr,cr)

	#Creating the Hadamard State

	qc.h(qr[0])
	qc.h(qr[1])

	# Circuit for I(theta) starts here
	qc.x(qr[0])
	qc.x(qr[1])

	angles = [pi/2, 0, pi/4, pi/6]
	#pi/4=0.7853
	qc.cu3(angles[0],0,0,qr[0],qr[2])

	qc.cx(qr[0],qr[1])

	qc.cu3(-angles[0],0,0,qr[1],qr[2])

	qc.cx(qr[0],qr[1])

	qc.cu3(angles[0],0,0,qr[0],qr[2])

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
	job_sim = execute(qc, backend_sim)
	result_sim = job_sim.result()

	# In[42]:

	counts = result_sim.get_counts(qc)
	print(counts)