function locationTab()
{
	$(".productTab").removeClass("active");
	$(".locationTab").addClass("active");   
}

function saveproduct()
{
	$.ajax({
        url: '/productAddPage',
        data: $('form').serialize(), 
        type: 'POST',
        success: function(res) {
            console.log(res);
			window.location.replace("/")
			
        },
        error: function(error) {
            console.log(error);
        }
    });
}
/*
function updateproduct()
{
	$.ajax({
        url: '/productEditPage',
        data: $('.updateproduct').serialize(), 
        type: 'POST',
        success: function(res) {
            console.log(res);
			window.location.replace("/")
			
        },
        error: function(error) {
            console.log(error);
        }
    });
}*/
function savelocation()
{
	$.ajax({
        url: '/locationAddPage',
        data: $('form').serialize(), 
        type: 'POST',
        success: function(res) {
            console.log(res);
			window.location.replace("/locationDetails")
			
        },
        error: function(error) {
            console.log(error);
        }
    });
}
/*
function updateLocation(id)
{

    form_data = $("form").serialize();
	alert(form_data);
          
	$.ajax({
        url: '/locationUpdatePage',
        data: $('form').serialize(), 
        type: 'POST',
        success: function(res) {
            console.log(res);
			//window.location.replace("/locationDetails")
			
        },
        error: function(error) {
            console.log(error);
        }
    });
}*/
function saveProductMovement()
{
	$.ajax({
        url: '/ProductMovementAddPage',
        data: $('form').serialize(), 
        type: 'POST',
        success: function(res) {
            console.log(res);
			window.location.replace("/productMovementDetails")
			
        },
        error: function(error) {
            console.log(error);
        }
    });
}