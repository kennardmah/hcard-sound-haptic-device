import pyaudio
import numpy as np
import serial
import time

# CALCULATE AUDIO SOUND AMPLITUDE
def amplitude(samples):
    return np.max(np.abs(samples), axis=0)

# REAL-TIME WINDOW SMOOTHING
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
        
# class MovingMax:
#     def __init__(self)

# FIND BLACKHOLE INDEX
def find_blackhole_device_index(pyaudio_instance):
    for i in range(pyaudio_instance.get_device_count()):
        dev_info = pyaudio_instance.get_device_info_by_index(i)
        if dev_info['name'].startswith('BlackHole') and dev_info['maxInputChannels'] >= CHANNELS:
            return i
    return None

def convert_for_arduino(smoothed_intensity):
    if smoothed_intensity > 10:
        return 1
    return 0

# INITIALIZE PYAUDIO
p = pyaudio.PyAudio()

# DEFINE PARAMETERS FOR AUDIO STREAM
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 2  # Number of audio channels for stereo sound
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# SERIAL CONNECTION
COM_PORT = '/dev/cu.usbmodem141401'
arduino = serial.Serial(COM_PORT, 9600)
time.sleep(2)  # Wait for the connection to establish

blackhole_index = find_blackhole_device_index(p)

if blackhole_index is None:
    print("BlackHole device with sufficient channels not found.")
    p.terminate()
    exit()

# OPEN STREAM
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=blackhole_index,  # Use BlackHole device index
                frames_per_buffer=CHUNK)

print("Starting audio stream...")
smooth = RealTimeSmooth(window_size=5*int(RATE/CHUNK))

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16).reshape(-1, CHANNELS)
        intensity = amplitude(audio_data)
        smoothed_intensity = smooth.add_data(intensity)

        # convert smoothed_intensity to [0, 1]
        int1 = convert_for_arduino(smoothed_intensity[0])
        int2 = convert_for_arduino(smoothed_intensity[1])
        smoothed_intensity = [int1, int2]
        if smoothed_intensity == [0, 0]:
            send_int = f"{int(0)}\n"
        elif smoothed_intensity == [0, 1]:
            send_int = f"{int(1)}\n"
        elif smoothed_intensity == [1, 0]:
            send_int = f"{int(2)}\n"
        else:
            send_int = f"{int(3)}\n"
        
        # send_int = f"{int(smoothed_intensity[0])}\n"
        print(smoothed_intensity)
        # send_int2 = f"{int(smoothed_intensity[1])}\n"
        arduino.write(send_int.encode())
except KeyboardInterrupt:
    print("Stopping audio stream...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    arduino.close()  # Close the serial connection