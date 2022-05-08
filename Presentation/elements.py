from Presentation.utils import *
import Presentation.cssElements as cssElements

class Element:

	def __init__(self, body = None):
		self.css = cssElements # FIXME What the hell does this do?
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
	
	def __init__(self, tag: str = None, body: str = None, properties: dict = None):
		super().__init__(body = body)
		self.tag = tag
		self.htmlProperties = properties

	@property
	def propertiesFormatted(self):
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
		return f"<{self.tag} {self.propertiesFormatted}>{self.childHtml}</{self.tag}>"

	@property
	def childHtml(self):
		return self.body

class CustomTag(Element):

	def __init__(self, tag: str = None, body: list = None, properties: dict = None):
		super().__init__(body = body)
		self.tag = tag
		self.htmlProperties = properties
		if self.htmlProperties == None:
			self.htmlProperties = dict()

	@property
	def propertiesFormatted(self):
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
		return f"<{self.tag} {self.propertiesFormatted}>{self.childHtml}</{self.tag}>"

class Div(CustomTag):
	def __init__(self, body: list = None, properties: dict = None):
		super().__init__("div", body, properties)

import base64
class Img(RawTag):
	def __init__(self, file: str, includeindoc: bool = None, alt: str = None, cssClass: str = None):  
		self.includeindoc = includeindoc

		self.cssClass = cssClass
		self.file = file
		self.alt = alt
		super().__init__("img", body = "", properties = {"alt" : alt, "class" : cssClass})

	@property
	def htmlOut(self):
		if self.tag == None:
			raise NoneError("A tag has to be provied")
		elif not type(self.tag) is str:
			raise TypeError("The tag must be a string")
		if self.includeindoc == None:
			self.includeindoc = False

		self.htmlProperties["alt"] = self.alt
		if self.includeindoc:
			with open(self.file, "rb") as f:
				encoded = str(base64.b64encode(f.read()))
				self.htmlProperties["src"] = f"data:image/png;base64, {encoded[2:-1]}"
		else:
			self.htmlProperties["src"] = self.file 
		
		if self.alt == None:
			self.alt = ""

		if self.cssClass == None:
			self.cssClass = ""

		self.htmlProperties["class"] = self.cssClass
		self.htmlProperties["alt"] = self.alt


		return f"<{self.tag} {self.propertiesFormatted}>{self.childHtml}</{self.tag}>"

		