import pyaudio
import serial
import time
import numpy as np
import audioop

# Audio settings
FPB = 1024        
FORMAT = pyaudio.paInt16  
CHANNELS = 1       
RATE = 44100        


# Serial settings
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

# Initialize serial communication with Arduino
serial_com = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)  

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=FPB)


try:
    while True:  
        data = stream.read(FPB) 

        # Convert data (get RMS, normalize and scale)
        rms = audioop.rms(data,2) 
        normalized_rms = rms/32768 
        scaled_magnitude = int(normalized_rms*255)

        # Send the value to Arduino via serial communication
        serial_com.write(bytes([scaled_magnitude]))

        time.sleep(0.01)
except KeyboardInterrupt:
    print("Audio capturing stopped.")

finally:
    # Stop and close stream, terminate PyAudio and close serial connection
    stream.stop_stream()
    stream.close()
    audio.terminate()
    serial_com.close()
