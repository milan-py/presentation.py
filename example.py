import Presentation.elements as el
import Presentation.widgets as wg

element = wg.Document(
	title = "HELO",
	body = [
		el.Div([
			el.CustomTag("a", properties = {"href" : "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, body = [
				el.RawTag("h1", body = "Cool youtube video"),
				el.RawTag("p", body = "Trust me it's not a rick roll"),
			])
		]),
		wg.Credits(backgroundcolor = "blue", color = "gray", body = [
			el.RawTag("p", body = "my stuff")
		])
	]
)


element.writeFile("test.html")