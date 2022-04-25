from Presentation.elements import *
from Presentation.widgets import *
from Presentation.PresentationWidgets import Category, CategoryCss
import Presentation.cssElements as css

element = Document(
	title = "HELO",
	body = [
		Category([
			RawTag("h1", body = "lol"),
			RawTag("p", "Text")
		])
	],
	css = css.CssTag([
		CategoryCss()
	])
)

element.writeFile("test.html")