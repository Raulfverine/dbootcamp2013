function pendekan (resopone) {
	responseObject = JSON.parse(response);
	var divId = document.getElementById('div1')
	var myTable = "<table cellspacing=\"0\" rules=\"all\" class=\"GridData\" border=\"1\" id=\"ctl00_ContentPlaceHolder1_gridReceived\" style=\"width:500px;border-collapse:collapse;\"><tr><td style='width: 100px; color: red;'>Key</td><td style='width: 100px; color: red;'>Value</td>";
	for (var count in responseObject) {
			myTable += "<tr><td>" + count +" </td><td>" + responseObject[count] + "</td></tr>";
		console.log(count + " " +responseObject[count]);		
	};
	div1.innerHTML = myTable;
}