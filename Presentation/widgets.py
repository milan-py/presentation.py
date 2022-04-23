from Presentation.elements import Element

class Document(Element):
	STRUCTURE = """<!DOCTYPE html>
	<html>
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>{{title}}</title>
	</head>
	<body>
		{{bodyTag}}
	</body>
	</html>
	"""

	def __init__(self, body = None, css = None, title = None):
		self.body = body
		self.css = css
		self.title = title
		super().__init__(body = body, css = css)

	@property
	def htmlOut(self):
		return self.STRUCTURE.replace(
			"{{title}}", self.title
		).replace(
			"{{bodyTag}}",
			self.childHtml
		)
	
class Credits(Element):
	STRUCTURE = """
        <div style = "position: fixed; bottom: 1%; right: 2%; padding-left: 10px; padding-right: 10px; border-radius: 30px; color: {{color}}; background-color: {{background-color}}; box-shadow: 0px 0px 50px 5px rgba(0,0,0,0.54);">
            {{credits}}
        </div>

		
	"""

	def __init__(self, body: list = None, color = None, backgroundcolor = None):
		super().__init__(body = body, css = None)
		self.color = color
		self.backgroundcolor = backgroundcolor

	@property
	def htmlOut(self):
		if self.color == None:
			self.color = "white"
		if self.backgroundcolor == None:
			self.backgroundcolor = "black"
		return self.STRUCTURE.replace(
			"{{credits}}", self.childHtml
		).replace(
			"{{color}}", self.color
		).replace(
			"{{background-color}}", self.backgroundcolor
		)