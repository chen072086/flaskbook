#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX


import os

os.environ['SDL_VIDEODRIVEDR'] = 'dummy'
import  pygame
pygame.init()
pygame.display.set_mode((1,1))

while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            key_input = pygame.key.get_pressed()
            print(key_input)
