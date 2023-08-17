/*
  Arduino FS-I6X Demo
  fsi6x-arduino-mega-ibus.ino
  Read iBus output port from FS-IA6B receiver module
  Display values on Serial Monitor

  Channel functions by Ricardo Paiva - https://gist.github.com/werneckpaiva/

  DroneBot Workshop 2021
  https://dronebotworkshop.com
*/

// Include iBusBM Library
#include <IBusBM.h>

// Create iBus Object
IBusBM ibus;


// Read the number of a given channel and convert to the range provided.
// If the channel is off, return the default value
int readChannel(byte channelInput, int minLimit, int maxLimit, int defaultValue) {
  uint16_t ch = ibus.readChannel(channelInput);
  if (ch < 100) return defaultValue;
  return map(ch, 1000, 2000, minLimit, maxLimit);
}

// Read the channel and return a boolean value
bool readSwitch(byte channelInput, bool defaultValue) {
  int intDefaultValue = (defaultValue) ? 100 : 0;
  int ch = readChannel(channelInput, 0, 100, intDefaultValue);
  return (ch > 50);
}

void setup() {
  // Start serial monitor
  Serial.begin(115200);

  // Attach iBus object to serial port
  ibus.begin(Serial1);
}

void loop() {

  // Cycle through first 5 channels and determine values
  // Print values to serial monitor
  // Note IBusBM library labels channels starting with "0"

  double V = readChannel(2, -100, 100, 0)+100;

  double vx = readChannel(1, -100, 100, 0)-1;
  double vy = readChannel(0, -100, 100, 0)+1;

  double vr = ((vx-vy)/100)*V;
  double vl = ((vx+vy)/100)*V;

  Serial.print(int(vl));
  Serial.println('L');
  Serial.print(int(vr));
  Serial.println('R');

  delay(20);
}
