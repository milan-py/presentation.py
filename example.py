from Presentation.elements import *
from Presentation.widgets import *
from Presentation.PresentationWidgets import Category, CategoryCss, PresentationJs
import Presentation.cssElements as css

category = Category(body = [
	RawTag("h1", body = "lol"),
	RawTag("p", "Text")
])
category.htmlProperties["onclick"] = "present(this, 500)"

element = Document(
	title = "HELO",
	body = [
		category,
		Category([
			RawTag("h1", body = "Second")
		]),
		PresentationJs()
	],
	css = css.CssTag([
		CategoryCss()
	])
)

element.writeFile("output.html")