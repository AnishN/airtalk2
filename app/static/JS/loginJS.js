function init(){
		$("#button").click(function(){
			verify();
		});
}

function verify(){
	if ($("#flightInputId").val() == "" || $("#emailInputId").val() == ""){
		alert("Not all fields filled out");
	}
	
	$.ajax({

		url: '/airtalk/_confirm',
		type: 'POST',
		data: {email:$("#flightInputId").val(), flightId:$("#emailInputId").val()},
		success: function(data){
			
		},
		error: function(error){
			
		}
	});
}
