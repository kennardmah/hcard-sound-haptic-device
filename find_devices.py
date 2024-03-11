import pyaudio

def find_device(pyaudio_instance):
    for i in range(pyaudio_instance.get_device_count()):
        dev_info = pyaudio_instance.get_device_info_by_index(i)
        print(dev_info)
        # if dev_info['name'].startswith('BlackHole') and dev_info['maxInputChannels'] >= CHANNELS:
            # return i
    print('done')
    return

p = pyaudio.PyAudio()
find_device(p)
