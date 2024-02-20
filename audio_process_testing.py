import pyaudio
import numpy as np
# import time
import pandas as pd

# Define the audio stream parameters
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 8  # Number of audio channels for 7.1 surround sound
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# Initialize PyAudio
p = pyaudio.PyAudio()

# Function to calculate amplitude, adjusted for multiple channels
def amplitude(samples):
    return np.max(np.abs(samples), axis=0)

# Attempt to find the BlackHole device index
def find_blackhole_device_index(pyaudio_instance):
    for i in range(pyaudio_instance.get_device_count()):
        dev_info = pyaudio_instance.get_device_info_by_index(i)
        if dev_info['name'].startswith('BlackHole') and dev_info['maxInputChannels'] >= CHANNELS:
            return i
    return None

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
testing = []

try:
    while True:
        # READ DATA AND CONVERT TO AUDIO DATA
        data = stream.read(CHUNK, exception_on_overflow=False)
        # Convert data to numpy array for analysis, reshaped for CHANNELS
        audio_data = np.frombuffer(data, dtype=np.int16).reshape(-1, CHANNELS)

        # RECORD AUDIO DATA TO CSV FILE TO INTERPRET MANUALLY (COMMENT OUT)

        # df = pd.DataFrame(audio_data, columns=[f'Channel_{i+1}' for i in range(audio_data.shape[1])])
        # df.to_csv('audio_data.csv', mode='a', header=False, index=True)  # Append mode, no header, with index
        
        # CALCULATE AND PRINT AMPLITUDE FOR AUDIO DATA
        intensity = amplitude(audio_data)
        testing.append([intensity[0], intensity[1]])
        print(intensity)
except KeyboardInterrupt:
    # Stop and close the stream
    print("Stopping audio stream...")
    print(testing)
    stream.stop_stream()
    stream.close()
    # Terminate PyAudio
    p.terminate()