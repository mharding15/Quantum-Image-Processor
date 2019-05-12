def print_results(results, num_shots):

	a_meas = results.measurements['a']
	b_meas = results.measurements['b']
	c_meas = results.measurements['c']
	
	res = {}

	for i in range(num_shots):

		str = ""
		if (c_meas[i][0] == False):
			str += '0'
		else:
			str += '1'

		if (b_meas[i][0] == False):
			str += '0'
		else:
			str += '1'

		if (a_meas[i][0] == False):
			str += '0'
		else:
			str += '1'

		if(str not in res):
			res[str] = 1
		else:
			res[str] += 1

	print(res)