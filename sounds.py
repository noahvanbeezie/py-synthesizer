from abc import ABC, abstractmethod

class Sound(ABC):
    @abstractmethod
    def play(self, frequency, duration, rate):
        ...

class SineSound(Sound):
    def play(self, frequency, duration, rate):
        ...