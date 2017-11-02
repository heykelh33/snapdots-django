$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/sensor/");
    
    chatsock.onopen = function() {
           console.log("Connectado con WebSocket! ");
           //$('#sensor').text("Connected!");
           chatsock.send("Connected!");
    };

    chatsock.onmessage = function message(event) {
        console.log("sensor.js: Received Sock message! "+ event.data);
        //var data=JSON.parse(event.data);
        //var data=encodeURI(JSON.parse(event.data)['text']);     
        $('#sensor').text(encodeURI(JSON.parse(event.data)['text']));
    };

    if (chatsock.readyState == WebSocket.OPEN) {
      chatsock.onopen();
    }

});
