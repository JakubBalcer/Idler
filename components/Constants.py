import configparser
import pygame

# LOAD CONFIG FROM FILE

config = configparser.ConfigParser()
config.read('config.ini')

width = int(config.get('window_settings', 'resolution_width'))
height = int(config.get('window_settings', 'resolution_height'))
save_name = config.get('game_settings', 'save_name')

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
