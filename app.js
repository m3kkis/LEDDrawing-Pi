var {spawn} = require('child_process');
var io = require('socket.io-client');
var socket = io.connect("http://localhost:3000", {
    reconnection: true
});

socket.on('connect', function(sock) { 
    console.log('Connected!');
    socket.emit('piconnected',{id:"PiZero"});

    socket.on('setRGB', function(sock) { 
        //console.log(sock);
        var dataToSend;
        const python = spawn('python3', ['start_leds.py']);
        python.stdin.write(JSON.stringify(sock));

        python.stdout.on('data', function (data) {
            console.log('Pipe data from python script ...');
            dataToSend = data.toString();
        });

        python.on('close', (code) => {
            console.log(`child process close all stdio with code ${code}`);
            // send data to browser
            console.log(dataToSend);
        });
    });
});