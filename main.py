import pygame,sys
from Button import Button
from Text import Text

pygame.init()

size = width, heigth = 480, 320
screen = pygame.display.set_mode(size)
paused = False

buttons = []
b = Button(20, 20, (30,20), 'rect')
b.setAction(lambda : print("Inside"))
buttons.append(b)

text = Text("TEST")
text.setPos((20,40))
text.color = (0,0,0)

b.text = text

while not paused:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                btn.clicked(pygame.mouse.get_pos())
            # print(pygame.mouse.get_pos())        

    
    screen.fill(pygame.Color(20,60,180))
    text.show(screen)
    for btn in buttons:
        btn.show(screen)
    pygame.display.flip()