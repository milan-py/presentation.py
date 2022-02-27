#unordered list
HTML_UL = """<ul> 
    {}
</ul>
"""

#ordered list
HTML_OL = """<ol> 
    {}
</ol>
"""

def remove(content, strings): #removing multiple string from content
    for string in strings:
        content = content.replace(string, "")
    return content

def htmlify(string, type): #turning a bulletlist to a html bulletlist
    if type != "ol" and type != "ul":
        raise Exception("argument must be 'ol' oder 'ul'") 

    
    lines = string.splitlines() 
    for i in range(len(lines)):
        content = remove(lines[i], ("\t", "\n", "•", "○"))
        indent = lines[i].count("\t") 
        lines[i] = "{}"
        for x in range(indent):
            lines[i] = lines[i].format(HTML_OL if type == "ol" else HTML_UL)
        lines[i] = lines[i].format(f"<li>{content}</li>")

    return "<" + type + ">\n" + '\n'.join(lines) + "\n</" + type + ">"