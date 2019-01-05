import tkinter as tk
from tkinter import ttk
import y

class BankDetails(ttk.Frame):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
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
		
		ttk.Label(self,text='Bank Details').grid(row=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text="Bank Name*").grid(row=2,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankId"]).grid(row=2,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Branch Name*').grid(row=2,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankBranchName"]).grid(row=2,column=4,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Account Name.').grid(row=3,column=1,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankAccountName"]).grid(row=3,column=2,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Label(self,text='Account No*').grid(row=3,column=3,sticky=(tk.N+tk.E+tk.W+tk.S))
		ttk.Entry(self,textvariable=self.variables["formFiveBankAccountNo"]).grid(row=3,column=4,sticky=(tk.N+tk.E+tk.W+tk.S))
		



class Application(tk.Tk):
	
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		#scrollbar
		self.frame=y.VerticalScrolledFrame(self)
		self.frame.pack(fill='both',expand='true')
		self.Question=[]
		for i in range(2):
			self.Question.append(ttk.Frame(self.frame.interior))
			self.Question[i].grid(row=i,column=0,sticky=tk.W)
			tk.Grid.rowconfigure(self.frame.interior,i,weight=1)
		self.data={}
		#que1
		self.data["que1"]=tk.StringVar()
		ttk.Label(self.Question[0],text="1.Whether separate RERA Bank Account has been opened as envisaged in Gujarat RERA Bank Account Direction, 2018?").grid(row=1,column=1,sticky=tk.W)
		ttk.Combobox(self.Question[0],textvariable=self.data["que1"],values=["yes","no"]).grid(row=1,column=2,sticky=tk.W)
		#que2
		ttk.Label(self.Question[1],text="2. Details of RERA Bank Account as registered with Gujarat RERA (mention all the bank accounts if there has been a change in Bank Account registered with RERA)").grid(row=1,column=1)
		ttk.Button(self.Question[1],text="Add More",command=self.AddBankDetails).grid(row=2,column=1,sticky=tk.W)
		self.BankDetailsFrame=ttk.Frame(self.Question[1])
		self.BankDetailsFrame.grid(row=3,column=1,sticky=tk.W)
		
	def AddBankDetails(self):
		BankDetails(self.BankDetailsFrame).grid(sticky=tk.W)
		
		

		
app=Application()
app.mainloop()		