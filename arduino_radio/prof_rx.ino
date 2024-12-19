#include <SoftwareSerial.h>
char cmd;
char old_cmd;

void setup() {
    ArduinoMaster.begin(9600);
}

void loop() {
    old_cmd=cmd;
    // Read data from master
    if (ArduinoMaster.available()) {
        cmd=ArduinoMaster.read();
    }
}