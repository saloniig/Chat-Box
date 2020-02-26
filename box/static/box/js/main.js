$('.login100-form-btn').click(function() {
    var catid;
    catid = document.getElementById("username").value;
    //catid = $(this).attr("data-catid");
    $.ajax({
        type: "GET",
        url: "/search",
        data: {
            username: catid
        },
        success: function(data) {
            data = JSON.parse(data);
            var body = document.body;
            counter = 0;
            document.getElementById("insert").innerHTML = "";

            var insert = document.getElementById("insert");
            var a = document.createElement('a');
            var link = document.createTextNode(data["username"]);
            document.getElementById("insert").style.textAlign = "center";
            document.getElementById("insert").style.fontSize = "30px ";

            a.style = 'color:white;font-size:20px,  '

            a.appendChild(link);
            a.title = data["username"];
            a.href = "https://www.geeksforgeeks.org";
            insert.appendChild(a);


            // var new_row = insert.parentNode.insertRow();
            // put_data = data["username"];
            // put_data = put_data.replace(/\n/g, "<br />");
            // new_row.insertCell(0).innerHTML = put_data;

            console.log(data)
                //alert(data);
                //$('#search' + search).remove();
                //$('#message').text(data);

        }
    });
});



$("#profile-img").click(function() {
    $("#status-options").toggleClass("active");
});

$(".expand-button").click(function() {
    $("#profile").toggleClass("expanded");
    $("#contacts").toggleClass("expanded");
});

$("#status-options ul li").click(function() {
    $("#profile-img").removeClass();
    $("#status-online").removeClass("active");
    $("#status-away").removeClass("active");
    $("#status-busy").removeClass("active");
    $("#status-offline").removeClass("active");
    $(this).addClass("active");

    if ($("#status-online").hasClass("active")) {
        $("#profile-img").addClass("online");
    } else if ($("#status-away").hasClass("active")) {
        $("#profile-img").addClass("away");
    } else if ($("#status-busy").hasClass("active")) {
        $("#profile-img").addClass("busy");
    } else if ($("#status-offline").hasClass("active")) {
        $("#profile-img").addClass("offline");
    } else {
        $("#profile-img").removeClass();
    };

    $("#status-options").removeClass("active");
});

function newMessage() {
    message = $(".message-input input").val();
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="sent"><img src="http://emilcarlsson.se/assets/mikeross.png" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollTop: $(document).height() }, "fast");
};

$('.submit').click(function() {
    newMessage();
});

$(window).on('keydown', function(e) {
    if (e.which == 13) {
        newMessage();
        return false;
    }

});