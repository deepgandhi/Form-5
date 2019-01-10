class validator():
	def __init__(self,entry,variable,value,submenu):
		vcmd=entry.register(self._validate)
		invcmd=entry.register(self._invalid)
		
		self.submenu=submenu
		self.variable=variable
		self.value=value
		
		entry.config(validate="all",validatecommand=(vcmd,'%P','%V'),invalidcommand=(invcmd))

	def _validate(self,proposed,event):
		valid=True
		if event=='focusout':
			if proposed=='Yes' or 'No':
				valid=True
				self._submenu()
			else:
				valid=False
		return valid
	
	def _invalid(self):
		self.variable.set('')
	
	def _submenu(self):
		if self.variable.get()==self.value:
			for s in self.submenu:
				s.grid()
		else:
			for s in self.submenu:
				s.grid_remove()

