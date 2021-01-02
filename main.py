import pygame
import sys
import time
import configparser
import pickle
from components.Button import Button
from components.Text import Text
from components.Counter import Counter
from components.Sprite import Sprite
from game_structures.Save import Save

# PYGAME INIT

pygame.init()
pygame.display.set_caption("Idler")

# LOAD SAVE FILE

save = Save('save')
save = save.load_from_file()

# LOAD CONFIG FROM FILE

config = configparser.ConfigParser()
config.read('config.ini')

width = int(config.get('window_settings', 'resolution_width'))
height = int(config.get('window_settings', 'resolution_height'))

# CONSTANTS

EACH_SECOND = pygame.USEREVENT
OAK_LOG_IMG = config.get('img_assets', 'oak_log')
BASIC_AXE_IMG = config.get('img_assets', 'basic_axe')
DARK_OAK_LOG_IMG = config.get('img_assets', 'dark_oak_log')
BASIC_TREE_IMG = config.get('img_assets', 'basic_tree')
COIN_IMG = config.get('img_assets', 'basic_coin')
SMALL_COIN_IMG = config.get('img_assets', 'small_basic_coin')
SMALL_SILVER_COIN_IMG = config.get('img_assets', 'small_silver_coin')
SILVER_COIN_IMG = config.get('img_assets', 'silver_coin')

# SETTING CUSTOM EVENTS

pygame.time.set_timer(EACH_SECOND, 1000)

# SCENE INIT

size = width, height
screen = pygame.display.set_mode(size)
paused = False

# GAME SCENE INIT

wood_counter = Counter(save.wood, size=32)
wood_counter.setPos((10, 10))
wood_counter.color = (255, 255, 255)
wood_counter.set_prefix_text("Wood: ")

money_counter = Counter(save.money, size=32)
money_counter.setPos((500, 10))
money_counter.color = (255, 255, 255)
money_counter.set_prefix_text("Money: $")

buttons = []
b = Button((10, 50), (100, 100), True)
b.setImage(OAK_LOG_IMG)
b.setAction(lambda: wood_counter.increment(1))
b.setBgcolor((131, 163, 161))
b.setText("Chop wood!")
buttons.append(b)

money_btn = Button((500, 50), (100, 100), True)
money_btn.setImage(SMALL_COIN_IMG)
money_btn.setAction(lambda: money_counter.increment(wood_counter.empty()))
money_btn.setBgcolor((131, 163, 161))
money_btn.setText("Sell wood!")
buttons.append(money_btn)

save_btn = Button((300, 200), (60, 30), True)
save_btn.setBgcolor((131, 163, 161))
save_btn.setText("Save")
save_btn.setAction(lambda: save.save_to_file())
buttons.append(save_btn)

text = Text("TEST")
text.setPos((20, 40))
text.color = (0, 0, 0)

sprite = Sprite((100, 200), (100, 100), BASIC_AXE_IMG)

# GAME LOOP

while not paused:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                btn.clicked(pygame.mouse.get_pos())
            # print(pygame.mouse.get_pos())
        if event.type == EACH_SECOND:
            wood_counter.each_second()
            save.money = money_counter.value
            save.wood = wood_counter.value

    screen.fill(pygame.Color(124, 122, 122))
    # text.draw(screen)
    wood_counter.draw(screen)
    money_counter.draw(screen)
    sprite.draw(screen)
    for btn in buttons:
        btn.draw(screen)
    pygame.display.flip()
