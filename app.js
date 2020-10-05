var spawn = require('child_process').spawn;
var io = require('socket.io-client');
var socket = io.connect("http://localhost:3000", {
    reconnection: true
});

socket.on('connect', function(sock) { 
    console.log('Connected!');
    socket.emit('piconnected',{id:"PiZero"});

    socket.on('setRGB', function(sock) { 
        const python = spawn('python3', ['./start_leds.py', JSON.stringify(sock) ]);

        var dataToSend;

        python.stdout.on('data', function (data) {
            console.log('Stream data...');
            dataToSend += data.toString();
        });

        python.on('close', (code) => {
            console.log(`Child process exit code ${code}`);
            console.log(dataToSend);
        });

        python.stdin.end();
    });
});