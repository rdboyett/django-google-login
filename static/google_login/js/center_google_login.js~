
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
        $("#google_forgot_form").fadeOut(600);
    });


    $("#google-sign-up").unbind('click').click(function(e){
        e.preventDefault();
        $("#google-login-shade").fadeIn(600);
        $("#google_register_form").fadeIn(600);
    });
    
    
    $(".forgot-password").click(function(){
        $("#google_login_form").fadeOut(600);
        $("#google_register_form").fadeOut(600);
        $("#google_forgot_form").fadeIn(600);
    });

    $("#google-forgot-submit").click(function(e){
            e.preventDefault();
            var value = $("#google-forgot-email").val();
            var atpos=value.indexOf("@");
            var dotpos=value.lastIndexOf(".");
            if (atpos<1 || dotpos<atpos+2 || dotpos+2>=value.length)
              {
                $("#email-forgot-error").html('not a valid email');
                $("#email-forgot-error").fadeIn(600);
                    $("#forgot-check-email").css({'top':(($("#google-forgot-email").position().top)+7)+"px"});
                    $("#forgot-check-email").addClass('register-check-error');
                    $("#forgot-check-email").removeClass('register-check-good');
                    $("#forgot-check-email").fadeIn(600);
              }else{
                    $("#email-forgot-error").fadeOut(600);
                    //$(this).attr('style','background-color:#BDFFBD;');
                    $("#forgot-check-email").fadeOut(600, function(){
                        $("#forgot-check-email").css({'top':(($("#google-forgot-email").position().top)+7)+"px"});
                        $("#forgot-check-email").removeClass('register-check-error');
                        $("#forgot-check-email").addClass('register-check-good');
                        $("#forgot-check-email").fadeIn(600);
                    });
                    submitPasswordForgot(value);
              }
        
    });

    $("#google-register-submit").click(function(e){
        e.preventDefault();
        var submit = true;
        $("#google-registration-form input").each(function(){
            var value = $(this).val();
            if ( $(this).hasClass('register-input-error') || value == "" ){
                submit = false;
            }
        });
        if ( submit ){
            submitRegistration();
        }
    });

    $("#google_register_form input").blur(function(){
        var inputName = $(this).attr('name');
        var value = $(this).val();
        if (inputName == 'username'){
            //todo: put in a check to see if the username already exists


            if (value.length > 5 && value.length < 30){
                if( /[^a-zA-Z0-9]/.test( value ) ) {
                    $("#username-register-error").html('letters and numbers only');
                    $("#username-register-error").fadeIn(600);
                    $(this).addClass('register-input-error');
                    //$(this).attr('style','background-color:#FFE6E6;');
                    $(this).unbind('keyup').keyup(function(){keyChangeInput($(this))});
                    var top = $(this).position().top;
                    //console.log(top);
                    setCheckSignalPosition();
                    $("#register-check-username").addClass('register-check-error');
                    $("#register-check-username").removeClass('register-check-good');
                    $("#register-check-username").fadeIn(600);
                }else{
                    $("#username-register-error").fadeOut(600);
                    $(this).removeClass('register-input-error');
                    //$(this).attr('style','background-color:#BDFFBD;');
                    $("#register-check-username").fadeOut(600, function(){
                        var top = $("#google-register-username").position().top;
                        //console.log(top);
                        setCheckSignalPosition();
                        $("#register-check-username").removeClass('register-check-error');
                        $("#register-check-username").addClass('register-check-good');
                        $("#register-check-username").fadeIn(600);
                    });
                    doesUsernameExist(value);
                    $(this).unbind('keyup');
                }
            }else if (value=="" || value.length <= 5){
                $("#username-register-error").html('at least 6 characters');
                $("#username-register-error").fadeIn(600);
                $(this).addClass('register-input-error');
                //$(this).attr('style','background-color:#FFE6E6;');
                $(this).unbind('keyup').keyup(function(){keyChangeInput($(this))});
                    var top = $(this).position().top;
                    //console.log(top);
                    setCheckSignalPosition();
                    $("#register-check-username").addClass('register-check-error');
                    $("#register-check-username").removeClass('register-check-good');
                    $("#register-check-username").fadeIn(600);
            }
        }else if (inputName == 'email'){
            var atpos=value.indexOf("@");
            var dotpos=value.lastIndexOf(".");
            if (atpos<1 || dotpos<atpos+2 || dotpos+2>=value.length)
              {
                $("#email-register-error").html('not a valid email');
                $("#email-register-error").fadeIn(600);
                $(this).addClass('register-input-error');
                //$(this).attr('style','background-color:#FFE6E6;');
                $(this).unbind('keyup').keyup(function(){keyChangeInput($(this))});
                    var top = $(this).position().top;
                    //console.log(top);
                    setCheckSignalPosition();
                    $("#register-check-email").addClass('register-check-error');
                    $("#register-check-email").removeClass('register-check-good');
                    $("#register-check-email").fadeIn(600);
              }else{
                    $("#email-register-error").fadeOut(600);
                    $(this).removeClass('register-input-error');
                    //$(this).attr('style','background-color:#BDFFBD;');
                    $("#register-check-email").fadeOut(600, function(){
                        var top = $("#google-register-email").position().top;
                        //console.log(top);
                        setCheckSignalPosition();
                        $("#register-check-email").removeClass('register-check-error');
                        $("#register-check-email").addClass('register-check-good');
                        $("#register-check-email").fadeIn(600);
                    });
                    doesEmailExist(value);
                    $(this).unbind('keyup');
              }
        }else{
            //password
            var noWhitespaces = /^\w+$/;
            var number = /[0-9]/;
            var lowerLetter = /[a-z]/;
            var upperLetter = /[A-Z]/;
            var correctPassword = false;
            if (value=="" || value.length <= 5){
                $("#password-register-error").html('6 or more characters');
            }else if (!noWhitespaces.test(value)){
                $("#password-register-error").html('no spaces');
            }else if (!number.test(value)){
                $("#password-register-error").html('at least 1 number');
            }else if (!lowerLetter.test(value)){
                $("#password-register-error").html('at least 1 lowercase');
            }else if (!upperLetter.test(value)){
                $("#password-register-error").html('at least 1 uppercase');
            }else{
                correctPassword = true;
            }

            if (!correctPassword){
                $("#password-register-error").fadeIn(600);
                $(this).addClass('register-input-error');
                //$(this).attr('style','background-color:#FFE6E6;');
                $(this).unbind('keyup').keyup(function(){keyChangeInput($(this))});
                    var top = $(this).position().top;
                    //console.log(top);
                    setCheckSignalPosition();
                    $("#register-check-password").addClass('register-check-error');
                    $("#register-check-password").removeClass('register-check-good');
                    $("#register-check-password").fadeIn(600);
            }else{
                $("#password-register-error").fadeOut(600);
                    $(this).removeClass('register-input-error');
                    //$(this).attr('style','background-color:#BDFFBD;');
                    $("#register-check-password").fadeOut(600, function(){
                        var top = $("#google-register-password").position().top;
                        //console.log(top);
                        setCheckSignalPosition();
                        $("#register-check-password").removeClass('register-check-error');
                        $("#register-check-password").addClass('register-check-good');
                        $("#register-check-password").fadeIn(600);
                    });
                    $(this).unbind('keyup');
            }
        }
    });

    setTimeout(function(){
        $("input").each(function(){
            $(this).val('test');
            $(this).val('');
        });
    }, 1000);

    
    
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
	    resizeTop($("#google_forgot_form"));
	    resizeLeft($("#google_forgot_form"));
    }


