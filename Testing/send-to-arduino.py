import serial
import time

# Initialize serial port connection
# Replace 'COM_PORT' with your Arduino's actual COM port
arduino = serial.Serial('COM_PORT', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

def send_data_to_arduino(data):
    arduino.write(f"{data}\n".encode())

# Example function that processes audio and calls send_data_to_arduino
def process_audio_and_send():
    # Your audio processing logic here
    # For demonstration, we'll just send a simple message
    audio_data = "Hello Arduino"
    send_data_to_arduino(audio_data)

try:
    while True:
        process_audio_and_send()
        time.sleep(1)  # Pause for a moment
except KeyboardInterrupt:
    print("Program terminated")
finally:
    arduino.close()  # Ensure serial connection is closed on exit