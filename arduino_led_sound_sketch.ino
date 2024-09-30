int pwmPin = 9; // PWM pin

void setup() {
  Serial.begin(9600);
  pinMode(pwmPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int sound_magnitude = Serial.read(); // Read the sound value from serial com
    analogWrite(pwmPin, sound_magnitude); // Output the PWM signal
  }
}