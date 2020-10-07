# LEDDrawing-Pi [ RASPBERRRY PI ]
***IMPORTANT:** This project need https://github.com/m3kkis/LEDDrawing-Web to work properly.*

This repository is part of a project that allows users to do a drawing online on a webpage and then the information gets sent over to my raspberry pi and replicates it on my 16x16 LED frame. It is by running 2 NodeJS servers and communicating between eachother by using SocketsIO and executing a python script by spawning a child process.

![alt text](https://github.com/m3kkis/LEDDrawing-Pi/blob/master/leddraw.gif?raw=true)

## Requirements
* Raspberry Pi (In my case I used the Raspberr Pi Zero W)
* WS2812B LED
* Python 3.X
* Pip 3.X
* Nodejs v10 (only tested on v10 so far)
* PM2 (optional, depends on your need)

## Circuit
* If Raspberry Pi Zero W solder header
* Connect the 5v from LED to 5v Pin on Pi
* Connect GND to GND Pin on Pi
* Connect DIN to GPIO 18 on Pi

## Installation
```
git clone https://github.com/m3kkis/LEDDrawing-Pi.git
cd LEDDrawing-Pi
npm install
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```
## Set up
If you are going to host the WEB Server somewhere other than locally you need to make a change in the file `app.j`. Instead of connecting to `localhost:3000` just replace it with your webserver address `https://example.com`

```
var socket = io.connect("http://localhost:3000", {
```
***to***
```
var socket = io.connect("https://example.com/", {
```

## Starting up
```
node app.js
```
or if you have PM2 installed
```
pm2 start app.js
```