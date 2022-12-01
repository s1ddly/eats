print("Executing Webpage Generation")
infile = open("../list.csv", "r")
inlines = infile.read().split("\n")

pageTemplate = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="Sid Shardanand" />
        <title>[Name]</title>
        <link rel="icon" type="image/x-icon" href="../assets/favicon.ico" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v6.1.0/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Varela+Round" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="../css/styles.css" rel="stylesheet" />
		<script src="../js/functions.js"></script>
    </head>
    <body id="page-top">
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#page-top">Eats</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="../">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="../restaraunts.html">Restaraunts</a></li>
                        <li class="nav-item"><a class="nav-link" href="https://sidshardanand.com/">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>	
        <!-- Details-->
        <section class="projects-section bg-black" id="Details">
            <div class="container px-4 px-lg-5" id="DetailContainer">
				<div class="row gx-0 justify-content-center">
					<div class="col-lg-6">
						<div class="bg-black text-center h-100 project">
							<div class="d-flex h-100">
								<div class="project-text w-100 my-auto text-center text-lg-left">
									<a id="RestarauntLink" href="[Site]"><h4 class="text-white" id="RestarauntTitle">[Name]</h4></a>
									<p class="mb-0 text-white-50" id="RestarauntDecription">[Description]</p>
									<hr class="d-none d-lg-block mb-0 ms-0">
									<p class="mb-0 text-white-50 text-start" id="RestarauntReview">[Review]</p>
									<hr class="d-none d-lg-block mb-0 ms-0">
									<p class="mb-0 text-white-50 text-start">Rating: <b id="RestarauntRating">[Rating]</b>/10</p>
									<p class="mb-0 text-white-50 text-start">Price: <b id="RestarauntCost">[Cost]</b></p>
									<p class="mb-0 text-white-50 text-start">Suburb: <b id="RestarauntSuburb">[Suburb]</b></p>
									<p class="mb-0 text-white-50 text-start">Tags: <b id="RestarauntTags">[Tags]</b></p>
								</div>
							</div>
						</div>
					</div>
					<div class="col-lg-6">
						<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" id="gmap_canvas" src="[Maps]">
						</iframe>
					</div>
				</div>
            </div>
        </section>
        <!-- Footer-->
        <footer class="footer bg-black small text-center text-white-50">
			<div class="container px-4 px-lg-5"><p class="m-0 text-center text-white">This webpage was made using a <a href="https://startbootstrap.com/theme/grayscale" onMouseOver="this.style.color='#212529'" onMouseOut="this.style.color='#64a19d'" target="_blank">Template</a> under the MIT <a href="https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE" onMouseOver="this.style.color='#212529'" onMouseOut="this.style.color='#64a19d'" target="_blank">License</a></p></div>
		</footer>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="../js/scripts.js"></script>
    </body>
</html>
"""

for x in range(1, len(inlines)):
    #print(inlines[x])
    if(inlines[x] != ""):
        invals = inlines[x].split(",")
        name = invals[0]
        visited = invals[1]
        visitedDate = invals[2]
        suburb = invals[3]
        rating = invals[4]
        pricing = invals[5]
        description = invals[6].replace("<comma>", ",")
        review = invals[7].replace("<comma>", ",")
        tags = invals[8].replace("|", ", ")
        site = invals[9]
        maps = invals[10]
        img = invals[11]
        
        templateString = pageTemplate
        templateString = templateString.replace("[Name]", name)
        templateString = templateString.replace("[Description]", description)
        templateString = templateString.replace("[Review]", review)
        templateString = templateString.replace("[Rating]", rating)
        templateString = templateString.replace("[Cost]", pricing)
        templateString = templateString.replace("[Suburb]", suburb)
        templateString = templateString.replace("[Tags]", tags)
        templateString = templateString.replace("[Site]", site)
        templateString = templateString.replace("[Maps]", maps)
        
        outfile = open(("../restaraunt/" + name + ".html"),"w")
        outfile.write(templateString)
        outfile.close()
    