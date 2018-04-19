def calc_day_num_of_year():
	dateList = []
	while True:
		try:
			enteredDate = input('Please enter a date in the format mm-dd-yyyy: \n')
			splitDate = enteredDate.split('-')
			enteredMonth = int(splitDate[0])
			enteredDay = int(splitDate[1])
			enteredYear = int(splitDate[2])
			daysPermonth1 = [31,28,31,30,31,30,31,31,30,31,30,31]
			daysPermonth2 = [31,29,31,30,31,30,31,31,30,31,30,31]
			if len(splitDate) != 3:
				print('Enter a proper date format')
				continue
			elif enteredMonth > 12 or enteredMonth < 1:
				print('enter a valid Month')
				continue
			elif enteredDay > daysPermonth2[enteredMonth-1] or enteredDay > daysPermonth1[enteredMonth-1] or enteredDay < 1:
				print('enter a valid number of days')
				continue
			else:
				#print(splitDate)
				if enteredYear % 4 == 0:
					daysInYeay = sum(daysPermonth2[:enteredMonth-1]) + enteredDay
				else:
					daysInYeay = sum(daysPermonth1[:enteredMonth-1]) + enteredDay
				#print(daysInYeay)
				keepGoing = input('Do you want to add another date? Y/N \n')
				if keepGoing.lower() == 'y':
					dateList.append([enteredDate,daysInYeay])
					continue
				break
		except Exception:
			print('please enter a proper date')
	dateList.append([enteredDate,daysInYeay])
	return dateList

def display_day_num_of_year(listOfDates):
	print('Date' + '\t\t' + 'Day of Year' + '\n')
	for line in listOfDates:
		print(str(line[0]) + '\t' + str(line[1]) +'\n')
	# print(listOfDates)

def save_day_num_of_year(datesToAddToFile):
	try:
		logFile = open('dateLog','xb')
	except Exception:
		logFile = open('dateLog', 'ab')
	for line in datesToAddToFile:
		logFile.write(bytes(str(line[0]) + '\t' + str(line[1]) +'\n','utf-8'))
	logFile.close()
	

def menu():
	a = calc_day_num_of_year()
	display_day_num_of_year(a)
	saveFile = input('Do you want to save the data? Y/N \n')
	if saveFile.lower() == 'y':
		save_day_num_of_year(a)

menu()