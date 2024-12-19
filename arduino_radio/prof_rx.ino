#include <SoftwareSerial.h>

SoftwareSerial ArduinoMaster(2,3);
char cmd;
char old_cmd;

void setup() {
    Serial.begin(9600);
    ArduinoMaster.begin(9600);
}

void loop() {
    old_cmd=cmd;
    // Read data from master
    if (ArduinoMaster.available()) {
        cmd=ArduinoMaster.read();
    }
}