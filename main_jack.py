# ====================================================================
#             ♬♪♫♪♬  Audio Setup - Initial Imports  ♬♪♫♪♬
# ====================================================================

import jack
import pyaudio
import numpy as np

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

# SCALE AUDIO TO BECOME VIBRATION VALUES
def scale_audio_intensity(intensity):
    # write function to scale the intensity for analog write / PWM
    print('nothing here so far')

# ====================================================================
#         ♬♪♫♪♬  Device Detection - Find Audio Output  ♬♪♫♪♬
# ====================================================================

client = jack.Client("HCARD_AudioProcessor")
in_port = client.inports.register("PyAudio_Input")

# ====================================================================
#     ♬♪♫♪♬  Stream Configuration - Define Audio Parameters  ♬♪♫♪♬
# ====================================================================

# INITIALIZE PYAUDIO
p = pyaudio.PyAudio()

FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 2  # Number of audio channels for stereo sound
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# ====================================================================
#      ♬♪♫♪♬  Audio Stream - Capture and Process Audio  ♬♪♫♪♬
# ====================================================================

print("Starting audio stream...")
client.activate()
smooth = RealTimeSmooth(window_size=5*int(RATE/CHUNK))

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16).reshape(-1, CHANNELS)
        intensity = amplitude(audio_data)
        smoothed_intensity = smooth.add_data(intensity)
        print(intensity)

except KeyboardInterrupt:
    print("Stopping audio stream...")
    stream.stop_stream()
    stream.close()
    client.deactivate()
    client.close()
    p.terminate()