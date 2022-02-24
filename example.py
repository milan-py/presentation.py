from presentation import *


presi = Presentation("Test", "header", backgroundImage = "wallpaper.webp", credits = "Creator")


categ = Category("title") 
categ.setContent("""<ul>
	<li>test1</li>
	<li>test2</li>
<ul>
""")


presi.addCategory(categ)
presi.addCategory(categ)

presi.display = False

presi.create()

presi.out("example.html")