from Presentation.elements import CustomTag, RawTag
from Presentation.cssElements import CssClass

class Category(CustomTag):

	def __init__(self, body: list = None, properties: dict = None):
		super().__init__("div", body, properties)

	@property
	def	htmlOut(self):
		if self.htmlProperties == None:
			self.htmlProperties = dict()
		if self.htmlProperties.get("class") == None:
			self.htmlProperties["class"] = "category"
		if self.htmlProperties.get("onclick") == None:
			self.htmlProperties["onclick"] = "present(this, 1000)"
		return f"<{self.tag} {self.propertiesFormatted}>{self.childHtml}</{self.tag}>"

class PresentationJs(RawTag): #FIXME: an element with an image surpasses the screen width
	def __init__(self):
		tag = "script"
		body = """
			function stop(time){
				console.debug("stop()");
        	    let element = document.getElementById("centeredCategory");
        	    element.id = null;
	
				element.animate([{ opacity: "0" }
        	    ], { duration: time });
	
				zoom(element, 1, time);
				setTimeout(() => {
        	        element.style.opacity = "0";
        	        element.remove();
        	    }, time-20);
			}
	
	
			function zoom(element, scale, time) {
				console.debug("zoom()");
				element.animate([{ transform: "scale(" + scale + ")" }
				], { duration: time, easing: "cubic-bezier(.77,0,0,1.06)" });
	
				setTimeout(() => { element.style.transform = "scale(" + scale + ")"; }, time-20);
			}
	
	
			function present(element, time) {
				console.debug("present()");
        	    const clone = element.cloneNode(true);
        	    clone.id = "centeredCategory";
				clone.style.opacity = "0";
	
				let centercontainer = document.createElement("div");
	
				centercontainer.style = "display: flex; position: fixed; justify-content: center; align-items: center; top: 20%; z-index: 5; width: 100%;"
	
				document.body.appendChild(centercontainer);
	
				centercontainer.appendChild(clone);
	
				clone.style.zindex = "5";
				zoom(clone, 1.8, time);
	
        	    clone.animate([{ opacity: "1" }
        	    ], { duration: time });
	
	
				let eventfunc = event => {
        	        let ignore = document.getElementById("centeredCategory");
					stop(time);
        	        if(!(event.target === ignore || ignore.contains(event.target))){
        	            window.removeEventListener("click", eventfunc);
        	        }
        	    };
	
				setTimeout(() => {window.addEventListener("click", eventfunc);}, time/2);
	
				setTimeout(() => {
					clone.style.opacity = "1";
				}, time-20)
			}
		"""
		super().__init__(tag = tag, body = body)

class CategoryCss(CssClass):
	STANDARD = {
		"cursor": "pointer",

        "margin-top": "10px",
        "margin-right": "1%",

        "padding-left": "15px",
        "padding-right": "15px",
        "padding-top": "5px",
        "padding-bottom": "5px",
		
        "background-color": "rgb(231, 231, 231)",
        "border-radius": "10px",
        "transform": "scale(1)",
	}

	def __init__(self, classname: str = None, properties: dict = None):
		super().__init__(classname, properties)

	@property
	def cssOut(self):
		if self.classname == None:
			self.classname = "category"

		if self.properties == None:
			self.properties = dict()
		for key, value in zip(self.STANDARD, self.STANDARD.values()):
			if self.properties.get(key) == None:
				self.properties[key] = value
		return f""".{self.classname}{{
            {'''
            '''.join(f"{key}: {value};" for key, value in zip(self.properties, self.properties.values()))}
        }}"""