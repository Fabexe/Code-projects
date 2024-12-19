#include <SoftwareSerial.h>

SoftwareSerial ArduinoSlave(2,3);
char cmd;
char old_cmd;

void setup() {
    Serial.begin(9600);
    Serial.println("ENTER Commands: ");
    ArduinoSlave.begin(9600);
}

void loop() {
    old_cmd=cmd;
    // Read command from monitor
    if (Serial.available()) {
        cmd=Serial.read();
    }

    // Send data to slave
    if (cmd!=old_cmd) {
        Serial.print("Master sent: ");
        Serial.println(cmd);
        ArduinoSlave.write(cmd);
    }
}