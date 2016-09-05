def eval_cookie_time(c, f, x):
	init_rate = 2
	cookie_rate = init_rate
	first_time = x/float(cookie_rate)
	time_to_farm = c/float(cookie_rate)
	second_time = time_to_farm + (x/float((cookie_rate + f)))
	cookie_rate = cookie_rate + f
	while first_time > second_time:
		first_time = second_time
		time_to_farm = time_to_farm + c/float(cookie_rate)
		second_time = time_to_farm + (x/float((cookie_rate + f)))
		cookie_rate = cookie_rate + f
	best_time = first_time
	return str(best_time)
def test_all_cases():
	case_list = open('B-small-practice.in')
	num_of_cases = int(case_list.readline())
	output = ''
	for index in range(0,num_of_cases):
		nextline = case_list.readline()
		inputs = nextline.split()
		c = float(inputs[0])
		f = float(inputs[1])
		x = float(inputs[2])
		case_num = index + 1
		output = output + "\nCase #" + str(case_num) + ": " + eval_cookie_time(c,f,x)
	output = output[1:]	
	output_file = open("codejamqual_2_smalloutput.txt", "w")
	output_file.write(output)
	output_file.close()
	return output_file
test_all_cases()

