from presentation import *
presi = Presentation("Test", "Test", backgroundImage = "wallpaper.jpg", credits = "von Mattis")


categ = Category("loltitle") 
categ.setContent("""<ul>
	<li>test1</li>
	<li>test2</li>
<ul>
""")


presi.addCategory(categ)
presi.addCategory(categ)

presi.display = False

presi.insertCategories()

presi.initJss()

presi.out("test.html")