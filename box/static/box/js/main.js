var global_data;
var datetime="";



setInterval(function(){
        $.ajax({
        type: "GET",
        url: '/fetch_data' ,
        data: {
                reciever_id: global_data,

        },    
        success: function (data){
              response_json = JSON.parse(data)
                if (datetime == ""){
              datetime = response_json["datetime"]; 
                }
                else{
            
                         if(datetime!=response_json["datetime"]){
                                 datetime = response_json["datetime"];

                                 newMessagerecieved1(response_json["message"]);
            }   

                }
           }
        });

   
   },4000);


$('.insert').click(function(){
    var img = Document.getElementById('profile-img');
    
img.src ="{{ hotel.hotel_Main_Img.url }}"
document.getElementById("profile-img").appendChild(img);



});
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

        a.title = data["username"];

        insert.appendChild(a);

        document.getElementById("_username_").innerHTML = "";
        document.getElementById("_username_").innerHTML = data.username;


            var img = document.getElementById('profile-img2');
            img.src = "/media/" + data["hotel_Main_Img"];
            global_data = data["id"];
            msg = data["msg"]
	    document.getElementById("messages").innerHTML = ""; 
        //console.log(msg);
            for(message in msg){
                if(msg[message][2] == data["id"])
                    {
                            newMessagerecieved1(msg[message][1]);
                    }
                    else{
                                newMessage1(msg[message][1]);
                    }
            }
        }
    });
});

function newMessage1(message) {
    $('<li class="sent" align = "right"><p>' + message + '</p></li>').appendTo($('.messages ul'));
    
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollBottom: $(document).height() }, "fast");
};
function newMessagerecieved1(message) {
    $('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));
    
    $('.contact.active .preview').html('<span>You: </span>' + message);
};

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

function newMessagerecieved() {
    message = response_json["message"];
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));

    $('.contact.active .preview').html('<span>You: </span>' + message);
    //$(".messages").animate({ scrollTop: $(document).height() }, "fast");
};
function newMessage() {
    message = $(".message-input input").val();
    if ($.trim(message) == '') {
        return false;
    }   
    $('<li class="sent" align = "right"><p>' + message + '</p></li>').appendTo($('.messages ul'));

    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
};

$('.message-input input').keypress(function() {
	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode=='13'){
//		alert('you press enter key')
	

    message = $(".message-input input").val();
   id = global_data;
        $.ajax(
        {
            type:"GET",
            url: "/likepost",
            data:{
                     post_id: message,
                    reciever_id: id,
            },
            success: function( data )
            {
                newMessage();
            }
	
	
    });
	}

});

$('.submit').click(function() {
//        var keycode = (event.keyCode ? event.keyCode : event.which);
  //      if(keycode=='13'){
//              alert('you press enter key')


    message = $(".message-input input").val();
   id = global_data;
        $.ajax(
        {
            type:"GET",
            url: "/likepost",
            data:{
                     post_id: message,
                    reciever_id: id,
            },
            success: function( data )
            {
                newMessage();
            }


    });
        

});



                
