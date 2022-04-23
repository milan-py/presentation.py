

class Presentation:
	def __init__(self, header, title: str, backgroundImage = None, backgroundColor = None, fontFamiliy = None, credits = None, columns = None):
		self.header = header
		self.title = title
		self.backgroundImage = backgroundImage
		self.backgroundColor = backgroundColor
		self.fontFamiliy = fontFamiliy
		self.credits = credits
		self.columns = columns

		self.htmlOutput = ""

		self.categories = []

		self.__initHtml()

	def __str__(self):
		return f"Presentation({self.header.content}, {self.title}); categories: {', '.join(category.title for category in self.categories)}"