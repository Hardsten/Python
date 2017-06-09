import pygame.mixer
from pygame.mixer import Sound
from signal import pause
from gpiozero import Button

pygame.mixer.init()
button_sounds = {
    Button(2): Sound("File 1.wav"),
    Button(3): Sound("File 2.wav"),
}

for button, sound in button_sounds.items():
    button.when_pressed = pygame.mixer.stop
    button.when_released = sound.play

pause()
