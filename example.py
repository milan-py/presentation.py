from presentation import *


presi = Presentation("Test", "header", backgroundImage = "wallpaper.webp", credits = "Creator")


categ = Category("title") 
categ.setContent("""<ul>
	<li>test1</li>
	<li>test2</li>
</ul>
<img src = "wallpaper.webp"></img>
""")


presi.addCategory(categ)
presi.addCategory(categ)

presi.centerImage.maxWidth = 10
presi.centerImage.float = "right"

presi.display = False

presi.create()

presi.write_html("example.html")