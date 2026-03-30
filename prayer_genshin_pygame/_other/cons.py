import pygame

pygame.init()
wid = 1600
hei = 1000
fps = 60
my_font = pygame.font.Font("_other/fonts/BitcountGridSingle_Cursive-Black.ttf", 30)
active_color = "white"
was_clicked = False
effect_button = print
scr = pygame.display.set_mode((wid, hei))