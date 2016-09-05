def isZero(l):
	return True if len([a for a in l if a != 0]) == 0 else False
def splitPancakes(current):
	state = list(current)
	maxItem = max(state)
	new = maxItem // 2
	reducedMax = maxItem - new
	state[current.index(maxItem)] = reducedMax
	state.append(new)
	return state
def computeSplitGain(result):
	maxItem = max(result)
	return maxItem // 2

i, o = open('B-small-attempt3.in','r'), open('B-small-out3.txt', 'w')
nCases = int(i.readline())
for case_num in range(nCases):
	nDiners = int(i.readline())
	pancakes = [int(a) for a in i.readline().split()]
	#each scenario is played out here.
	result = pancakes
	count = 0
	print(pancakes)
	while not isZero(result):
		gainNormal = len(result)
		gainSpecial = computeSplitGain(result)
		if gainSpecial > gainNormal:
			specialMinuteResult = splitPancakes(result)
			print('special', specialMinuteResult, 'step count: ', count+1, 'gainSpecial', gainSpecial, 'gainNormal', gainNormal)
			result = specialMinuteResult
		elif gainNormal >= gainSpecial:
			normalMinuteResult = [a-1 for a in result if a-1 > 0]
			print('normal', normalMinuteResult, 'step count: ', count+1, 'gainSpecial', gainSpecial, 'gainNormal', gainNormal)
			result = normalMinuteResult
		count += 1
	print('final', count)
	o.write('Case #' + str(case_num+1) + ': ' + str(count)+'\n')



	# while not isZero(result):
	# 	normalMinuteResult = [a-1 for a in result if a > 0]
	# 	gainNormal = len(result)
	# 	gainSpecial = computeSplitGain(result)
	# 	specialMinuteResult = splitPancakes(result)
	# 	if isZero(normalMinuteResult):
	# 		# print('normal', normalMinuteResult)
	# 		result = normalMinuteResult
	# 	elif gainSpecial > gainNormal:
	# 		# print('special', specialMinuteResult)
	# 		result = specialMinuteResult
	# 	elif gainNormal >= gainSpecial:
	# 		# print('normal', normalMinuteResult)
	# 		result = normalMinuteResult
	# 	count += 1
	# o.write('Case #' + str(case_num+1) + ': ' + str(count)+'\n')