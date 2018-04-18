class Apartment:
	"""docstring for Apartment"""
	def __init__(self, aptNumber, numOfBaths, numOfBedrooms, rent):

		self.setRent(rent)
		self.setApartmentNumber(aptNumber)
		self.setNumberOfBathrooms(numOfBaths)
		self.setNumberOfBedrooms(numOfBedrooms)
		
	def setRent(self,rent):
		try:
			self.rent = float(rent)
			if self.rent < 0.0:
				raise Exception
		except Exception:
			self.rent = 0.0		
	def setApartmentNumber(self,aptNumber):
		try:
			self.aptNumber = int(aptNumber)
			if self.aptNumber < 0:
				raise Exception
		except Exception:
			self.aptNumber = 0		
	def setNumberOfBathrooms(self,numOfBaths):
		try:
			self.numOfBaths = int(numOfBaths)
			if self.numOfBaths < 0:
				raise Exception
		except Exception:
			self.numOfBaths = 0
		
	def setNumberOfBedrooms(self,numOfBedrooms):
		try:
			self.numOfBedrooms = int(numOfBedrooms)
			if self.numOfBedrooms < 0:
				raise Exception
		except Exception:
			self.numOfBedrooms = 0 
		
	def getRent(self):
		return self.rent
	def getApartmentNumber(self):
		return self.aptNumber
	def getNumberOfBathrooms(self):
		return self.numOfBaths
	def getNumberOfBedrooms(self):
		return self.numOfBedrooms

def getApartmentData(fileName):
	data = []
	try:
		logFile = open(fileName,'r')
	except Exception:
		# logFile = open('dateLog', 'ab')
		print('Data not formatted properly')
	for line in logFile.readlines():
		y = line
		data.append(y.strip('\n').split(','))
	logFile.close()
	return data

w = getApartmentData('ApartmentData.txt')

allApartments = []
for i in w:
	allApartments.append(Apartment(i[0],i[1],i[2],i[3]))

def userApartmentWants(wantAptlst):
	apartmentsFound = []
	for aa in range(len(allApartments)):
		if wantAptlst[0] <= allApartments[aa].numOfBedrooms and wantAptlst[1] <= allApartments[aa].numOfBaths and wantAptlst[2] >= allApartments[aa].rent:
			apartmentsFound.append(allApartments[aa])
	return apartmentsFound

def mainMenu(option):
	if option is '1':
		newaptnum = input('Enter new Apartment Number\n')
		newaptbeds = input('Enter new Apartment Number of bedrooms\n')
		newaptbaths = input('Enter new Apartment Number of bathrooms\n')
		newaptrent = input('Enter new Apartment Rent\n')
		allApartments.append(Apartment(newaptnum,newaptbaths,newaptbeds,newaptrent))
	elif option is '2':
		while True:
			try:
				minaptbeds = int(input('Enter min Apartment Number of bedrooms\n'))
				if minaptbeds < 0:
					continue
				else:
					break
			except Exception:
				continue

		while True:
			try:
				minaptbaths = int(input('Enter min Apartment Number of bathrooms\n'))
				if minaptbaths < 0:
					continue
				else:
					break
			except Exception:
				continue

		while True:
			try:
				maxaptrent = float(input('Enter max Apartment Rent\n'))
				if maxaptrent < 0:
					continue
				else:
					break
			except Exception:
				continue
		return [minaptbeds,minaptbaths,maxaptrent]

x = input('Select 1 for new Apartment or 2 for finding Apartments\n')
if x is '1':
	mainMenu('1')
elif x is '2':
	apartmentCriteria = mainMenu('2')
	selectedaparts = userApartmentWants(apartmentCriteria)
else:
	print('not a valid menu choice')	
if len(selectedaparts) > 0:
	print('Number: ', '\t', 'Rent: ', '\t', 'Bedrooms: ', '\t', 'Bathrooms: ')
	for n in range(len(selectedaparts)):
		print(selectedaparts[n].aptNumber,'\t\t',  '{:5.2f}'.format(selectedaparts[n].rent),'\t\t', selectedaparts[n].numOfBedrooms, '\t\t', selectedaparts[n].numOfBaths)