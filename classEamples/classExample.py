def calAverageDailyBal():
	qAs = {}
	questions = ('What is your net balance?','What is your payment?' ,'What is your number of days in the billing cycle?' ,'How many days early did you pay?','What is your interest rate?')
	moneys = ('netBal', 'payment', 'd1', 'd2', 'iRate')

	for question, money in zip(questions,moneys):

		while True:
			try:
				qAs[money] = float(input(question+'\n'))
				break
			except Exception:
				print('Only Input Numbers!')

	avgDailyBal = (qAs['netBal'] * qAs['d1'] - qAs['payment'] * qAs['d2'])/qAs['d1']
	interestAmount = avgDailyBal * qAs['iRate']

	return avgDailyBal, interestAmount

a,b = calAverageDailyBal()
print('Daily Balance: ',a)
print('Daily Interest: ',b)