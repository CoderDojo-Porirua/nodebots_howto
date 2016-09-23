var Cylon = require('cylon');

function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function xyToDegrees(x, y) {
  return Math.round(Math.atan2(y, x) * 180 / Math.PI) + 180;
}

function xyToSpeed(x, y) {
  var speed = Math.round(Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)));
  if (speed > 100) return 0;
  return speed;
}

function oneInEvery(number, every) {
  return !(number % every);
}

Cylon.robot({
  connections: {
    leapmotion: {adaptor: 'leapmotion'},
    sphero:     {adaptor: 'sphero', port: 'COM6'}
  },
  devices: {
    leapmotion: {driver: 'leapmotion', connection: 'leapmotion'},
    sphero:     {driver: 'sphero', connection: 'sphero'}
  },

  work: function(my) {
	var counter = 0;
    my.leapmotion.on('hand', function(hand) {
	  counter++;
	  if(oneInEvery(counter, 50)) {
	    var direction = xyToDegrees(hand.palmX, hand.palmZ);
	    var speedX = hand.palmX.fromScale(-400, 400).toScale(-200, 200);
	    var speedZ = hand.palmZ.fromScale(-400, 400).toScale(-200, 200);
	    var speed = xyToSpeed(speedX, speedZ);
	    var red = Math.round(speed.fromScale(0, 100).toScale(0, 255));
	    var green = 255 - red;
		var colour = rgbToHex(red, green, 0);
	    //var height = hand.palmY.fromScale(0, 400).toScale(0, 255);
		my.sphero.roll(speed, direction);
		my.sphero.color(colour);
        //my.sphero.randomColor();
		console.log(direction + " degrees at " + speed + " % speed, colour " + color);
	  }
    });
  }
})

Cylon.start();