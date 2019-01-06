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
			
			

class que3(que):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		self.data={}
		self.data=tk.StringVar()
		ttk.Label(self,text="3.In case of change in RERA Bank Account as indicated above, whether due approval following prescribed documentation was taken from Gujarat RERA under the Gujarat RERA Bank Account Directions, 2018?").grid(row=0,column=0,sticky=tk.W)
		ttk.Combobox(self,textvariable=self.data,values=["Yes","No",'Not Changed']).grid(row=1,column=0,sticky=tk.W)
		
	def get(self):
		return self.data.get()
	
	def set(self,data):
		self.data.set(data)