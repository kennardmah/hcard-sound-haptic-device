import pyaudio
import numpy as np
import time

# Define the audio stream parameters
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 8  # Number of audio channels for 7.1 surround sound
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# Initialize PyAudio
p = pyaudio.PyAudio()

# Function to calculate RMS, adjusted for multiple channels
def rms(samples):
    return np.sqrt(np.mean(np.square(samples), axis=0))

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

try:
    while True:
        # Read data from audio stream
        data = stream.read(CHUNK, exception_on_overflow=False)
        # Convert data to numpy array for analysis, reshaped for CHANNELS
        audio_data = np.frombuffer(data, dtype=np.int16).reshape(-1, CHANNELS)
        # Calculate RMS for each channel
        print(f"AudioData: {audio_data}")
        intensity = rms(audio_data)
        print(f"Intensity: {intensity}")
        time.sleep(1)  # Capture once per second
except KeyboardInterrupt:
    # Stop and close the stream
    print("Stopping audio stream...")
    stream.stop_stream()
    stream.close()
    # Terminate PyAudio
    p.terminate()
