def infiniteHousePancakes(diners):
	minutes = 0
	yes4 = False
	smallest = 0
	for diner in diners:
		if (diner > 6):
			n = diner//4
			if diner % 4 == 0:
				n -= 1
			minutes += n + 4
			yes4 = True
			continue
		smallest = diner
	if yes4:
		return minutes
	elif smallest == 4:
		return 3
	elif smallest > 4:
		return 4
	return smallest
i, o = open('B-small-attempt2.in','r'), open('B-small-out2.txt', 'w')
nCases = int(i.readline())
for case_num in range(nCases):
	nDiners = int(i.readline())
	pancakes = [int(a) for a in i.readline().split()]
	count = infiniteHousePancakes(pancakes)
	o.write('Case #' + str(case_num+1) + ': ' + str(count)+'\n')