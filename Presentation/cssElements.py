from Presentation.utils import *

class CssClass:
    def __init__(self, classname: str, properties: dict = None):
        self.properties = properties
        self.classname = classname

    def __str__(self):
        return self.classname

    @property
    def cssOut(self):
        return f""".{self.classname}{{
            {'''
            '''.join(f"{key}: {value};" for key, value in zip(self.properties, self.properties.values()))}
        }}"""

    def WriteFile(self, file):
        with open(file, "w") as f:
            f.write(self.cssOut)

    def __eq__(self, other):
        return self.classname == other.classname

if __name__ == "__main__":
    css = CssClass("lol", {"color" : "Black", "border-radius" : "20px"})
    print(css.cssOut)

class CssId(CssClass):

    def __init__(self, classname: str, properties: dict = None):
        super().__init__(classname, properties)

    @property
    def cssOut(self):
        return f"""#{self.classname}{{
            {'''
            '''.join(f"{key}: {value};" for key, value in zip(self.properties, self.properties.values()))}
        }}"""

class CssTag:
    def __init__(self, classes: list = None):
        self.classes = classes

    @property
    def htmlOut(self):
        if self.classes == None:
            return ""
        return "<style>\n" + "\n\n".join(i.cssOut for i in self.classes) + "\n</style>"
