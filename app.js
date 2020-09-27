var io = require('socket.io-client');
var socket = io.connect("http://localhost:3000", {
    reconnection: true
});

socket.on('connect', function(sock) { 
    console.log('Connected!');
    socket.emit('piconnected',{id:"PiZero"});

    socket.on('setRGB', function(sock) { 
        console.log(sock);
    });
});
