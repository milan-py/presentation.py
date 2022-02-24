import constants

class Image:
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

		self.insertTitle()

	def insertTitle(self):
		self.finalOutput = self.finalOutput + constants.HTML_CATEGORY.format(title = self.title)

	def setContent(self, content):
		self.finalOutput = self.finalOutput.replace("categoryBody", content)
		

class Presentation:


	def __init__(self, title, header, backgroundImage = "none", backgroundColor = "none", fontFamiliy = "Arial, Helvetica, sans-serif", credits = ""):
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

		self.initHtml()

	def addCategory(self, categ):
		self.categories.append(categ)

	def addcredits(self):
		self.finalOutput = self.finalOutput + constants.HTML_OWN_CREDITS.format(credits = self.credits + ((" - " if self.credits != "" else "") + "von Milan Bömer programmiert"))


	def initHtml(self):
		self.finalOutput = self.finalOutput + constants.HTML_HEAD.format(title = self.header, header = self.title)

	def initJss(self):
		self.addcredits()

		css = constants.CSS_STYLE.replace("backgroundImage", f'url("{self.backgroundImage}")' if self.backgroundImage != "none" else "none")
		css = css.replace("fontFamiliy", self.fontFamiliy)
		css = css.replace("backgroundColor", self.backgroundColor)
		if not self.display:
			css = css.replace("/* NODISPLAY_PLACEHOLDER */", constants.CSS_NODISPLAY)
		self.finalOutput = self.finalOutput + css

		self.finalOutput = self.finalOutput + constants.JAVASCRIPT_HTML_END
	
	def insertCategories(self):
		finalString = ""

		categoryString = ""

		for i in self.categories:
			categoryString = categoryString + i.finalOutput

		finalString = constants.HTML_CATEGORY_DIV.format(categories = categoryString)

		self.finalOutput = self.finalOutput + finalString
		
	def create(self):
		self.insertCategories()
		self.initJss()
		self.finalOutput = self.centerImage.setProperties("centerMaxHeight", "centerMaxwidth", "centerWidth", "centerFloat", self.finalOutput)
		self.finalOutput = self.previewImage.setProperties("previewMaxHeight", "previewMaxWidth", "previewWidth", "previewFloat", self.finalOutput)

	def out(self, filename):
		with open(filename, "w", encoding = "utf-8") as f:
			f.write(self.finalOutput)
		print(self.finalOutput)