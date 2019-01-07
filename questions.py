import tkinter as tk
from tkinter import ttk

class que(ttk.Frame):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
	def get(self):
		pass		
	def set(self):
		pass
	def fill(self):
		pass

class que1(que):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		self.data={}
		self.data["que1"]=tk.StringVar()
		ttk.Label(self,text="1.Whether separate RERA Bank Account has been opened as envisaged in Gujarat RERA Bank Account Direction, 2018?").grid(row=0,column=0,sticky=tk.W)
		ttk.Combobox(self,textvariable=self.data["que1"],values=["Yes","No"]).grid(row=1,column=0,sticky=tk.W)
	
	def get(self):
		data={}
		for keys,variables in self.data.items():
			data[keys]=variables.get()
		return data
	
	def set(self,data):
		for keys,variables in self.data.items():
			variables.set(data[keys])

class BankDetails(ttk.Labelframe):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,text="Bank Details",*args,**kwargs)
		self.variables={}
		self.variables["formFiveBankId"]=tk.StringVar()
		self.variables["formFiveBankBranchName"]=tk.StringVar()
		self.variables["formFiveBankAccountName"]=tk.StringVar()
		self.variables["formFiveBankAccountNo"]=tk.IntVar()
		self.variables['formFiveBankAccountType']=tk.StringVar()
		self.variables['formFiveBankIFSCCode']=tk.StringVar()
		self.variables['formFiveBankAcOpenDate']=tk.StringVar()
		self.variables['formFiveOpeningBalDate']=tk.StringVar()
		self.variables['formFiveBankOpeningBal']=tk.IntVar()
		self.variables['formFiveBankDeposit']=tk.IntVar()
		self.variables['formFiveBankWithdrawals']=tk.IntVar()
		
		ttk.Label(self,text="Bank Name*").grid(row=0,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankId"]).grid(row=0,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Branch Name*').grid(row=0,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankBranchName"]).grid(row=0,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Account Name.*').grid(row=1,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankAccountName"]).grid(row=1,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Account No*').grid(row=1,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankAccountNo"]).grid(row=1,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Account Type.*').grid(row=2,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankAccountType']).grid(row=2,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='IFSC Code*').grid(row=2,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankIFSCCode']).grid(row=2,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Opening Balance*').grid(row=3,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankOpeningBal']).grid(row=3,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Deposit during the period*').grid(row=3,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankDeposit']).grid(row=3,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Withdrawals during the period*').grid(row=4,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankWithdrawals']).grid(row=4,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Closing Balance*').grid(row=4,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self).grid(row=4,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		
		
	def get(self):
		data={}
		for keys,variable in self.variables.items():
			data[keys]=variable.get()
		return data
	
	def set(self,data):
		for keys,variable in self.variables.items():
			variable.set(data[keys])
			
			
class que2(que):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		ttk.Label(self,text="2.Details of RERA Bank Account as registered with Gujarat RERA (mention all the bank accounts if there has been a change in Bank Account registered with RERA)").grid(row=0,column=0,sticky=tk.W)
		ttk.Button(self,text="Add More",command=self.AddBankDetails).grid(row=1,column=0,sticky=tk.W)
		self.banks=[]
		self.i=2

	def AddBankDetails(self):
		self.banks.append(BankDetails(self))
		self.banks[-1].grid(row=self.i,column=0,sticky=tk.W)
		self.i+=1
		
	def get(self):
		data=[]
		for bank in self.banks:
			data.append(bank.get())
		return data
		
	def set(self,data):
		for b in range(len(data)):
			self.AddBankDetails()
		i=0
		for bank in self.banks:
			bank.set(data[i])
			i+=1

class que3(que):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		self.data=tk.StringVar()
		ttk.Label(self,text="3.In case of change in RERA Bank Account as indicated above, whether due approval following prescribed documentation was taken from Gujarat RERA under the Gujarat RERA Bank Account Directions, 2018?").grid(row=0,column=0,sticky=tk.W)
		ttk.Combobox(self,textvariable=self.data,values=["Yes","No",'Not Changed']).grid(row=1,column=0,sticky=tk.W)
		
	def get(self):
		return self.data.get()
	
	def set(self,data):
		self.data.set(data)