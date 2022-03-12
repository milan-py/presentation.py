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

		self.finalOutput = ""

		self.__insertTitle()
		self.__content = ""

	def __insertTitle(self):
		self.finalOutput = self.finalOutput + constants.HTML_CATEGORY.format(title = self.title)

	@property
	def content(self):
		return self.__content
	
	@content.setter
	def content(self, content):
		self.finalOutput = self.finalOutput.replace("categoryBody", content)
		self.__content = content
		

class Presentation:


	def __init__(self, title: str, header: str, backgroundImage = "none", backgroundColor = "none", fontFamiliy = "Arial, Helvetica, sans-serif", credits = ""):
		self.title = title
		self.header = header
		self.backgroundImage = backgroundImage
		self.backgroundColor = backgroundColor
		self.fontFamiliy = fontFamiliy
		self.credits = credits


		self.finalOutput = ""
		self.categoryString = ""

		self.categories = []
		self.previewImage = Image()
		self.centerImage = Image()

		self.display = True

		self.__initHtml()

	def __addcredits(self):
		self.finalOutput = self.finalOutput + constants.HTML_OWN_CREDITS.format(credits = self.credits + ((" - " if self.credits != "" else "") + "von Milan Bömer programmiert")) # adds credits to the presentation in the bottom left corner


	def __initHtml(self):
		self.finalOutput = self.finalOutput + constants.HTML_HEAD.format(title = self.header, header = self.title)

	def __initJss(self):
		self.__addcredits()

		css = constants.CSS_STYLE.replace("backgroundImage", f'url("{self.backgroundImage}")' if self.backgroundImage != "none" else "none") # sets the brackground image
		css = css.replace("fontFamiliy", self.fontFamiliy) # sets the font family
		css = css.replace("backgroundColor", self.backgroundColor) # set the background color
		if not self.display:
			css = css.replace("/* NODISPLAY_PLACEHOLDER */", constants.CSS_NODISPLAY) # removes the content in the category preview
		self.finalOutput = self.finalOutput + css # adds the css code to the final output

		self.finalOutput = self.finalOutput + constants.JAVASCRIPT_HTML_END
	
	def __insertCategories(self): # inserts the categories to the output
		finalString = ""

		categoryString = ""

		for i in self.categories:
			categoryString = categoryString + i.finalOutput

		finalString = constants.HTML_CATEGORY_DIV.format(categories = categoryString)

		self.finalOutput = self.finalOutput + finalString
		
	def create(self): # sets everything up. Has to be executed before out() and after setting all properties
		self.__insertCategories()
		self.__initJss()
		self.finalOutput = self.centerImage.setProperties("centerMaxHeight", "centerMaxwidth", "centerWidth", "centerFloat", self.finalOutput)
		self.finalOutput = self.previewImage.setProperties("previewMaxHeight", "previewMaxWidth", "previewWidth", "previewFloat", self.finalOutput)

	def write_html(self, filename: str, **kwargs): # outputs the code to the console and a file 
		with open(filename, "w", encoding = "utf-8") as f:
			if len(kwargs) > 0 and kwargs["compress"] == True:
				f.write(self.finalOutput.replace("\t", "").replace("    ", "").replace("\n", ""))
			else:
				f.write(self.finalOutput)
		print(self.finalOutput)