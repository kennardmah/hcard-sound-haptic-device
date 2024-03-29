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
#         ♬♪♫♪♬  Device Detection - Find Audio Output  ♬♪♫♪♬
# ====================================================================
    
def find_blackhole_device_index(pyaudio_instance):
    for i in range(pyaudio_instance.get_device_count()):
        dev_info = pyaudio_instance.get_device_info_by_index(i)
        if dev_info['name'].startswith('BlackHole') and dev_info['maxInputChannels'] >= CHANNELS:
            return i
    return None

# we can add one for JackAudio

# ====================================================================
#    ♬♪♫♪♬  Arduino Communication - Convert and Send Signals  ♬♪♫♪♬
# ====================================================================

def convert_for_arduino(smoothed_intensity):
    # update later
    if smoothed_intensity > 10:
        return 1
    return 0

# INITIALIZE PYAUDIO
p = pyaudio.PyAudio()

# ====================================================================
#     ♬♪♫♪♬  Stream Configuration - Define Audio Parameters  ♬♪♫♪♬
# ====================================================================

FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 5  # Number of audio channels for stereo sound
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# SERIAL CONNECTION SET-UP
COM_PORT = '/dev/cu.usbmodem144301'
arduino = serial.Serial(COM_PORT, 9600) # COMMENT OUT W/O ARDUINO
time.sleep(2) # slight delay for connection

blackhole_index = find_blackhole_device_index(p)

if blackhole_index is None:
    print("No device with sufficient channels not found.")
    p.terminate()
    exit()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                # input_device_index=blackhole_index,
                frames_per_buffer=CHUNK)

# ====================================================================
#      ♬♪♫♪♬  Audio Plotting - Finding the Range  ♬♪♫♪♬
# ====================================================================

def plot_stereo_sound(stereo_audio_list, rate=44100, chunk=1024):
    left = [item[0] for item in stereo_audio_list]
    right = [item[1] for item in stereo_audio_list]
    indices_per_second = rate/chunk
    time = np.arange(len(stereo_audio_list)) / indices_per_second
    plt.plot(time, left, label='Left Ear')
    plt.plot(time, right, label='Right Ear')
    plt.title('Linear Graph of Left and Right Amplitude')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.legend()
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

        # defining and converting intensity into 0, 128, 256
        intensity = amplitude(audio_data)
        intensity = smooth.add_data(intensity)
        data_normalized = [0 if value < 800 else 128 if value < 2000 else 255 for value in intensity]
        cmdArrayFloat = np.array(data_normalized, dtype=np.uint8) # array of 2 uint8
        # print(data_normalized)
        cmd_bytes = cmdArrayFloat.tobytes() # array of 16 bytes
        testing.append([data_normalized[0], data_normalized[1]])  # Storing data for plotting
        # print(cmd_bytes)
        n = arduino.write(cmd_bytes)# send the command # COMMENT OUT W/O ARDUINO
        # print(f"{n} bytes sent")
except KeyboardInterrupt:
    print("Stopping audio stream...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    plot_stereo_sound(testing, RATE, CHUNK)  # Plotting after stopping the stream with a keyboard interrupt
    # arduino.close()
