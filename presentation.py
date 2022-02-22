import constants


class Category:

	def __init__(self, title):
		self.title = title

		self.finalOutput = ""

		self.insertTitle()

	def insertTitle(self):
		self.finalOutput = self.finalOutput + constants.HTML_CATEGORY.format(title = self.title)

	def setContent(self, content):
		print("debug 0")
		self.finalOutput = self.finalOutput.replace("categoryBody", content)
		print(self.finalOutput)
		

class Presentation:


	def __init__(self, title, header, backgroundImage = "", fontFamiliy = "Arial, Helvetica, sans-serif"):
		self.title = title
		self.header = header
		self.backgroundImage = backgroundImage
		self.fontFamiliy = fontFamiliy

		self.finalOutput = ""
		self.categoryString = ""

		self.categories = []

		self.display = True

		self.initHtml()

	def addCategory(self, categ):
		self.categories.append(categ)
		# print("CATEGORY:")
		# print(categ.finalOutput)

	def initHtml(self):
		self.finalOutput = self.finalOutput + constants.HTML_HEAD.format(title = self.header, header = self.title)

	def initJss(self):
		css = constants.CSS_STYLE.replace("backgroundImage", self.backgroundImage).replace("fontFamiliy", self.fontFamiliy)
		if not self.display:
			css = css.replace("/* NODISPLAY_PLACEHOLDER */", constants.CSS_NODISPLAY)
		self.finalOutput = self.finalOutput + css

		self.finalOutput = self.finalOutput + constants.JAVASCRIPT_HTML_END
	
	def insertCategories(self):
		finalString = ""

		categoryString = ""

		for i in self.categories:
			# print(f"i.finalOutputs: {i.finalOutput}")
			categoryString = categoryString + i.finalOutput

		finalString = constants.HTML_CATEGORY_DIV.format(categories = categoryString)

		self.finalOutput = self.finalOutput + finalString
		

	def out(self, filename):
		with open(filename, "w", encoding = "utf-8") as f:
			f.write(self.finalOutput)
		print(self.finalOutput)


