import tkinter as tk
from tkinter import ttk,filedialog
import y
import json
import questions as q
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Application(tk.Tk):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.frame=y.VerticalScrolledFrame(self)
		self.frame.pack(fill='both',expand='true')
		self.ques={}
		self.ques['que1']=q.que1(self.frame.interior)
		self.ques['que2']=q.que2(self.frame.interior)
		self.ques['que3']=q.que3(self.frame.interior)
		self.ques['que4']=q.que4(self.frame.interior)
		self.ques['que5']=q.que5(self.frame.interior)
		i=0
		for keys,que in self.ques.items():
			que.grid(row=i,column=0,sticky=tk.W)
			i+=1
		ttk.Button(self,text="Save",command=self.get).pack()
		ttk.Button(self,text="Open",command=self.set).pack()
		ttk.Button(self,text="Upload",command=self.upload).pack()
		
		
	def get(self):
		data={}
		for keys,frame in self.ques.items():
			data[keys]=frame.get()
		filename=filedialog.asksaveasfilename(initialdir='D:\programs\selenium python\json',title='Select File',filetypes=(('JSON file','*.json'),))
		if not filename.lower().endswith('.json'):
			filename+='.json'
		file=open(filename,'w')
		file.write(json.dumps(data))
		file.close()
		print(json.dumps(data))
		
	def set(self):
		filename=filedialog.askopenfilename(initialdir='D:\programs\selenium python\json',title='Select File',filetypes=(('JSON file','*.json'),))
		file=open(filename,'r')
		data=json.loads(file.readline())
		file.close()
		for keys,frame in self.ques.items():
			try:
				temp=data[keys]
			except KeyError:
				temp=''
			frame.set(temp)
			
			
	def upload(self):
		driver=webdriver.Chrome()
		driver.get("file:///C:/Users/Hp/Desktop/rera/Project%20Form-5(ANNUAL%20REFPORT%20ON%20STATEMENT%20OF%20ACCOUNTS).html")
		for keys,frame in self.ques.items():
			frame.upload(driver)
		

if __name__=='__main__':
	app=Application()
	app.mainloop()