def testcase(first_row, first_arrangement, second_row, second_arrangement):
	first_options = first_arrangement[first_row -1]
	second_options = second_arrangement[second_row -1]
	chosen = []
	for card1 in first_options:
		for card2 in second_options:
			if int(card1) == int(card2):
				chosen.append(card1)
	if (len(chosen) > 1):
		return "Bad Magician!"
	elif (len(chosen) == 0):
		return "Volunteer Cheated!"
	else:
		return chosen[0]

def test_all_cases():
	case_list = open('A-small-practice.in')
	num_of_cases = int(case_list.readline())
	output = ''
	for x in range(0,num_of_cases):
		first_row = int(case_list.readline())
		first_arrangement = []
		for rows_in_arrangement1 in range(0, 4):
			next = case_list.readline()
			row = next.split()
			first_arrangement.append(row)
		second_row = int(case_list.readline())
		second_arrangement = []
		for rows_in_arrangement2 in range(0, 4):
			next = case_list.readline()
			row = next.split()
			second_arrangement.append(row)
		output = output + '\nCase #'+ str((x+1)) + ': ' +  testcase(first_row, first_arrangement, second_row, second_arrangement)
	output_file = open("codejamqual_1_output.txt", "w")
	output_file.write(output)
	output_file.close()
	return output_file
test_all_cases()