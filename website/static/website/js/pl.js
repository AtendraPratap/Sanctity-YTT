window.onload = function () {
    $('#pl-form').validator();
    $(".success-text").hide();
    sessionStorage.setItem("otp_verified", false);
    // sessionStorage.setItem("loan_sms", false);
    $(".error-text").hide();
    $('#get-otp-btn').on('click', function () {

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {

                    var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                        }
                   }
               }
               return cookieValue;
           }
           var csrftoken = getCookie('csrftoken');

          function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
           }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
        });





        var phone = $("#id_mobile_number_1").val();
        if (phone.length == 10 && /^\d+$/.test(phone)) {
            $.post("/otp/", {mobile: phone}, function (data, status) {
                if (status == 'success') {
                    $('#otp-modal').modal('show');
                }
                else {
                    alert("Something went wrong, please try again later!");
                }
            });
        }
        else {
            alert("Invalid Phone Number, please check and try again.");
        }
    });
    $('#otp-ver').on('click', function () {
        var phone = $("#id_mobile_number_1").val();
        var otp = $("#votp").val();
        $.post("/votp/", { number: phone, otp: otp }, function (data, status) {
            if (data == 'success') {                    
                $('#otp-modal').modal('hide');
                // $(".success-text").show();
                $("#get-otp-btn").attr("disabled", "disabled");
                $("#id_mobile_number_1").attr("readonly", "readonly");
                sessionStorage.setItem("otp_verified", true);
                $("#deposit").trigger('click');
                $.post("/sms_confirm/", {mobile: phone}, function(data, status){
                    if(data=='SUCCESS') {
                        console.log('Successful');
                    }
                    else {
                        console.log('Unsuccessful');
                    }
                });
                
                
               
            }
            else {
                sessionStorage.setItem("otp_verified", false);
               $(".error-text").show();
               return false
            }
        });
    });

    $('#pl-form').validator().on('submit', function (e) {
        var otp_val = (sessionStorage.getItem("otp_verified") == 'true');
        if (e.isDefaultPrevented()) {
            e.preventDefault();
        } else if (otp_val === false ) {
            // alert('Please try again');
            e.preventDefault();
        } else if (otp_val === true && e.isDefaultPrevented() === true) {
        }
    });
};

    