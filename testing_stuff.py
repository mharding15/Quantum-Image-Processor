# Import the Qiskit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer

num_measurements = 10000

def run():
	
	# Create a Quantum Register with 2 qubits.
	q = QuantumRegister(2)
	# Create a Classical Register with 2 bits.
	c = ClassicalRegister(2)
	# Create a Quantum Circuit
	qc = QuantumCircuit(q, c)

	# Add a H gate on qubit 0, putting this qubit in superposition.
	qc.h(q[0])
	qc.h(q[1])

	qc.measure(q, c)

	#print("Aer backends: ", Aer.backends())

	backend_sim = Aer.get_backend('qasm_simulator')
	
	job_sim = execute(qc, backend_sim, shots=num_measurements)
	result_sim = job_sim.result()
	
	print(result_sim.get_counts(qc))
