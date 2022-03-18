import Presentation.constants as constants

class Image: # class for storing css properties for images 
	def __init__(self, maxHeight = 100, maxWidth = 100, float = "none", width = "none"):
		self.maxHeight = maxHeight
		self.maxWidth = maxWidth
		self.float = float
		self.width = width

	def setProperties(self, rmaxHeight, rmaxWidth, rWidth, rfloat, string):
		string = string.replace(rmaxHeight, str(self.maxHeight))
		string = string.replace(rmaxWidth, str(self.maxWidth))
		string = string.replace(rWidth, f"{self.width}%" if self.width != "none" else "none")
		string = string.replace(rfloat, self.float)

		return string
		
class Category:

	def __init__(self, title):
		self.title = title

		self.htmlOutput = ""

		self.__insertTitle()
		self.content = ""

	def __str__(self):
		return f"Category({self.title})"

	def __insertTitle(self):
		self.htmlOutput = self.htmlOutput + constants.HTML_CATEGORY.format(title = self.title)

	def setContent(self):
		self.htmlOutput = self.htmlOutput.replace("categoryBody", self.content)
		

class Presentation:


	def __init__(self, title: str, header: str, backgroundImage = "none", backgroundColor = "none", fontFamiliy = "Arial, Helvetica, sans-serif", credits = "", columns = 3):
		self.title = title
		self.header = header
		self.backgroundImage = backgroundImage
		self.backgroundColor = backgroundColor
		self.fontFamiliy = fontFamiliy
		self.credits = credits
		self.columns = columns


		self.htmlOutput = ""
		self.categoryString = ""

		self.categories = []
		self.previewImage = Image()
		self.centerImage = Image()

		self.display = True

		self.__initHtml()

	def __str__(self):
		return f"Presentation({self.title}, {self.header}); categories: {', '.join(category.title for category in self.categories)}"

	def __addcredits(self):
		self.htmlOutput = self.htmlOutput + constants.HTML_OWN_CREDITS.format(credits = self.credits + ((" - " if self.credits != "" else "") + "gemacht mit presentation.py")) # adds credits to the presentation in the bottom left corner


	def __initHtml(self):
		self.htmlOutput = self.htmlOutput + constants.HTML_HEAD.format(title = self.header, header = self.title)

	def __initJss(self):
		self.__addcredits()

		css = constants.CSS_STYLE.replace("backgroundImage", f'url("{self.backgroundImage}")' if self.backgroundImage != "none" else "none") # sets the brackground image
		css = css.replace("fontFamiliy", self.fontFamiliy) # sets the font family
		css = css.replace("backgroundColor", self.backgroundColor) # set the background color
		if not self.display:
			css = css.replace("/* NODISPLAY_PLACEHOLDER */", constants.CSS_NODISPLAY) # removes the content in the category preview
		self.htmlOutput = self.htmlOutput + css # adds the css code to the final output

		self.htmlOutput = self.htmlOutput + constants.JAVASCRIPT_HTML_END
	
	def __insertCategories(self): # inserts the categories to the output
		finalString = ""
		categoryString = ""
		

		i = 0
		while i < len(self.categories):
			columnString = ""
			for column in range(self.columns):
				if i >= len(self.categories):
					continue
				self.categories[i].setContent()
				columnString = columnString + self.categories[i].htmlOutput
				i += 1
			categoryString = categoryString + constants.HTML_ROW.format(rowcontent = columnString)

		finalString = constants.HTML_CATEGORIES_CENTERCONTAINER.format(categories = categoryString)

		self.htmlOutput = self.htmlOutput + finalString
		
	def create(self): # sets everything up. Has to be executed before out() and after setting all properties
		self.__insertCategories()
		self.__initJss()
		self.htmlOutput = self.centerImage.setProperties("centerMaxHeight", "centerMaxwidth", "centerWidth", "centerFloat", self.htmlOutput)
		self.htmlOutput = self.previewImage.setProperties("previewMaxHeight", "previewMaxWidth", "previewWidth", "previewFloat", self.htmlOutput)

	def writeHtml(self, filename: str, **kwargs): # outputs the code to a file 
		with open(filename, "w", encoding = "utf-8") as f:
			if len(kwargs) > 0 and kwargs["compressed"] == True:
				f.write(self.htmlOutput.replace("\t", "").replace("    ", "").replace("\n", ""))
			else:
				f.write(self.htmlOutput)