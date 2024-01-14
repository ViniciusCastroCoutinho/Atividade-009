import pygame
import spritesheet_class
pygame.init()

screen = pygame.display.set_mode((513, 401))
sprite_sheet_image = pygame.image.load('esse aqui3.png').convert_alpha()
COLOR = (0, 0, 0)


sprite_sheet = spritesheet_class.Spritesheet(sprite_sheet_image)

animation_master = []
animations = [6, 6, 6, 6]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
counter = 0

for x in animations:
    temp_list = []
    for _ in range(x):
        temp_list.append(sprite_sheet.get_image(counter, 137, 137, 1, COLOR))
        counter += 1
    animation_master.append(temp_list)

loop = True
while loop:
    screen.fill((0, 0, 0))

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
            if event.key == pygame.K_DOWN:
                action = 0
                frame = 0
            elif event.key == pygame.K_LEFT:
                action = 1
                frame = 0
            elif event.key == pygame.K_RIGHT:
                action = 2
                frame = 0
            elif event.key == pygame.K_UP:
                action = 3
                frame = 0

    pygame.display.update()
