# LED Sound Level Meter

This Arduino hobby project uses five LEDs to measure the sound level from a PC’s input microphone.

## Project Overview

The project has two main components:
1. Converting sound level to an analog voltage for input into the circuit.
2. Creating a circuit that turns on LED’s at different voltage input levels.

## Implementation Steps

To start, I used PyAudio, an audio I/O Python library, to collect microphone data. The root mean square (RMS) of this data, commonly used to measure audio volume, was calculated. The data was then normalized and scaled to a range of 0-255, which corresponds to the range of values that my Arduino’s pulse width modulation (PWM) output can take. Using UART serial communication, the data is sent to my Arduino.

Unfortunately, the Arduino is unable to output DC analog signals; it instead uses PWM. This creates an issue where all the LEDs would be active when the PWM signal is high and deactivated when it is low. To solve this, I first maximized the PWM frequency to 62.5 kHz. Additionally, I implemented a low-pass RC filter to convert the PWM signal into a smoother analog voltage. I ensured that the frequency, resistor, and capacitor values adhered to the equation:

f_c = 1 / (2 * π * C * R)

Next, I needed to turn on different LEDs at varying voltage values. To achieve this, I used NPN transistors as switches. Each LED was connected to the collector of its respective transistor. The LED will turn on when the voltage at the base exceeds the cutoff voltage (>Vbeon). I created different voltage division ratios for each base and connected them to the analog input. This setup causes the voltage at the base of each transistor to vary based on the voltage division ratio, resulting in the switches closing at different input voltage levels and achieving the desired functionality.

## Materials Used

- **PC with microphone** (or another sound input)
- **Arduino UNO**
- **5 LEDs**
- **5 NPN transistors** (I used MY2N3904)
- **1 capacitor** (I used 0.1 μF)
- **Various resistors** (I used 5 x 330Ω, 6 x 300Ω, 2 x 200Ω, 2 x 100Ω, and 1 x 25Ω)

## Conclusion

This LED Sound Level Meter provides a visual representation of audio levels using simple electronic components and programming. It was a great project for learning about signals, transistors and embedded systems.
