from tkinter import *
class LoanCalculator:

	def __init__(self):
		window = Tk() # Create a window
		window.title("Loan Calculator")
		# create the input boxes.
		Label(window, font=25, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W)
		Label(window, font=25, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
		Label(window, font=25, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
		Label(window, font=25, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
		Label(window, font=25, text = "Total Payment").grid(row = 5,	column = 1, sticky = W)

		#taking inputs
		self.annualInterestRateVar = StringVar() 
		Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)
		self.numberOfYearsVar = StringVar()

		Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)
		self.loanAmountVar = StringVar()

		Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
		self.monthlyPaymentVar = StringVar()
		lblMonthlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)

		self.totalPaymentVar = StringVar()
		lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)
		
		#button
		btComputePayment = Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 6, column = 2, sticky = E) 
		window.mainloop()

	# computing total payment.
	def computePayment(self):				
		monthlyPayment = self.getMonthlyPayment(
		float(self.loanAmountVar.get()),
		float(self.annualInterestRateVar.get()) / 1200,
		int(self.numberOfYearsVar.get()))

		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
			                            * int(self.numberOfYearsVar.get())
		self.totalPaymentVar.set(format(totalPayment, '10.2f'))

	def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears): 
		# computing monthly payment.
		monthlyPayment = loanAmount * monthlyInterestRate / (1
		- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
		return monthlyPayment;
		root = Tk() #widget

LoanCalculator()