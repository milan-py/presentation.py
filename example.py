from Presentation import *

header = elements.Header("A beautiful presentation")
header.color = "white"
header.backgroundColor = "black"
header.padding = "10px"
header.borderRadius = "10px"

presi = Presentation(header, "presentation.py", backgroundImage = "wallpaper.webp", credits = "Creator", columns = 4)


categ1 = elements.Category("Categories like this") 
categ1.content = """<ul>
	<li>with just html</li>
	<li>pictures and everything</li>
</ul>
<img src = "wallpaper.webp"></img>
"""

categ2 = elements.Category("or like this") 
categ2.style = {"color" : "white", "background-color" : "black", "border-radius" : "15px 30px 60px 100px"}
categ2.content = """<ul>
	<li>with different colors</li>
	<li>and different shapes</li>
</ul>
"""

categ3 = elements.Category("With python")
categ3.content = """
<p>
<pre>
	<code>
categ1 = elements.Category("Categories like this")
categ1.content = '''
&lt;ul&gt;
	&lt;li&gt;with just html&lt;/li&gt;
	&lt;li&gt;pictures and everything&lt;/li&gt;
	&lt;img src = "wallpaper.webp"&gt;&lt;/img&gt;
&lt;/ul&gt;
'''
	</code>
</pre>
</p>
"""

presi.previewImage.style["padding"] = "1%"
presi.previewImage.style["width"] = "98%"
presi.previewImage.style["background-color"] =  "blue"
presi.centerImage.style["padding"] = "0%"
presi.centerImage.style["width"] = "50%"



presi.categories = [categ1, categ2, categ3, categ2, categ3, categ1]

presi.display = True
presi.equalSize = True

presi.create()

presi.writeHtml("example.html", compressed = False)