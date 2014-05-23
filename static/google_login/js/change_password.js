$(document).ready(function(){
    resizeGoogleLoginPopup();
});

$( window ).resize(function() {
    resizeGoogleLoginPopup();
});

    function resizeTop(element) {
	var halfScreenHeight = (element.parent().height())/2;
	var halfElementHeight = (element.height())/2;
	var top = halfScreenHeight - halfElementHeight;
	element.css({
	    'margin-top': top+"px",
	});
    }
    function resizeLeft(element) {
	var halfScreenWidth = (element.parent().width())/2;
    console.log(halfScreenWidth);
	var halfElementWidth = (element.width())/2;
    console.log(halfElementWidth);
	var left = halfScreenWidth - halfElementWidth;
	element.css({
	    'margin-left': left+"px",
	});
    }
    
    function resizeGoogleLoginPopup() {
	    resizeTop($("#google_login_password_reset"));
	    resizeLeft($("#google_login_password_reset"));
    }

