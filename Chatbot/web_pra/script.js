function submit () {
    var checks = document.getElementsByTagName("input");
	fetch('/submit', {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({ })
	})
		.then(res => res.json())
		.then(ret => {
    
        }
			// Update Element
		
)};


// function submit () {
    
//     var checks = document.getElementsByTagName("input")
    
//     for (var i=0; i < checks.length; i++){
//         if (checks[i].checked == true && checks[i].value =="안창호"){
//             document.getElementById("result").innerHTML = "정답입니다." 
//             break
//         }else{
//             document.getElementById("result").innerHTML = "오답입니다."
//         }
    
    
//     }};
    