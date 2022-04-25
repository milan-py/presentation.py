from Presentation.elements import CustomTag
from Presentation.cssElements import CssClass

# TODO add functionality with javascript

class Category(CustomTag):
	STRUCTURE = """		
		<div class = "category" onclick = "present(this)" style = "{style}">
		    <h1>{title}</h1>
		    categoryBody
		</div>
	"""

	def __init__(self, body: list = None, properties: dict = None):
		super().__init__("div", body, properties)

	@property
	def	htmlOut(self):
		if self.htmlProperties == None:
			self.htmlProperties = dict()
		if self.htmlProperties.get("class") == None:
			self.htmlProperties["class"] = "category"
		if self.htmlProperties.get("onclick") == None:
			self.htmlProperties["onclick"] = "present(this)"
		return f"<{self.tag} {self.propertiesFormatted}>{self.childHtml}</{self.tag}>"

class CategoryCss(CssClass):
	STANDARD = {
		"cursor": "pointer",

        "margin-top": "10px",
        "margin-right": "1%",

        "padding-left": "15px",
        "padding-right": "15px",
        "padding-top": "5px",
        "padding-bottom": "5px",
		
        "background-color": "rgb(231, 231, 231)",
        "border-radius": "10px",
        "transform": "scale(1)",
	}

	def __init__(self, classname: str = None, properties: dict = None):
		super().__init__(classname, properties)

	@property
	def cssOut(self):
		if self.classname == None:
			self.classname = "category"

		if self.properties == None:
			self.properties = dict()
		for key, value in zip(self.STANDARD, self.STANDARD.values()):
			if self.properties.get(key) == None:
				self.properties[key] = value
		return f""".{self.classname}{{
            {'''
            '''.join(f"{key}: {value};" for key, value in zip(self.properties, self.properties.values()))}
        }}"""