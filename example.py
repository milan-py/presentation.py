from Presentation import *

header = elements.Header("Header")
header.color = "white"
header.backgroundColor = "black"
header.padding = "10px"
header.borderRadius = "10px"

presi = Presentation(header, "title", backgroundImage = "wallpaper.webp", credits = "Creator", columns = 3)


categ1 = elements.Category("title1") 
categ1.content = """<ul>
	<li>test1</li>
	<li>test2</li>
</ul>
<img src = "wallpaper.webp"></img>
"""

categ2 = elements.Category("title1") 
categ2.style = {"color" : "white", "background-color" : "black"}
categ2.content = """<ul>
	<li>test1</li>
	<li>test2</li>
</ul>
"""
presi.previewImage.style["padding"] = "1%"
presi.centerImage.style["padding"] = "0%"
presi.previewImage.style["background-color"] =  "green"

presi.previewImage.style["width"] = "100%"
presi.centerImage.style["width"] = "50%"


presi.categories.append(categ1)
presi.categories.append(categ2)
presi.categories.append(categ2)
presi.categories.append(categ2)
presi.categories.append(categ2)

presi.display = False
presi.equalSize = True

presi.create()

presi.writeHtml("example.html", compressed = False)