# Presentation.py

A program written in python for creating a webbrowser presentation

[wallpaper source](https://pixahive.com/photo/desktop-wallpaper-8/)

## tutorial

### create Presentation object
```py
presentation = Presentation(Title, Header, backgroundImage = Image, credits = Name)
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
presentation.centerImage.float = "none"
presentation.centerImage.maxWidth = 100
presentation.centerImage.maxHeight = 100
presentation.centerImage.width = "none"

presentation.previewImage.float = "none"
presentation.previewImage.maxWidth = 100
presentation.previewImage.maxHeight = 100
presentation.previewImage.width = "none"
```
    
### deactivating preview text
```py
presentation.display = False
```
    
### create the presentation
```py
presentation.create()
```

### output to a file
```py
presentation.writeHtml(filename)
```
