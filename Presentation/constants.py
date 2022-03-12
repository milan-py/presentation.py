HTML_HEAD = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>

        <div id = "header">
            <h1>{header}</h1>
        </div>
"""

CSS_STYLE = """
	<style>

		body{
			font-family: fontFamiliy;
			color: #2c2c2c;
			margin: 0px;

			background-image: backgroundImage;
            background-color: backgroundColor;
			background-repeat: no-repeat;
			background-attachment: fixed;
			background-size: cover;

			height: 100%;
			width: 100%;       
		}

		#header{
			text-align: center;
			font-size: xx-large;

			margin-top: 0px;
			margin-bottom: -30px;
		}

		#categories{
			margin-left: 1.5%;
			/* margin-right: 0; */
		}

		.category{

			cursor: pointer;

			margin-top: 10px;

			margin-right: 1%;

			padding-left: 15px;
			padding-right: 15px;
			padding-top: 5px;
			padding-bottom: 5px;

			background-color: rgb(231, 231, 231);
			border-radius: 10px;

			width: 30%;
			transform: scale(1);

			float: left;
		}
		.category > img{
			opacity: 1;
			border-radius: 10px;
			max-width: previewMaxWidth%;
			width: previewWidth;
			max-height: previewMaxHeight%;
            float: previewFloat;
		}


		#fixed{
			position: fixed;
			bottom: 1%;
			right: 2%;

			padding-left: 10px;
			padding-right: 10px;

			border-radius: 30px;

			color: rgb(231, 231, 231);;
			background-color: rgb(0, 0, 90);

			box-shadow: 0px 0px 50px 5px rgba(0,0,0,0.54);
		}

		.center{
			position: fixed;

			left: 35%;
			top: 22%;
		}

		.center > img{
			max-height: centerMaxHeight%;
			max-width: centerMaxwidth%;
            width: centerWidth;
			cursor: default;
            float: centerFloat;
		}

        
		.center > p, .center > ul, .center > h1{
			cursor: text;
		}

		/* NODISPLAY_PLACEHOLDER */

        .center > ul, .center p{
            display: block;
        }
	</style>
"""

CSS_NODISPLAY = """
		.category > ul, .category > p{
    	    display: none;
		}
"""


HTML_CATEGORY_DIV = """
		<div id = "categories">
			{categories}
		</div>""" 

HTML_CATEGORY = """		
			<div class = "category" onclick = "present(this)">
			    <h1>{title}</h1>
			    categoryBody
			</div>
"""

HTML_OWN_CREDITS = """
        <div id = "fixed">
            <p>{credits}</p>
        </div>"""

JAVASCRIPT_HTML_END = """
<script>
            function zoom(element, scale){

                element.animate([{ transform: "scale(" + scale + ")" }
                ], {duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)"});

                setTimeout(() => {element.style.transform = "scale(" + scale + ")";}, 990);
            }

            function test(id){
                console.log(id);
                console.log(Array.from(id.parentNode.children).indexOf(id));
            }

            function stop(element){
                var element = document.getElementById("blurred");
                element.id = null;

                

                element.animate([{ filter: "blur(0)" }
                ], {duration: 1000});

                setTimeout(() => {
                    element.style.filter = "blur(0)";
                }, 990);

                var categories = document.getElementById("categories");
                var clone = categories.lastChild;

                zoom(clone, 1);

                clone.animate([{ opacity: "0" }
                ], {duration: 1000});

                setTimeout(() => {
                    clone.style.opacity = "0";
                    clone.remove();
                }, 990);
                

                var header = document.getElementById("header");
                
                header.animate([{ opacity: "1" }
                ], {duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)"});

                setTimeout(() => {
                    header.style.opacity = "1";
                }, 990);

                console.log(categories.children);
                for(var i = 0; i < categories.children.length; i++){
                    console.log("Iteration " + i);
                    categories.children[i].setAttribute("onclick","present(this)");
                }
            }

            function present(element){
                element.id = "blurred";

                const clone = element.cloneNode(true);

                document.getElementById("categories").appendChild(clone);

                element.animate([{ filter: "blur(1rem)" }
                ], {duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)"});

                setTimeout(() => {
                    element.style.filter = "blur(1rem)";
                }, 990);


                clone.style.boxShadow =  "0px 0px 31px 10px rgba(5,5,5,0.65)";
                clone.style.opacity = "0";
                    
                clone.classList.add("center");

                clone.onclick = (element) => {stop(element);};

                zoom(clone, 1.8);

                clone.animate([{ opacity: "1" }
                ], {duration: 1000});

                setTimeout(() => {
                    clone.style.opacity = "1";
                }, 990);

                var header = document.getElementById("header");
                
                header.animate([{ opacity: "0" }
                ], {duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)"});

                setTimeout(() => {
                    header.style.opacity = "0";
                }, 990);

                var categories = document.getElementById("categories");
                console.log(categories.children);
                for(var i = 0; i < (categories.children.length-1); i++){
                    console.log("Iteration " + i);
                    categories.children[i].setAttribute("onclick","");
                }
            }
            
        </script>
    </body>
</html>
"""