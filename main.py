import pygame
import sys
from components.Constants import *
from components.Button import Button
from components.Text import Text
from game_structures.Save import Save
from game_structures.Resource import Resource
from game_structures.Stage import Stage
from game_structures.Player import Player
from game_structures.Game_time import Game_time

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
player = Player(resources)
game_time = Game_time(60)
stage.add_component(game_time.display)

# GAME LOOP

fps_counter = 0
fps_txt = Text("0")
fps_txt.setPos((width-60, 0))

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
            fps_txt.setText("FPS: "+str(fps_counter))
            fps_counter = 0
            game_time.each_second()

    screen.fill(pygame.Color(124, 122, 122))
    stage.draw_scene(screen)
    fps_txt.draw(screen)
    fps_counter += 1
    pygame.display.flip()
