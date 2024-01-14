import pygame
import spritesheet_class
pygame.init()

screen = pygame.display.set_mode((513, 401))
sprite_sheet_image = pygame.image.load('spritesheet.png').convert_alpha()
COLOR = (146, 144, 255)


sprite_sheet = spritesheet_class.Spritesheet(sprite_sheet_image)

animation_master = []
animations = [3, 2]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0
counter = 0

for x in animations:
    temp_list = []
    for _ in range(x):
        temp_list.append(sprite_sheet.get_image(counter, 16, 16, 5, COLOR))
        counter += 1
    animation_master.append(temp_list)

loop = True
while loop:

    screen.fill((50, 40, 30))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_master[action]):
            frame = 0

    screen.blit(animation_master[action][frame], (200, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                action = 1
                frame = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                action = 0
                frame = 0

    pygame.display.update()
