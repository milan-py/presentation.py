from Presentation.elements import *
from Presentation.widgets import *
from Presentation.PresentationWidgets import Category, CategoryCss, PresentationJs
import Presentation.cssElements as css

category = Category(body = [
	RawTag("h1", body = "lol"),
	RawTag("p", "Text")
])
category.htmlProperties["onclick"] = "present(this, 2000)"

element = Document(
	title = "HELO",
	body = [
		category,
		Category([
			RawTag("h1", body = "Second"),
			Img("wallpaper.webp", alt = "Hello", cssClass = "testclass", includeindoc = True)
		]),
		PresentationJs()
	],
	css = css.CssTag([
		CategoryCss(),
		css.CssClass(classname = "testclass", properties = {
			"width" : "10%"
		})
	])
)

element.writeFile("output.html")