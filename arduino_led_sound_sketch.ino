int pwmPin = 5; // PWM pin

void setup() {
  Serial.begin(9600); // Initialize serial communication 
  TCCR0B = TCCR0B & 0b11111000 | 0x01; // Sets prescalar to 1 to maximize PWM frequency (62.5 kHz)
  pinMode(pwmPin, OUTPUT); // Set pin as output
}

void loop() {
  if (Serial.available() > 0) {
    int sound_magnitude = Serial.read(); // Read the sound value from serial com
    analogWrite(pwmPin, sound_magnitude); // Output the PWM signal
  }
}