//This script is to test the flow of the entire process
var clipboard_data = "Delivered-To: rauf.ridzuan@gmail.com";


var http = new XMLHttpRequest();
var url = "http://ec2-54-254-97-253.ap-southeast-1.compute.amazonaws.com:8000/post";
var params = "clipboard_data=" + clipboard_data;
http.open("POST", url, true);

//Send the proper header information along with the request
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.setRequestHeader("Content-length", params.length);
http.setRequestHeader("Connection", "close");

http.onreadystatechange = function() {//Call a function when the state changes.
	if(http.readyState == 4 && http.status == 200) {
		alert(http.responseText);
	}
}
http.send(params);