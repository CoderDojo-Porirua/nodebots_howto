var Cylon = require('cylon');
var counter = 0;

Cylon.robot({
  connections: {
    leapmotion: { adaptor: 'leapmotion' },
    sphero: { adaptor: 'sphero', port: 'COM6' }
  },

  devices: {
    leapmotion: { driver: 'leapmotion', connection: 'leapmotion' },
    sphero: { driver: 'sphero', connection: 'sphero' }
  },

  work: function(my) {
    my.leapmotion.on('hand', function(hand) {
      //var r = hand.palmY.fromScale(100, 600).toScale(0, 359) | 0;
	  //my.sphero.roll(60, r);
	  var direction = Math.atan2(hand.palmZ, hand.palmX) * 180 / Math.PI;
	  direction += 180;
	  direction = Math.round(direction);
	  var speed = hand.palmY.fromScale (0, 400).toScale(0, 100);
	  counter++;
	  
	  if(Math.abs(hand.palmZ) > 300 || Math.abs(hand.palmX) > 300){
		  speed = 0;
	  } 
	  
	  if(!(counter % 10)) {
		my.sphero.roll(speed, direction);
		console.log(direction + " at " + speed);
	  }
	  
      //my.sphero.setRgbLed(r, 0, 0);
    });
  }
})

Cylon.start();