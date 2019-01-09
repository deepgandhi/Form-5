class validator():
	def __init__(self,entry,variable,value,sublabel,subentry):
		vcmd=entry.register(self._validate)
		invcmd=entry.register(self._invalid)
		
		self.subentry=subentry
		self.sublabel=sublabel
		self.variable=variable
		self.value=value
		
		entry.config(validate="all",validatecommand=(vcmd,'%P','%V'),invalidcommand=(invcmd))

	def _validate(self,proposed,event):
		valid=True
		if event=='focusout':
			if proposed=='Yes' or 'No':
				valid=True
				self.submenu()
			else:
				valid=False
		return valid
	
	def _invalid(self):
		self.variable.set('')
	
	def submenu(self):
		if self.variable.get()==self.value:
			self.subentry.grid()
			self.sublabel.grid()
		else:
			self.subentry.grid_remove()
			self.sublabel.grid_remove()
		
