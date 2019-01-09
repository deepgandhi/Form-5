import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import submenu

def setDate(driver,field,value):
	driver.execute_script('arguments[0].setAttribute("value",arguments[1]);',field,value)

class que(ttk.Frame):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
	def get(self):
		pass		
	def set(self):
		pass
	def upload(self,driver):
		pass

class que1(que):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		self.data={}
		self.data["que1"]=tk.StringVar()
		self.data['que1_1']=tk.StringVar()
		ttk.Label(self,text="1.Whether separate RERA Bank Account has been opened as envisaged in Gujarat RERA Bank Account Direction, 2018?").grid(row=0,column=0,sticky=tk.W)
		q1=ttk.Combobox(self,textvariable=self.data["que1"],values=["Yes","No"])
		q1.grid(row=1,column=0,sticky=tk.W)
		q1_1l=ttk.Label(self,text='1.1.Whether the existing operational bank account was made known at the time of application for registration as RERA Bank Account?')
		q1_1l.grid(row=2,column=0,sticky=tk.W)
		q1_1e=ttk.Combobox(self,textvariable=self.data['que1_1'],values=['Yes','No'])
		q1_1e.grid(row=3,column=0,sticky=tk.W)
		q1_1e.grid_remove()
		q1_1l.grid_remove()
		self.sub=submenu.validator(q1,self.data['que1'],'Yes',q1_1e,q1_1l)
		
	def get(self):
		data={}
		for keys,variables in self.data.items():
			data[keys]=variables.get()
		return data
	
	def set(self,data):
		self.data['que1'].set(data['que1'])
		self.sub._validate(self.data['que1'].get(),'focusout')
		self.data['que1_1'].set(data['que1_1'])

		
	def upload(self,driver):
		temp=driver.find_elements_by_id("question_1_ans")
		if self.data['que1'].get()=='Yes':
			temp[0].click()
			temp=driver.find_elements_by_id("question_1_1_ans")
			if self.data['que1_1'].get()=='Yes':
				temp[0].click()
			else:
				temp[1].click()
		else:
			temp[1].click()



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
		ttk.Label(self,text='Date of Account Opening *').grid(row=3,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankAcOpenDate']).grid(row=3,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Opening Balance Date*').grid(row=3,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveOpeningBalDate']).grid(row=3,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Opening Balance*').grid(row=4,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankOpeningBal']).grid(row=4,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Deposit during the period*').grid(row=4,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankDeposit']).grid(row=4,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Withdrawals during the period*').grid(row=5,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankWithdrawals']).grid(row=5,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Closing Balance*').grid(row=5,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self).grid(row=5,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		
		
	def get(self):
		data={}
		for keys,variable in self.variables.items():
			data[keys]=variable.get()
		return data
	
	def set(self,data):
		for keys,variable in self.variables.items():
			variable.set(data[keys])
			
	def upload(self,driver,i):
		for items,variable in self.variables.items():
			temp=driver.find_elements_by_id(items)
			if items in ('formFiveBankAcOpenDate','formFiveOpeningBalDate'):
				setDate(driver,temp[i],variable.get())
			else:
				temp[i].send_keys(variable.get())
		
			
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
			
	def upload(self,driver):
		addmore=driver.find_element_by_id('bankDetail')
		for i in range(len(self.banks)-1):
			addmore.click()
		i=0
		for bank in self.banks:
			bank.upload(driver,i)
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
		
	def upload(self,driver):
		temp=driver.find_elements_by_id('question_3_ans')
		if self.data.get()=='Yes':
			temp[0].click()
		elif self.data.get()=='No':
			temp[1].click()
		else:
			temp[2].click()
		

class que4(que):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		self.data=tk.StringVar()
		ttk.Label(self,text='4.Whether any of the Form 3 issued during the certificate period mandated deposit of 100% of the money collected from the booking of the project units (refer point 5 of Additional Information for Ongoing Projects of Form 3)?').grid(row=0,column=0,sticky=tk.W)
		ttk.Combobox(self,textvariable=self.data,values=["Yes","No"]).grid(row=1,column=0,sticky=tk.W)
		
	def get(self):
		return self.data.get()
	
	def set(self,data):
		self.data.set(data)
		
	def upload(self,driver):
		temp=driver.find_elements_by_id('question_4_ans')
		if self.data.get()=='Yes':
			temp[0].click()
		else:
			temp[1].click()


class que5(que):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		self.data=tk.StringVar()
		ttk.Label(self,text='5.Whether the required proportion of money collected from the allottees of the project units (as indicated in Form 3) deposited in the RERA Bank Account?').grid(row=0,column=0,sticky=tk.W)
		ttk.Combobox(self,textvariable=self.data,values=["Yes","No"]).grid(row=1,column=0,sticky=tk.W)
		
	def get(self):
		return self.data.get()
	
	def set(self,data):
		self.data.set(data)
		
	def upload(self,driver):
		temp=driver.find_elements_by_id('question_5_ans')
		if self.data.get()=='Yes':
			temp[0].click()
		else:
			temp[1].click()
		