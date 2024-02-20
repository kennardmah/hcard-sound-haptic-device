import pyaudio
import numpy as np

# Initialize PyAudio
p = pyaudio.PyAudio()
device_index = 0  # Make sure this is the correct device index

# Open stream for stereo audio
stream = p.open(format=pyaudio.paInt16,
                channels=8,  # Stereo
                rate=48000,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=1024)

for i in range(200):
    # Read data from audio input
    data = stream.read(1024)

    # Convert data to numpy array, assuming interleaved stereo data
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Reshape audio_data to separate channels
    # The resulting array has shape [2, N/2] where N is the original number of samples
    audio_data = np.reshape(audio_data, (-1, 2))

    # Calculate a simple metric for amplitude - the average of absolute values across both channels
    amplitude = np.mean(np.abs(audio_data))

    print(int(amplitude))  # Convert the amplitude to an integer before printing

# Close the stream
stream.stop_stream()
stream.close()
p.terminate()
