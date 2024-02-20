import pyaudio
import numpy as np
import serial
import time

# Function to calculate amplitude, adjusted for multiple channels
def amplitude(samples):
    return np.max(np.abs(samples), axis=0)

# Function to maintain a running average for real-time smoothing
class RealTimeSmooth:
    def __init__(self, window_size):
        self.window_size = window_size
        self.data = np.zeros((window_size, CHANNELS), dtype=np.float32)
        self.index = 0

    def add_data(self, new_data):
        self.data[self.index % self.window_size] = new_data
        self.index += 1
        if self.index < self.window_size:
            # Not enough data yet for a full window
            return np.mean(self.data[:self.index], axis=0)
        else:
            return np.mean(self.data, axis=0)

# Attempt to find the BlackHole device index
def find_blackhole_device_index(pyaudio_instance):
    for i in range(pyaudio_instance.get_device_count()):
        dev_info = pyaudio_instance.get_device_info_by_index(i)
        if dev_info['name'].startswith('BlackHole') and dev_info['maxInputChannels'] >= CHANNELS:
            return i
    return None

# Initialize PyAudio
p = pyaudio.PyAudio()

# Define Audio Stream Parameters
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 2  # Number of audio channels for stereo sound
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# Initialize serial connection
arduino = serial.Serial('COM_PORT', 9600)  # Replace 'COM_PORT' with your Arduino's COM port
time.sleep(2)  # Wait for the connection to establish

blackhole_index = find_blackhole_device_index(p)

if blackhole_index is None:
    print("BlackHole device with sufficient channels not found.")
    p.terminate()
    exit()

# Open stream with BlackHole as input
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=blackhole_index,  # Use BlackHole device index
                frames_per_buffer=CHUNK)

print("Starting audio stream...")
smooth = RealTimeSmooth(window_size=5*int(RATE/CHUNK))  # Adjust window size as needed

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16).reshape(-1, CHANNELS)
        intensity = amplitude(audio_data)
        smoothed_intensity = smooth.add_data(intensity)
        # Convert intensity to string and send to Arduino
        send_str = f"{int(smoothed_intensity[0])},{int(smoothed_intensity[1])}\n"
        arduino.write(send_str.encode())
except KeyboardInterrupt:
    print("Stopping audio stream...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    arduino.close()  # Close the serial connection