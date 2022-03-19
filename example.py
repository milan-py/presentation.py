from Presentation import *


presi = Presentation("Test", "header", backgroundImage = "wallpaper.webp", credits = "Creator")


categ1 = Category("title1") 
categ1.content = """<ul>
	<li>test1</li>
	<li>test2</li>
</ul>
<img src = "wallpaper.webp"></img>
"""

categ2 = Category("title1") 
categ2.content = """<ul>
	<li>test1</li>
	<li>test2</li>
</ul>
"""



presi.categories.append(categ1)
presi.categories.append(categ2)
presi.categories.append(categ1)
presi.categories.append(categ1)

print(categ1)
print(presi)

presi.centerImage.maxWidth = 10
presi.centerImage.float = "right"

presi.display = False
presi.equalSize = True

presi.create()

presi.writeHtml("example.html", compressed = True)