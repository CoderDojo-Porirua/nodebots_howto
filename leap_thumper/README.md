https://cylonjs.com/documentation/platforms/leapmotion/

- Allow Web Apps
- Firewall configuration....
https://community.leapmotion.com/t/i-cant-connect-to-leap-device-on-another-pc/1315
find your Leap Motion config.json file and add:

"websockets_allow_remote": true
