# Presentation.py

A program written in python for creating a webbrowser presentation

[wallpaper source](https://pixahive.com/photo/desktop-wallpaper-8/)

## tutorial

```py
from Presentation import *
```

### create Presentation object
```py
presentation = Presentation(elements.Header("Title"), "Title")
```
### create a category object
```py
categ = Category("title") 
```    
### set the content of a category
```py
categ.content = "<p>example</p>"
```
### add the categories to the presentation
```py
presentation.categories = [categ]
```
    
### set image properties of category preview and presented category
```py
presi.previewImage.style["padding"] = "1%"
presi.previewImage.style["width"] = "98%"
presi.previewImage.style["background-color"] =  "blue"
presi.centerImage.style["padding"] = "0%"
presi.centerImage.style["width"] = "50%"
```
    
### deactivating preview text
```py
presentation.display = False
```

### setting the categories to the same size
```py
presentation.equalSize = True 
```
    
### create the presentation
```py
presentation.create()
```

### output to a file
```py
presentation.writeHtml(filename)
```
