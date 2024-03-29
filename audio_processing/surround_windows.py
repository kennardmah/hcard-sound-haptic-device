# ====================================================================
#             ♬♪♫♪♬  Audio Setup - Initial Imports  ♬♪♫♪♬
# ====================================================================

import pyaudio
import numpy as np
import serial
import time
import matplotlib.pyplot as plt

# ====================================================================
#      ♬♪♫♪♬  Real-Time Processing - Audio Data Processing ♬♪♫♪♬
# ====================================================================

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

# CALCULATE AUDIO SOUND AMPLITUDE
def amplitude(samples):
    return np.max(np.abs(samples), axis=0)

# ====================================================================
#     ♬♪♫♪♬  Stream Configuration - Define Audio Parameters  ♬♪♫♪♬
# ====================================================================

# INITIALIZE PYAUDIO
p = pyaudio.PyAudio()

FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 6  # Number of audio channels for stereo sound
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# SERIAL CONNECTION SET-UP
COM_PORT = '/dev/cu.usbmodem144401' # Change based on computer
arduino = serial.Serial(COM_PORT, 500000) # COMMENT OUT W/O ARDUINO
time.sleep(2) # Slight delay for connection

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                # input_device_index=blackhole_index,
                frames_per_buffer=CHUNK)

# ====================================================================
#      ♬♪♫♪♬  Audio Plotting - Finding the Range  ♬♪♫♪♬
# ====================================================================

def plot_surround_sound(audio_list):
    channels = np.array(audio_list).T  # Transpose to get channels as lists
    time = np.arange(channels.shape[1]) * CHUNK / RATE
    plt.figure(figsize=(10, 8))
    for i, channel_data in enumerate(channels):
        plt.subplot(CHANNELS, 1, i+1)
        plt.plot(time, channel_data, label=f'Channel {i+1}')
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()

# ====================================================================
#      ♬♪♫♪♬  Audio Stream - Capture and Process Audio  ♬♪♫♪♬
# ====================================================================

print("Starting audio stream...")
smooth = RealTimeSmooth(window_size=int(RATE/CHUNK))
testing = []

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16).reshape(-1, CHANNELS)
        # Defining and converting intensity into 0, 75, 100
        intensity = amplitude(audio_data)
        intensity = smooth.add_data(intensity)
        for i, value in enumerate(intensity):
            if i == 0 or i == 1 or i == 2:
                intensity[i] = 0 if value < 2000 else 75 if value < 8000 else 100 # Front two audio channels
            else:
                intensity[i] = 0 if value < 1000 else 75 if value < 2000 else 100 # Back two audio channels
        cmdArrayFloat = np.array(intensity, dtype=np.uint8) # Array of 2 uint8
        cmd_bytes = cmdArrayFloat.tobytes() # Array of 16 bytes
        testing.append(intensity)  # Convert np.array to list for easier handling later
        n = arduino.write(cmd_bytes) # Send to Arduino # COMMENT OUT W/O ARDUINO
except KeyboardInterrupt:
    print("Stopping audio stream...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    plot_surround_sound(testing)  # Plotting after stopping the stream with a keyboard interrupt
    arduino.close()
