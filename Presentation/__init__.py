import Presentation.constants as constants
from Presentation.elements import *


		

class Presentation:
	def __init__(self, header: Header, title: str, backgroundImage = "none", backgroundColor = "none", fontFamiliy = "Arial, Helvetica, sans-serif", credits = "", columns = 3, equalSize = False):
		self.header = header
		self.title = title
		self.backgroundImage = backgroundImage
		self.backgroundColor = backgroundColor
		self.fontFamiliy = fontFamiliy
		self.credits = credits
		self.columns = columns
		self.equalSize = equalSize


		self.htmlOutput = ""
		self.categoryString = ""

		self.categories = []
		self.previewImage = Image()
		self.centerImage = Image()

		self.display = True

		self.__initHtml()

	def __str__(self):
		return f"Presentation({self.header.content}, {self.title}); categories: {', '.join(category.title for category in self.categories)}"

	def __addcredits(self):
		self.htmlOutput = self.htmlOutput + constants.HTML_OWN_CREDITS.format(credits = self.credits + ((" - " if self.credits != "" else "") + "gemacht mit presentation.py")) # adds credits to the presentation in the bottom left corner


	def __initHtml(self):
		self.htmlOutput = self.htmlOutput + constants.HTML_HEAD.format(title = self.title, header = self.header.content)

	def __initJss(self):
		self.__addcredits()

		css = constants.CSS_STYLE.replace("backgroundImage", f'url("{self.backgroundImage}")' if self.backgroundImage != "none" else "none") # sets the brackground image
		css = css.replace("fontFamiliy", self.fontFamiliy) # sets the font family
		css = css.replace("backgroundColor", self.backgroundColor) # set the background color
		if not self.display:
			css = css.replace("/* NODISPLAY_PLACEHOLDER */", constants.CSS_NODISPLAY) # removes the content in the category preview
		if self.equalSize:
			css = css.replace("/* EQUAL_SIZE_PLACEHOLDER */", constants.CSS_EQUAL_SIZE) # sets the categories to a equal size
		self.htmlOutput = self.htmlOutput + css # adds the css code to the final output

		self.htmlOutput = self.htmlOutput + constants.JAVASCRIPT_HTML_END
	
	def __insertCategories(self): # inserts the categories to the output
		finalString = ""
		categoryString = ""
		

		i = 0
		while i < len(self.categories):
			columnString = ""
			for y in range(self.columns):
				if i >= len(self.categories):
					break
				self.categories[i].setContent()
				columnString = columnString + self.categories[i].htmlOutput
				# open("temp.html", "a", encoding = "utf-8").write(f"======\n{self.categories[i].htmlOutput}\n======")
				i += 1
			categoryString = categoryString + constants.HTML_ROW.format(rowcontent = columnString)

		finalString = constants.HTML_CATEGORIES_CENTERCONTAINER.format(categories = categoryString)

		self.htmlOutput = self.htmlOutput + finalString
		
	def create(self): # sets everything up. Has to be executed before out() and after setting all properties
		self.__insertCategories()
		self.__initJss()
		self.htmlOutput = self.htmlOutput.replace("centerImageProperties", self.centerImage.formatStyle())
		self.htmlOutput = self.htmlOutput.replace("previewImageProperties", self.previewImage.formatStyle())
		self.htmlOutput = self.htmlOutput.replace("headerProperties", self.header.formatStyle())


	def writeHtml(self, filename: str, **kwargs): # outputs the code to a file 
		with open(filename, "w", encoding = "utf-8") as f:
			if len(kwargs) > 0 and kwargs["compressed"] == True:
				f.write(self.htmlOutput.replace("\t", "").replace("    ", "").replace("\n", ""))
			else:
				f.write(self.htmlOutput)