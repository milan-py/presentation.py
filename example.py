from Presentation.elements import *
from Presentation.widgets import *
import Presentation.cssElements as css

cssclass = css.CssClass("hello", {
	"border-radius" : 
	"10px", 
	"background-color" : "black", 
	"text-decoration" : "none"
})

element = Document(
	title = "HELO",
	body = [
		Div(properties = {"class" : "hello"}, body = [
			CustomTag("a", properties = {"href" : "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, body = [
				RawTag("h1", body = "Cool youtube video"),
				RawTag("p", body = "Trust me it's not a rick roll"),
			])
		]),
		Credits(backgroundColor = "blue", color = "white", body = [
			RawTag("h1", body = "my stuff")
		])
	],
	css = css.CssTag([
		cssclass
	])
)

element.writeFile("test.html")