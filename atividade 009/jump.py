import pygame
pygame.init()

screen = pygame.display.set_mode((513, 401))
sprite_sheet_image = pygame.image.load('spritesheet.png').convert_alpha()
COLOR = (146, 144, 255)


class Spritesheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((2 * frame + frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image


sprite_sheet = Spritesheet(sprite_sheet_image)

animation = []
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

for x in range(animation_steps):
    animation.append(sprite_sheet.get_image(x, 16, 16, 5, COLOR))
animation.append(sprite_sheet.get_image(4, 16, 16, 5, COLOR))
animation.append(sprite_sheet.get_image(4, 16, 16, 5, COLOR))
animation.append(sprite_sheet.get_image(4, 16, 16, 5, COLOR))
animation.append(sprite_sheet.get_image(4, 16, 16, 5, COLOR))

loop = True

while loop:

    screen.fill((50, 40, 30))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame > 7:
            frame = 0
    if frame < 4:
        screen.blit(animation[frame], (200, 150))
    else:
        if frame == 4:
            screen.blit(animation[frame], (225, 125))
        elif frame == 5:
            screen.blit(animation[frame], (250, 100))
        elif frame == 6:
            screen.blit(animation[frame], (275, 125))
        else:
            screen.blit(animation[frame], (300, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    pygame.display.update()
