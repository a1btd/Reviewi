		function choose_country() {
			var y = document.getElementById("selectasin");
			if (y.style.display === "none") {
				y.style.display = "flex";
			} else if (y.style.display === "flex"){
				y.style.display = "none";
			} else {
				y.style.display = "none";
			}
			var x = document.getElementById("selectcountry");
			if (x.style.display === "none") {
				x.style.display = "flex";
			} else if (x.style.display === "flex"){
				x.style.display = "none";
			} else {
				x.style.display = "none";
			}
			var z = document.getElementById("countryContainer");
			if (z.style.display === "none") {
				z.style.display = "flex";
			} else if (z.style.display === "flex"){
				z.style.display = "none";
			} else {
				z.style.display = "none";
			}				
		}
		function choose_format() {
			var x = document.getElementById("selectcountry");
			if (x.style.display === "none") {
				x.style.display = "flex";
			} else if (x.style.display === "flex"){
				x.style.display = "none";
			} else {
				x.style.display = "none";
			}
			var sf = document.getElementById("selectformat");
			if (sf.style.display === "none") {
				sf.style.display = "flex";
			} else if (sf.style.display === "flex"){
				sf.style.display = "none";
			} else {
				sf.style.display = "none";
			}
			var fc = document.getElementById("formatContainer");
			if (fc.style.display === "none") {
				fc.style.display = "flex";
			} else if (fc.style.display === "flex"){
				fc.style.display = "none";
			} else {
				fc.style.display = "none";
			}

		}

		function enter_email() {	
			var sf = document.getElementById("selectformat");
			if (sf.style.display === "none") {
				sf.style.display = "flex";
			} else if (sf.style.display === "flex"){
				sf.style.display = "none";
			} else {
				sf.style.display = "none";
			}		
			var sa = document.getElementById("submitAll");
			if (sa.style.display === "none") {
				sa.style.display = "flex";
			} else if (sa.style.display === "flex"){
				sa.style.display = "none";
			} else {
				sa.style.display = "none";
			}
			var ec = document.getElementById("emailContainer");
			if (ec.style.display === "none") {
				ec.style.display = "flex";
			} else if (ec.style.display === "flex"){
				ec.style.display = "none";
			} else {
				ec.style.display = "none";
			}
		}