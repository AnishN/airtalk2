var io = require("socket.io");  
var socket = io.listen(1223, "1.2.3.4");  
var people = {}; var io = require("socket.io");  


socket.on("connection", function (client) {  
    client.on("join", function(name){
        people[client.id] = name;
        client.emit("update", "You have connected to the server.");
        socket.sockets.emit("update", name + " has joined the server.")
        socket.sockets.emit("update-people", people);
    });

    client.on("send", function(msg){
        socket.sockets.emit("chat", people[client.id], msg);
    });

    client.on("disconnect", function(){
        socket.sockets.emit("update", people[client.id] + " has left the server.");
        delete people[client.id];
        socket.sockets.emit("update-people", people);
    });
});


$(document).ready(function(){  
        var socket = io.connect("1.2.3.4:1223");
        $("#chat").hide();
        $("#name").focus();
        $("form").submit(function(event){
            event.preventDefault();
        });

        $("#join").click(function(){
            var name = $("#name").val();
            if (name != "") {
                socket.emit("join", name);
                $("#login").detach();
                $("#chat").show();
                $("#msg").focus();
                ready = true;
            }
        });

        $("#name").keypress(function(e){
            if(e.which == 13) {
                var name = $("#name").val();
                if (name != "") {
                    socket.emit("join", name);
                    ready = true;
                    $("#login").detach();
                    $("#chat").show();
                    $("#msg").focus();
                }
            }
        });

        socket.on("update", function(msg) {
            if(ready)
                $("#msgs").append("
" + msg + "");
        })

        socket.on("update-people", function(people){
            if(ready) {
                $("#people").empty();
                $.each(people, function(clientid, name) {
                    $('#people').append("
" + name + "");
                });
            }
        });

        socket.on("chat", function(who, msg){
            if(ready) {
                $("#msgs").append("
" + who + " says: " + msg + "");
            }
        });

        socket.on("disconnect", function(){
            $("#msgs").append("
The server is not available
");
            $("#msg").attr("disabled", "disabled");
            $("#send").attr("disabled", "disabled");
        });


        $("#send").click(function(){
            var msg = $("#msg").val();
            socket.emit("send", msg);
            $("#msg").val("");
        });

        $("#msg").keypress(function(e){
            if(e.which == 13) {
                var msg = $("#msg").val();
                socket.emit("send", msg);
                $("#msg").val("");
            }
        });

    });
