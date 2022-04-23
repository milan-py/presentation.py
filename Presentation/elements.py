class NoneError(Exception):

	def __init__(self, message):
		super().__init__()

	def __str__(self):
		return f"Presentation NoneError: {self.message}"

class Element:
	def __init__(self, body = None, css = None):
		self.css = css
		self.body = body

	def __str__(self):
		return "Html Element, Use element.htmlOut for the actual output"

	@property
	def htmlOut(self):
		return self.childHtml

	@property
	def childHtml(self):
		return "\n".join(f"\t{i.htmlOut}" for i in self.body)

	def writeFile(self, file):
		with open(file, "w") as f:
			f.write(self.htmlOut)

class RawTag(Element):
	
	def __init__(self, tag: str = None, body: str = None, css = None, properties: dict = None):
		super().__init__(css = css, body = body)
		self.tag = tag
		self.htmlProperties = properties

	@property
	def __propertiesFormatted(self):
		output = ""
		if(self.htmlProperties == None):
			return output
		for key, value in zip(self.htmlProperties, self.htmlProperties.values()):
			output += f"{key} = '{value}' "
		return output

	@property
	def htmlOut(self):
		if self.tag == None:
			raise NoneError("A tag has to be provied")
		elif not type(self.tag) is str:
			raise TypeError("The tag must be a string")  
		return f"<{self.tag} {self.__propertiesFormatted}>{self.childHtml}</{self.tag}>"

	@property
	def childHtml(self):
		return self.body

class CustomTag(Element):

	def __init__(self, tag: str = None, body: list = None, css = None, properties: dict = None):
		super().__init__(body = body, css = css)
		self.tag = tag
		self.htmlProperties = properties

	@property
	def __propertiesFormatted(self):
		output = ""
		if(self.htmlProperties == None):
			return output
		for key, value in zip(self.htmlProperties, self.htmlProperties.values()):
			output += f"{key} = '{value}' "
		return output

	@property
	def htmlOut(self):
		if self.tag == None:
			raise NoneError("A tag has to be provied")
		elif not type(self.tag) is str:
			raise TypeError("The tag must be a string")  
		return f"<{self.tag} {self.__propertiesFormatted}>{self.childHtml}</{self.tag}>"

class Div(CustomTag):

	def __init__(self, body: list = None, css=None, properties: dict = None):
		super().__init__("div", body, css, properties)