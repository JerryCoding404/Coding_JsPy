#撥放音樂
# windows-> python -> 

import pygame 
import time

pygame.mixer.init()
pygame.mixer.music.load("./起來現在也才3點.mp3")
pygame.mixer.music.play()

time.sleep(100)