from Presentation import *


presi = Presentation("Test", "header", backgroundImage = "wallpaper.webp", credits = "Creator")


categ = Category("title1") 
categ.content = """<ul>
	<li>test1</li>
	<li>test2</li>
</ul>
<img src = "wallpaper.webp"></img>
"""



presi.categories.append(categ)

print(categ)
print(presi)

presi.centerImage.maxWidth = 10
presi.centerImage.float = "right"

presi.display = False

presi.create()

presi.writeHtml("example.html", compressed = True)