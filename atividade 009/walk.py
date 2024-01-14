import pygame
import spritesheet_class

pygame.init()

screen = pygame.display.set_mode((513, 401))
sprite_sheet_image = pygame.image.load('spritesheet.png').convert_alpha()
COLOR = (146, 144, 255)

sprite_sheet = spritesheet_class.Spritesheet(sprite_sheet_image)

animation = []
animation_steps = 3
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0

for x in range(animation_steps):
    animation.append(sprite_sheet.get_image(x, 16, 16, 5, COLOR))

loop = True

while loop:

    screen.fill((50, 40, 30))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame == animation_steps:
            frame = 0

    screen.blit(animation[frame], (200, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    pygame.display.update()
