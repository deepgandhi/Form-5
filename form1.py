import tkinter as tk
from tkinter import ttk
import y
import json


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
		ttk.Entry(self,textvariable=self.variables['formFiveBankWithdrawals']).grid(row=3,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Withdrawals during the period*').grid(row=4,column=0,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables['formFiveBankWithdrawals']).grid(row=4,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Closing Balance*').grid(row=4,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self).grid(row=4,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		
		
	def get(self):
		data={}
		for keys,variable self.variables.items():
			data[keys]=variable.get()
		return data



class Application(tk.Tk):
	
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		#scrollbar
		self.frame=y.VerticalScrolledFrame(self)
		self.frame.pack(fill='both',expand='true')
		self.Question=[]
		for i in range(3):
			self.Question.append(ttk.Frame(self.frame.interior))
			self.Question[i].grid(row=i,column=0,sticky=tk.W)
			tk.Grid.rowconfigure(self.frame.interior,i,weight=1)
		self.data={}
		#que1
		self.data["que1"]=tk.StringVar()
		ttk.Label(self.Question[0],text="1.Whether separate RERA Bank Account has been opened as envisaged in Gujarat RERA Bank Account Direction, 2018?").grid(row=1,column=1,sticky=tk.W)
		ttk.Combobox(self.Question[0],textvariable=self.data["que1"],values=["Yes","No"]).grid(row=2,column=1,sticky=tk.W)
		#que2
		ttk.Label(self.Question[1],text="2. Details of RERA Bank Account as registered with Gujarat RERA (mention all the bank accounts if there has been a change in Bank Account registered with RERA)").grid(row=1,column=1,sticky=tk.W)
		ttk.Button(self.Question[1],text="Add More",command=self.AddBankDetails).grid(row=2,column=1,sticky=tk.W)
		self.BankDetailsFrame=ttk.Frame(self.Question[1])
		self.BankDetailsFrame.grid(row=3,column=1,sticky=tk.W)
		#que3
		self.data['que3']=tk.StringVar()
		ttk.Label(self.Question[2],text='3.	In case of change in RERA Bank Account as indicated above, whether due approval following prescribed documentation was taken from Gujarat RERA under the Gujarat RERA Bank Account Directions, 2018?').grid(row=1,column=1,sticky=tk.W)
		ttk.Combobox(self.Question[2],textvariable=self.data['que3'],values=['Yes','No','Not Changed']).grid(row=2,column=1,sticky=tk.W)
		
		
		ttk.Button(self.frame.interior,text="SAVE",command=self._on_save).grid(row=3)
		
		
	def AddBankDetails(self):
		BankDetails(self.BankDetailsFrame).grid(sticky=tk.W)
		
		
	def _on_save(self):
		data1={}
		for keys,variable in self.data.items():
			data1[keys]=variable.get()
		print(json.dumps(data1))

		
app=Application()
app.mainloop()		