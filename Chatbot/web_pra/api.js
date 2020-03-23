function submit () {
	// var req = new Request(document.querySelectorAll("input"));
	// var myRequest = new Request('products.json');
	// var checks = document.querySelectorAll("input")
	var form = document.getElementById('input');
    // console.log(checks)
	fetch('./submit', {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({ })
	})
		.then(res => res.json())
		.then(ret => {  console.log(form)
			for (var i=0; i < checks.length; i++){
			        if (checks[i].checked == true && checks[i].value =="안창호"){
			            document.getElementById("result").innerHTML = "정답입니다." 
			            break
			        }else{
			            document.getElementById("result").innerHTML = "오답입니다."
			        }}
			// Update Element
		});
};
// body > div.body > div:nth-child(2)

