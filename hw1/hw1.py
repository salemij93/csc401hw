def kineticEnergyandMomentum():
	#create empty dict for output
	qAs = {}
	questions = ('What is the mass of the object?','What is the velocity of the object?')
	physicalProperties = ('mass', 'velocity')
	#loop over questions and physicalProperties to create dict
	#also tests for correct values
	for question, physicalProperty in zip(questions,physicalProperties):
		while True:
			try:
				qAs[physicalProperty] = float(input(question+'\n'))
				if qAs[physicalProperty]<0 and 'mass' in physicalProperty:
					print('So you think you can have negative mass?')
					continue
				elif qAs[physicalProperty]<0 and 'velocity' in physicalProperty:
					print('velocity cannot be negative!')
				else:
					break
			except Exception:
				if 'mass' in physicalProperty:
					print('Mass is usually a number?')
				else:
					print('velocity is probably a number?')
	#assign output values
	kineticEnergy = (qAs['mass'] * qAs['velocity']**2)/2
	momentum = qAs['mass'] * qAs['velocity']
	return kineticEnergy, momentum
#call function and print answers
a,b = kineticEnergyandMomentum()
print('Kinetic Energy: ',a)
print('Momentum: ',b)