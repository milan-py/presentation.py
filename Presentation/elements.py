import Presentation.constants as constants

class Element:
	def __init__(self):
		pass

	@property
	def formatStyle(self):	
		string = ""
		for i in self.style.keys():
			string = string + f"\t\t\t{i}: {self.style[i]};\n"
		return string

class Image(Element):
	def __init__(self, *args):
		if len(args) > 0:
			self.style = args[0]
		else:
			self.style = {"max-height" : "100%", "max-width" : "100%", "float" : "none", "width" : "none", "border-radius" : "10px"}

	def __str__(self):
		return f"Image style: {self.style}"
class Header(Element):
	def __init__(self, content, style = {"margin-bottom" : "-30px"}):
		self.content = content
		self.style = style

	def __str__(self):
		return f"Header({self.content})"

class Category(Element):

	def __init__(self, title, *args):
		self.title = title
		if len(args) > 0:
			self.style = args[0]
		else:
			self.style = {"color" : "black"}
		self.content = ""

	def __str__(self):
		return f"Category({self.title})"

	def setContent(self):
		self.htmlOutput = ""
		self.htmlOutput = self.htmlOutput + constants.HTML_CATEGORY.format(title = self.title, style = self.formatStyle)
		self.htmlOutput = self.htmlOutput.replace("categoryBody", self.content)

		