const { spawn } = require('child_process');
const { Scanner } = require('spherov2.js');

let coords;
const pythonScript = spawn('python3', ['coords.py']);

pythonScript.stdout.on('data', (data) => {
  coords = data.toString();
});

pythonScript.stderr.on('data', (data) => {
  console.log(data);
});

pythonScript.on('close', async (data) => {
  const sphero = await Scanner.findSpheroMini();
  await sphero.setMainLedColor(0, 0, 255);

  let coordinates = coords.split('\r\n');
  let pinCoords = coordinates.shift().replace(/([(])/g, '').replace(/([)])/g, '');
  let spheroCoords = coordinates.shift().replace(/([(])/g, '').replace(/([)])/g, '');

  let pinCoordsSplit = pinCoords.split(',');
  let spheroCoordsSplit = spheroCoords.split(',');

  let pinLocation = {
    x: pinCoordsSplit[1],
    y: pinCoordsSplit[0],
  };

  let spheroLocation = {
    x: spheroCoordsSplit[1],
    y: spheroCoordsSplit[0],
  };

  let angle = (Math.atan2(spheroLocation.y - pinLocation.y, spheroLocation.x - pinLocation.x) * 180) / Math.PI;
  if (spheroLocation.x > pinLocation.x) angle = 360 - angle;
  console.log(angle);

  await sphero.rollTime(120, Math.abs(angle), 800, []);
  await sphero.rollTime(120, 180, 800, []);
});
