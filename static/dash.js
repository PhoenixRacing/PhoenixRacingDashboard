$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('updateSpeed', function(msg) {
        $('#speed_list').html('<span>' + msg.speed + '</span>');
    });
    setInterval(getSpeed, 150);
    function getSpeed() {
        socket.emit('update', {data : {}});    
    }

    socket.on('updatePtime', function(msg) {
        $('#prev_time').html('<p>' + msg.prev + '</p>');
    });
    setInterval(getPtime, 100);
    function getPtime() {
        socket.emit('update ptime', {data : {}});
    }

    socket.on('updateCtime', function(msg) {
        $('#curr_time').html('<p>' + msg.curr + '</p>');
    });
    setInterval(getCtime, 100);
    function getCtime() {
        socket.emit('current time', {data : {}});
    }
 });
