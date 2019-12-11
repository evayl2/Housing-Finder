
//var beds = document.getElementById("myform").beds;
//var baths = document.getElementById("baths").value;
//var price = document.getElementById("price-select").value;
//var mymajor = document.getElementById("major").value;
var major = document.getElementById("myform");
//var mymajor = "";
if (major == null) {
	console.log("can't find the form/form is null");
}

var maj = document.getElementById("major");
if (maj == null) {
	console.log("why is this null");
} 
if (maj != null) {
	var mymajor = console.log(maj.value);
}


function getApartments() {
	console.log("I am being called :)!");
	var major = document.getElementById("myform");
	var mymajor = "";
	if (major == null) {
		console.log("can't find the form/form is null");
	}

	var maj = document.getElementById("major");
	if (maj == null) {
		console.log("why is this null");
	} 
	if (maj != null) {
		mymajor = maj.value;
		if (mymajor == "computer science") {
		var myWindow = window.open("file:///C:/Users/Eva/Notepad++/CS196/csresults.html", "_self");
		}
		if (mymajor == "cs") {
			var myWindow = window.open("file:///C:/Users/Eva/Notepad++/CS196/csresults.html", "_self");
		}
		if (mymajor == "business") {
			var myWindow = window.open("file:///C:/Users/Eva/Notepad++/CS196/businessresults.html", "_self");
		}
		if(mymajor == "psychology"){
			var myWindow = window.open("file:///C:/Users/Eva/Notepad++/CS196/psychresults.html", "_self");
		}
	}
	//console.log(mymajor);
	
}

function openfile(file) { 
	window.location = "file:///C:/Users/Eva/Notepad++/CS196/" + file; 
}


		