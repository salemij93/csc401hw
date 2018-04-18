def calcElectionResults():
	ElectionResults = {}
	totalVotes = 0
	for x in range(5):
		candidate = input('Please enter the last name of a candidate: \n')
		votesOfCandidate = int(input('Please enter the number of votes ' + candidate + ' received. \n'))
		ElectionResults[x] = {'name':candidate,'votes':votesOfCandidate,'percentage':None}
		totalVotes += votesOfCandidate
	maxVotes = 0
	for v in ElectionResults.values():
		percentageOfVotes = 100 * v['votes']/totalVotes
		v['percentage'] = percentageOfVotes
		if v['votes'] > maxVotes:
			maxVotes = v['votes']
			ElectionWinner = v['name']
	print('Name' + '\t\t' + 'Votes Received' + '\t\t' + 'Percentage of Total Vote')
	for items in ElectionResults.values():
		print(items['name'] + '\t\t' + str(items['votes']) + '\t\t\t' + str(items['percentage'])[:5])
	print('Total Votes ' + str(maxVotes))
	print('The Winner of the Election is ' + ElectionWinner)

calcElectionResults()