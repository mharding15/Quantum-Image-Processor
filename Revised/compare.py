import cirq_compare
import qiskit_compare
from scipy import stats
import numpy as np
import time

def avg(list):

	size = len(list)

	sum = list[0]
	for i in range(1, len(list)):
		sum += list[i]

	return sum/size

def convert(list):

	array = np.zeros(len(list))
	i = 0
	for x in list:
		array[i] = x
		i += 1

	return array

if __name__ == "__main__":

	cirq_times = []
	cirq_accs = []
	
	print("cirq")
	for i in range(100000, 1000001, 100000):

		time, acc = cirq_compare.run(i)

		cirq_times.append(time)
		cirq_accs.append(acc)

	qiskit_times = []
	qiskit_accs = []

	print("qiskit")
	for i in range(100000, 1000001, 100000):

		time, acc = qiskit_compare.run(i)

		qiskit_times.append(time)
		qiskit_accs.append(acc)

	print("Avg time for cirq: ", avg(cirq_times))
	print("Avg error for cirq: ", avg(cirq_accs))
	print("Avg time for qiskit: ", avg(qiskit_times))
	print("Avg error for qiskit: ", avg(qiskit_accs))

	cirq_time_array = convert(cirq_times)
	cirq_accs_array = convert(cirq_accs)
	qiskit_time_array = convert(qiskit_times)
	qiskit_accs_array = convert(qiskit_accs)
	
	print("Time stats:")
	print(stats.ttest_ind(cirq_time_array, qiskit_time_array))

	print("Error stats:")
	print(stats.ttest_ind(cirq_accs_array, qiskit_accs_array))
