import numpy as np
import sounddevice as sd
from gui import GUI

def play_sine(frequency, duration, rate=44100):
    t = np.linspace(0, duration, int(duration * rate), False)
    amplitude = np.sin(frequency * 2 * np.pi * t)
    sd.play(amplitude, samplerate=rate)
    sd.wait()

def main():
    application = GUI()
    application.mainloop()

if __name__ == "__main__":
    main()