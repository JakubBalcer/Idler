import pygame
import sys
from components.Constants import *
from components.Button import Button
from game_structures.Save import Save
from game_structures.Resource import Resource
from game_structures.Stage import Stage

# PYGAME INIT

pygame.init()
pygame.display.set_caption("Idler")

# LOAD SAVE FILE

resources = Resource.load_resources_from_file('resources.json')
save2 = Save(save_name)
save2.deserialize()
for resource in resources:
    resource.load_from_save(save2.get_object(resource.name))

# SETTING CUSTOM EVENTS

pygame.time.set_timer(EACH_SECOND, 1000)

# SCENE INIT

size = width, height
screen = pygame.display.set_mode(size)
paused = False
stage = Stage(resources)
stage.set_scene("Forest")

# GAME LOOP

while not paused:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in filter(lambda x: isinstance(x, Button), stage.get_components()):
                btn.clicked(pygame.mouse.get_pos())
        if event.type == EACH_SECOND:
            for component in filter(lambda x: hasattr(x, 'each_second'), stage.get_components()):
                component.each_second()
                for resource in resources:
                    save2.add_object(resource.name, resource.get_save_data())
                save2.serialize()
    screen.fill(pygame.Color(124, 122, 122))
    stage.draw_scene(screen)
    pygame.display.flip()
