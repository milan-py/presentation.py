import Presentation.constants as constants

class Element:
	def formatStyle(self):	
		string = ""
		for i in self.style.keys():
			string = string + f"{i}: {self.style[i]};\n"
		return string

class Image(Element):
	def __init__(self, style = {"max-height" : "100%", "max-width" : "100%", "float" : "none", "width" : "none", "border-radius" : "10px"}):
		self.style = style
class Header(Element):
	def __init__(self, content, style = {"margin-bottom" : "-30px"}):
		self.content = content
		self.style = style

	def __str__(self):
		return f"Header({self.content})"

class Category(Element):

	def __init__(self, title, style = {"color" : "black"}):
		self.title = title
		self.style = style
		self.content = ""

	def __str__(self):
		return f"Category({self.title})"

	def setContent(self):
		self.htmlOutput = ""
		print(f"output before: {self.htmlOutput if self.htmlOutput != '' else 'Nothing'}")
		self.htmlOutput = self.htmlOutput + constants.HTML_CATEGORY.format(title = self.title, style = self.formatStyle())
		self.htmlOutput = self.htmlOutput.replace("categoryBody", self.content)
		open("temp.html", "a", encoding = "utf-8").write(f"======\n{self.htmlOutput}\n======")

		