function keyChangeInput(e){
    var inputName = e.attr('name');
    var value = e.val();
        if (inputName == 'username'){
            if (value.length > 5 && value.length < 30){
                if( /[^a-zA-Z0-9]/.test( value ) ) {
                    $("#username-register-error").html('letters and numbers only');
                    $("#username-register-error").fadeIn(600);
                    e.addClass('register-input-error');
                    //e.attr('style','background-color:#FFE6E6;');
                    var top = e.position().top;
                    setCheckSignalPosition();
                    $("#register-check-username").addClass('register-check-error');
                    $("#register-check-username").removeClass('register-check-good');
                    $("#register-check-username").fadeIn(600);
                }else{
                    $("#username-register-error").fadeOut(600);
                    e.removeClass('register-input-error');
                    //e.attr('style','background-color:#BDFFBD;');
                    $("#register-check-username").fadeOut(600, function(){
                        var top = e.position().top;
                        setCheckSignalPosition();
                        $("#register-check-username").removeClass('register-check-error');
                        $("#register-check-username").addClass('register-check-good');
                        $("#register-check-username").fadeIn(600);
                    });
                }
            }else{
                $("#username-register-error").html('at least 6 characters');
                $("#username-register-error").fadeIn(600);
                e.addClass('register-input-error');
                //e.attr('style','background-color:#FFE6E6;');
                    var top = e.position().top;
                    setCheckSignalPosition();
                    $("#register-check-username").addClass('register-check-error');
                    $("#register-check-username").removeClass('register-check-good');
                    $("#register-check-username").fadeIn(600);
            }
        }else if (inputName == 'email'){
            var atpos=value.indexOf("@");
            var dotpos=value.lastIndexOf(".");
            if (atpos<1 || dotpos<atpos+2 || dotpos+2>=value.length)
              {
                $("#email-register-error").html('not a valid email');
                $("#email-register-error").fadeIn(600);
                e.addClass('register-input-error');
                //e.attr('style','background-color:#FFE6E6;');
                    var top = e.position().top;
                    //console.log(top);
                    setCheckSignalPosition();
                    $("#register-check-email").addClass('register-check-error');
                    $("#register-check-email").removeClass('register-check-good');
                    $("#register-check-email").fadeIn(600);
              }else{
                    $("#email-register-error").fadeOut(600);
                    e.removeClass('register-input-error');
                    //e.attr('style','background-color:#BDFFBD;');
                    $("#register-check-email").fadeOut(600, function(){
                        var top = $("#google-register-email").position().top;
                        //console.log(top);
                        setCheckSignalPosition();
                        $("#register-check-email").removeClass('register-check-error');
                        $("#register-check-email").addClass('register-check-good');
                        $("#register-check-email").fadeIn(600);
                    });
                }
        }else{
            //password
            var noWhitespaces = /^\w+$/;
            var number = /[0-9]/;
            var lowerLetter = /[a-z]/;
            var upperLetter = /[A-Z]/;
            var correctPassword = false;
            if (value=="" || value.length <= 5){
                $("#password-register-error").html('6 or more characters');
            }else if (!noWhitespaces.test(value)){
                $("#password-register-error").html('no spaces');
            }else if (!number.test(value)){
                $("#password-register-error").html('at least 1 number');
            }else if (!lowerLetter.test(value)){
                $("#password-register-error").html('at least 1 lowercase');
            }else if (!upperLetter.test(value)){
                $("#password-register-error").html('at least 1 uppercase');
            }else{
                correctPassword = true;
            }

            if (!correctPassword){
                $("#password-register-error").fadeIn(600);
                e.addClass('register-input-error');
                //e.attr('style','background-color:#FFE6E6;');
                    var top = e.position().top;
                    //console.log(top);
                    setCheckSignalPosition();
                    $("#register-check-password").addClass('register-check-error');
                    $("#register-check-password").removeClass('register-check-good');
                    $("#register-check-password").fadeIn(600);
            }else{
                $("#password-register-error").fadeOut(600);
                    e.removeClass('register-input-error');
                    //e.attr('style','background-color:#BDFFBD;');
                    $("#register-check-password").fadeOut(600, function(){
                        var top = $("#google-register-password").position().top;
                        //console.log(top);
                        setCheckSignalPosition();
                        $("#register-check-password").removeClass('register-check-error');
                        $("#register-check-password").addClass('register-check-good');
                        $("#register-check-password").fadeIn(600);
                    });
            }
        }
}


function setCheckSignalPosition(){
    $("#register-check-username").css({'top':(($("#google-register-username").position().top)+7)+"px"});
    $("#register-check-email").css({'top':(($("#google-register-email").position().top)+7)+"px"});
    $("#register-check-password").css({'top':(($("#google-register-password").position().top)+7)+"px"});
}













