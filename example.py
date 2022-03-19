from Presentation import *

header = Header("Header")
header.color = "white"
header.backgroundColor = "black"
header.padding = "10px"
header.borderRadius = "10px"

presi = Presentation(header, "title", backgroundImage = "wallpaper.webp", credits = "Creator")


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
presi.centerImage._float = "left"

presi.display = False
presi.equalSize = True

presi.create()

presi.writeHtml("example.html", compressed = True)