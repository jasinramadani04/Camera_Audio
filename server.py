from flask import Flask, request
import cv2
import pyaudio
import wave

app = Flask(__name__)

@app.route('/activate', methods=['POST'])
def activate():
    # Aktivizo kamerën
    camera = cv2.VideoCapture(0)
    return 'Kamera është aktivizuar.'

@app.route('/deactivate', methods=['POST'])
def deactivate():
    # Nderro gjendjen e kamerës
    camera.release()
    return 'Kamera është çaktivizuar.'

@app.route('/record', methods=['POST'])
def record():
    # Regjistro audio
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = 'recording.wav'

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return 'Regjistrimi u krye.'

if __name__ == '__main__':
    app.run()
