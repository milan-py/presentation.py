from Presentation.elements import Element
from Presentation.cssElements import CssTag
class Document(Element):
	STRUCTURE = """<!DOCTYPE html>
	<html>
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>{title}</title>
	</head>
	<body>
		{bodyTag}
		{cssTag}
	</body>
	</html>
	"""

	def __init__(self, body = None, css: CssTag = None, title = None):
		self.title = title
		self.cssTag = css
		super().__init__(body = body)

	@property
	def htmlOut(self):
		return self.STRUCTURE.format(title = self.title, bodyTag = self.childHtml, cssTag = self.cssTag.htmlOut)
	
class Credits(Element):
	STRUCTURE = """
        <div style = "position: fixed; bottom: 1%; right: 2%; padding-left: 10px; padding-right: 10px; border-radius: 30px; color: {color}; background-color: {backgroundColor}; box-shadow: 0px 0px 50px 5px rgba(0,0,0,0.54);">
            {credits}
        </div>

		
	"""

	def __init__(self, body: list = None, color = None, backgroundColor = None):
		super().__init__(body = body)
		self.color = color
		self.backgroundColor = backgroundColor

	@property
	def htmlOut(self):
		if self.color == None:
			self.color = "white"
		if self.backgroundColor == None:
			self.backgroundColor = "black"

		return self.STRUCTURE.format(credits = self.childHtml, color = self.color, backgroundColor = self.backgroundColor)