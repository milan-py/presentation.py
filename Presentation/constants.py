HTML_HEAD = """<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>

        <div id = "header">
            <h1><span>{header}</span></h1>
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
			text-align: headerTextAlign;
			font-size: headerFontSize;
            
            margin: headerMargin;
			margin-bottom: -30px;

            color: headerColor;
            
		}

        #header > h1 > span{
            background-color: headerBackgroundColor;
            padding: headerPadding;
            border-radius: headerBorderRadius;
        }

		#categories{
			margin-left: 1.5%;
		}

        .row{
            display: block;
        }

        #centercontainer{
            display: flex;
            position: fixed;
            justify-content: center;
            align-items: center;
            top: 20%;
            z-index: 5;
            width: 100%;
        }

		.category {

            cursor: pointer;

            margin-top: 10px;

            margin-right: 1%;

            padding-left: 15px;
            padding-right: 15px;
            padding-top: 5px;
            padding-bottom: 5px;

            background-color: rgb(231, 231, 231);
            border-radius: 10px;
            transform: scale(1);
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
            width: 45%;
            cursor: auto;
        }

		.center > img{
			max-height: centerMaxHeight%;
			max-width: centerMaxwidth%;
            width: centerWidth;
            float: centerFloat;
		}

		/* NODISPLAY_PLACEHOLDER */

        .center > ul, .center p{
            display: block;
        }

        @media(min-width: 720px){
            .row{
                display: flex;
            }
            .center{
                width: 40%;
            }

            /* EQUAL_SIZE_PLACEHOLDER */
        }
	</style>
"""

CSS_EQUAL_SIZE = """
        .category{
            flex-basis: 100%;
        }
        .center{
            flex-basis: auto;
        }
"""

CSS_NODISPLAY = """
		.category > ul, .category > p{
    	    display: none;
		}
"""


HTML_CATEGORIES_CENTERCONTAINER = """
        <div id = "centercontainer">
                <p></p>
        </div>
		<div id = "categories">
			{categories}
		</div>"""

HTML_CATEGORY = """		
			<div class = "category" onclick = "present(this)">
			    <h1>{title}</h1>
			    categoryBody
			</div>
"""

HTML_ROW = """
    <div class = "row">
        {rowcontent}
    </div>
"""

HTML_OWN_CREDITS = """
        <div id = "fixed">
            <p>{credits}</p>
        </div>"""

JAVASCRIPT_HTML_END = """
<script>
            function zoom(element, scale) {

            element.animate([{ transform: "scale(" + scale + ")" }
            ], { duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)" });

            setTimeout(() => { element.style.transform = "scale(" + scale + ")"; }, 990);
        }

        function test(id) {
            console.log(id);
            console.log(Array.from(id.parentNode.children).indexOf(id));
        }

        function stop() {
            let element = document.getElementById("blurred");
            element.id = null;



            element.animate([{ filter: "blur(0)" }
            ], { duration: 1000 });

            setTimeout(() => {
                element.style.filter = "blur(0)";
            }, 990);

            let categories = document.getElementById("categories");

            let centercontainer = document.getElementById("centercontainer");

            let clone = centercontainer.lastChild;

            zoom(clone, 1);

            clone.animate([{ opacity: "0" }
            ], { duration: 1000 });

            setTimeout(() => {
                clone.style.opacity = "0";
                clone.remove();
            }, 990);


            let header = document.getElementById("header");

            header.animate([{ opacity: "1" }
            ], { duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)" });

            setTimeout(() => {
                header.style.opacity = "1";
            }, 990);

            console.log(categories.children);
            for(let i = 0; i < categories.children.length; i++){
                for(let y = 0; y < categories.children[i].children.length; y++){
                    console.log("iteration" + i);
                    categories.children[i].children[y].setAttribute("onclick", "present(this)");
                }
            }
        }

        function present(element) {
            const clone = element.cloneNode(true);
            clone.id = "centered";
            element.id = "blurred";

            document.getElementById("centercontainer").appendChild(clone);

            element.animate([{ filter: "blur(1rem)" }
            ], { duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)" });


            setTimeout(() => {
                element.style.filter = "blur(1rem)";
            }, 990);


            clone.style.boxShadow = "0px 0px 31px 10px rgba(5,5,5,0.65)";
            clone.style.opacity = "0";

            clone.classList.add("center");

            clone.onclick = "";

            let eventfunc = event => {
                let ignore = document.getElementById("centered");
                if(!(event.target === ignore || ignore.contains(event.target))){
                    stop();
                    window.removeEventListener("click", eventfunc);
                }
            };

            zoom(clone, 1.8);

            clone.animate([{ opacity: "1" }
            ], { duration: 1000 });

            setTimeout(() => {
                clone.style.opacity = "1";
                window.addEventListener("click", eventfunc);
                header.style.opacity = "0";
            }, 990);

            let header = document.getElementById("header");

            header.animate([{ opacity: "0" }
            ], { duration: 1000, easing: "cubic-bezier(.77,0,0,1.06)" });

            let categories = document.getElementById("categories");
            console.log(categories.children);
            for(let i = 0; i < categories.children.length; i++){
                for(let y = 0; y < categories.children[i].children.length; y++){
                    console.log("iteration" + i);
                    categories.children[i].children[y].setAttribute("onclick", "");
                }
            }
        }
            
        </script>
    </body>
</html>
"""