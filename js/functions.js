var searchFilter = [1, 0];

function httpGet(theUrl)
{
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
	xmlHttp.send( null );
	return xmlHttp.responseText;
}

function loadlist(){
	listing(httpGet("list.csv"), searchFilter);
}

function listing(instr, searchfilter){
	visited = searchfilter[0];
	price = searchfilter[1];
	document.getElementById("RestarauntList").innerHTML = "";
	inlines = instr.split("\n");
	for(let i = 1; i < inlines.length; i++){
		if (inlines[i] != ""){
			vals = inlines[i].split(",");
			//Below filters restaraunts based on visited status
			switch(visited){
				case 1:
					if(vals[1] != "Yes"){
						continue;
					}
					break;
				case 2:
					if(vals[1] != ""){
						continue;
					}
					break;
				default:
					break;
			}
			//Below filters restaraunts based on cost indicator
			switch(price){
				case 1:
					if(vals[5] != "$"){
						continue;
					}
					break;
				case 2:
					if(vals[5] != "$$"){
						continue;
					}
					break;
				case 3:
					if(vals[5] != "$$$"){
						continue;
					}
					break;
				default:
					break;
			}
			
			var linkdiv = document.createElement("a");
			linkdiv.className = "divlink";
			linkdiv.href = "restaraunt/" + encodeURI(vals[0]) + ".html"
			var rowdiv = document.createElement("div");
			rowdiv.className = "row gx-0 justify-content-center";
			var leftcol = document.createElement("div");
			leftcol.className = "col-lg-3";
			var leftimg = document.createElement("img");
			leftimg.className = "img-fluid rounded";
			if(vals[11] == ""){
				leftimg.src = "assets/img/default-food.jpg"
			} else {
				leftimg.src = "assets/img/" + vals[11];
			}
			var rightcol = document.createElement("div");
			rightcol.className = "col-lg-9 item-hover";
			var rightproj = document.createElement("div");
			rightproj.className = "bg-black text-center h-100 project";
			var rightproj = document.createElement("div");
			rightproj.className = "bg-black text-center h-100 project";
			var rightflex = document.createElement("div");
			rightflex.className = "d-flex h-100";
			var righttext = document.createElement("div");
			righttext.className = "project-text w-100 my-auto text-center text-lg-left";
			var righthead = document.createElement("h4");
			righthead.className = "text-white";
			righthead.innerText = vals[0];
			var rightpara = document.createElement("p");
			rightpara.className = "mb-0 text-white-50";
			rightpara.innerText = vals[6].replaceAll("<comma>",",");
			var righthr = document.createElement("hr");
			righthr.className = "d-none d-lg-block mb-0 ms-0";
			var rightsuburb = document.createElement("p");
			rightsuburb.className = "mb-0 text-white-50";
			rightsuburb.style["text-align"] = "left";
			rightsuburb.innerText = vals[3]
			
			leftcol.append(leftimg);
			rowdiv.append(leftcol);
			
			righttext.append(righthead);
			righttext.append(rightpara);
			righttext.append(righthr);
			righttext.append(rightsuburb);
			rightflex.append(righttext);
			rightproj.append(rightflex);
			rightcol.append(rightproj);
			rowdiv.append(rightcol);
			linkdiv.append(rowdiv);
			document.getElementById("RestarauntList").append(linkdiv);
		}
	}
}

//Filter functions below
function visitedany(){
	searchFilter[0] = 0;
	listing(httpGet("list.csv"), searchFilter);
}

function visitedonly(){
	searchFilter[0] = 1;
	listing(httpGet("list.csv"), searchFilter);
}

function visitedun(){
	searchFilter[0] = 2;
	listing(httpGet("list.csv"), searchFilter);
}

function visitedun(){
	searchFilter[0] = 2;
	listing(httpGet("list.csv"), searchFilter);
}

function costany(){
	searchFilter[1] = 0;
	listing(httpGet("list.csv"), searchFilter);
}

function costone(){
	searchFilter[1] = 1;
	listing(httpGet("list.csv"), searchFilter);
}

function costtwo(){
	searchFilter[1] = 2;
	listing(httpGet("list.csv"), searchFilter);
}

function costthree(){
	searchFilter[1] = 3;
	listing(httpGet("list.csv"), searchFilter);
}