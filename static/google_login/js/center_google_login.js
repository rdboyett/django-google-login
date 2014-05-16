
$(document).ready(function(){
    resizeGoogleLoginPopup();
    
    $("#google-login-clicker").unbind('click').click(function(){
        $("#google-login-shade").fadeIn(600);
        $("#google_login_form").fadeIn(600);
    });
    
    $("#google-login-shade").unbind('click').click(function(){
        $("#google-login-shade").fadeOut(600);
        $("#google_login_form").fadeOut(600);
        $("#google_register_form").fadeOut(600);
    });


    $("#google-register").unbind('click').click(function(){
        $("#google-login-shade").fadeIn(600);
        $("#google_register_form").fadeIn(600);
    });
    
});


$( window ).resize(function() {
    resizeGoogleLoginPopup();
});

    function resizeTop(element) {
	var halfScreenHeight = ($(window).height())/2;
	var halfElementHeight = (element.height())/2;
	var top = halfScreenHeight - halfElementHeight;
	element.css({
	    'top': top+"px",
	});
    }
    function resizeLeft(element) {
	var halfScreenWidth = ($(window).width())/2;
	var halfElementWidth = (element.width())/2;
	var left = halfScreenWidth - halfElementWidth;
	element.css({
	    'left': left+"px",
	});
    }
    
    function resizeGoogleLoginPopup() {
	resizeTop($("#google_login_form"));
	resizeLeft($("#google_login_form"));
	resizeTop($("#google_register_form"));
	resizeLeft($("#google_register_form"));
    }






















