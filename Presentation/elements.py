class Element:
	def setProperties(self, html: str, **kwargs):
		for i in kwargs.keys():
			html = html.replace(i, str(getattr(self, kwargs[i])))
		return html

class Image(Element): # class for storing css properties for images 
	def __init__(self, maxHeight = 100, maxWidth = 100, _float = "none", width = "none"):
		self.maxHeight = maxHeight
		self.maxWidth = maxWidth
		self._float = _float
		self.width = width

class Header(Element):
	def __init__(self, content, textAlign = "center", fontSize = "xx-large", margin = "0px", color = "black", backgroundColor = "none", padding = "0px", borderRadius = "0px"):
		self.content = content
		self.textAlign = textAlign
		self.fontSize = fontSize 
		self.margin = margin
		self.color = color
		self.padding = padding
		self.backgroundColor = backgroundColor
		self.borderRadius = borderRadius

	def __str__(self):
		return f"Header({self.content})"