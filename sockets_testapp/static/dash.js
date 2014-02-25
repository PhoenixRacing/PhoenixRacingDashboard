$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('updateRes', function(msg) {
        $('#speedList').html('<p>Speed:' + msg.speed + ' Lap time: ' + msg.laptime + '</p>');
    });
    setInterval(getSpeed, 100);
    function getSpeed() {
        socket.emit('update', {data : {}});    
    }
 });


