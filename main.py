import pygame,sys
from Button import Button

size = width, heigth = 480, 320
screen = pygame.display.set_mode(size)
paused = False

buttons = []
buttons.append(Button(screen, 20, 20, (20,20), 'rect'))

while not paused:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                btn.clicked(pygame.mouse.get_pos())
            # print(pygame.mouse.get_pos())        

    
    screen.fill(pygame.Color(20,60,180))
    for btn in buttons:
        btn.show()
    pygame.display.flip()