var Cylon = require("cylon");

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
    raspi: { adaptor: 'raspi' },
    leapmotion: { adaptor: 'leapmotion', host: '192.168.1.64' }
  },

  devices: {
    led: { driver: 'led', pin: 11 },
    leapmotion: { driver: 'leapmotion' },

    motorL: { driver: 'motor', pin: 3 },
    motorR: { driver: 'motor', pin: 3 }
  },

  work: function(my) {
    every((1).second(), my.led.toggle);

    var counter = 0;
    my.leapmotion.on('hand', function(hand) {
	  counter++;
	  if(oneInEvery(counter, 50)) {
	    var direction = xyToDegrees(hand.palmX, hand.palmZ);
	    var positionX = hand.palmX.fromScale(-400, 400).toScale(-200, 200);
	    var speed = hand.palmZ.fromScale(-400, 400).toScale(-200, 200);

      var speed = xyToSpeed(speedX, speedZ);



	    my.sphero.roll(speed, direction);
  		my.sphero.color(colour);
          //my.sphero.randomColor();
  		console.log(direction + " degrees at " + speed + " % speed, colour " + color);
  	  }
    });

  }
}).start();
