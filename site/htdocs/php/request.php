<!doctype html>
<html lang="en">
  <head>
  	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=UA-128178623-1"></script>
	<script>
	  window.dataLayer = window.dataLayer || [];
	  function gtag(){dataLayer.push(arguments);}
	  gtag('js', new Date());

	  gtag('config', 'UA-128178623-1');
	</script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../image/favicon.ico">

    <title>Reviewi For Amazon</title>

    <!-- Bootstrap core CSS -->
    <link href="../css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="../css/cover.css" rel="stylesheet">
	
    <!-- CSS for check boxes -->	
	<link href="https://cdn.jsdelivr.net/npm/pretty-checkbox@3.0/dist/pretty-checkbox.min.css" rel="stylesheet">
	
  </head>

  <body class="text-center">

    <div class=".cover-container_res d-flex w-100 h-100 p-3 mx-auto flex-column">
      <header class="masthead mb-auto">
        <div class="inner"  style=" width:85%; padding-left: 25%">
        <img src="/image/rlogo.png" alt="Reviewi.me" height="50" width="66">
          <h3 class="masthead-brand">Reviewi.me</h3>
          <nav class="nav nav-masthead justify-content-center">
            <a class="nav-link" href="../index.html">Home</a>
            <a class="nav-link" href="../html/HowTo.html">How To</a>
            <a class="nav-link" href="../html/Contact.html">Contact</a>
            <a class="nav-link" href="../html/Donate.html">Donate</a> 
          </nav>
        </div>
      </header>
      <br>
      <main role="main" class="inner cover">
        <h1 class="cover-heading"><a href="../index.html">Reviewi For Amazon</a></h1>
        <p class="lead">You requested, we deliver! <br> <br>
		Within 1 hour you will receive a file in  <b><?php echo $_POST["format"]; ?></b> format to the email address provided. <br>
		Within the file you will find reviews and much more for the product <b><?php echo $_POST["ASIN"]; ?></b>  <br> 
		Enjoy it and feel free to request more! <br><br><br></p>

		<div  class="secondaryHeader"> 
		<div class="button-container" style="width:50%; margin: auto;">
		<p class="lead" style="color: #333;">
			<?php
			require_once('dbconnection.php');
				// define variables and set to empty values
			$asinErr = $emailErr = $formatErr = $countryErr = "";

			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				if (empty($_POST["ASIN"])) {
				  		$asinErr="Error";
					    print "<meta http-equiv=\"refresh\" content=\"0;URL=../html/Again.html\">";
					  } else {
						$asin = test_input($_POST["ASIN"]);
						

					}
				if (empty($_POST["Email"])) {
				  		$emailErr="Error";
					    print "<meta http-equiv=\"refresh\" content=\"0;URL=../html/Again.html\">";
					  } else {
						$email = test_input($_POST["Email"]);
						
					}
				
				$date = date("Ymd");

				if (empty($_POST["COM"]) and empty($_POST["UK"]) and empty($_POST["FR"]) and empty($_POST["DE"]) and empty($_POST["ES"]) and empty($_POST["IT"]) and empty($_POST["IND"])) {
						$countryErr = "Error";
					    print "<meta http-equiv=\"refresh\" content=\"0;URL=../html/Again.html\">";							
					} else {

						$com = test_input($_POST["COM"]);
						$uk = test_input($_POST["UK"]);
						$fr = test_input($_POST["FR"]);
						$de = test_input($_POST["DE"]);
						$es = test_input($_POST["ES"]);
						$it = test_input($_POST["IT"]);
						$ind = test_input($_POST["IND"]);

					}

				if (empty($_POST["format"])) {
				  		$formatErr="Error";
					    print "<meta http-equiv=\"refresh\" content=\"0;URL=../html/Again.html\">";
					  } else {
						$format = test_input($_POST["format"]);
					}
			}
			function test_input($data) {
			  $data = trim($data);
			  $data = stripslashes($data);
			  $data = htmlspecialchars($data);
			  return $data;
			}
			function db_quote($value) {
			    $connection = db_connect();
			    return "'" . mysqli_real_escape_string($connection,$value) . "'";
			}


			function db_query($query) {
			    // Connect to the database
			    $connection = db_connect();
			 
			    // Query the database
			    $result = mysqli_query($connection,$query);
			 
			    return $result;
			}

			function db_error() {
			    $connection = db_connect();
			    return mysqli_error($connection);
			}

			$charset = 'utf8' ;
			// Create connection
			
			
			if (empty($_POST["ASIN"]) or empty($_POST["Email"]) or empty($_POST["format"])) {
				$sql=""; 
			}
			else {
				$sql = "INSERT INTO `reviewidev`.`tab_requests`
				(`ID`,
				`ASIN`,
				`EMAIL`,
				`DATE`,
				`UK`,
				`FR`,
				`IT`,
				`DE`,
				`ES`,
				`COM`,
				`IND`,				
				`FORMAT`,
				`TOPROCESS`,
				`PROCESSED_DT`)
				VALUES
				(null,
				'$asin ',
				'$email',
				'$date',
				'$uk',
				'$fr',
				'$it',
				'$de',
				'$es',
				'$com',
				'$ind',
				'$format',
				'Y',
				null);
				";
			} 
			$result = db_query($sql);

			if (@$result===true) {
				echo "STATUS: The file is on his way...";
			} else {
				print "<meta http-equiv=\"refresh\" content=\"0;URL=../html/Error.html\">";
			}

			
			?></p><br>

			<p class="lead" style="color: #333;">
  				<span class="small"> >> One hour is gone and you didn't receive anything? >> <br>  >> Check your spam folder >> <br> >> Nothing there? >> <br> >> <a href="../html/Contact.html">Contact me </a> ;) << </span></p>
			</div>
		</div>
			</main>
		<br><br>
      <footer class="mastfoot mt-auto">
        <div class="inner">

          <p>
          	<span> Reviewi.me is a project by <a href="https://www.linkedin.com/in/angelomartelli" target="_new">Angelo Martelli.</a><br>
          	<span class="small">Cover template for <a href="https://getbootstrap.com/">Bootstrap</a>, by <a href="https://twitter.com/mdo">@mdo</a>.</span>
          </p>
        </div>
      </footer>
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <script src="../js/popper.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
	<script src="../js/buttons.js"></script>



</body>
</html>