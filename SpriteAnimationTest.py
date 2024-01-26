import pygame
import spritehelper
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')
sprite_sheet_image = pygame.image.load('vita.png').convert_alpha()
sprite_sheet = spritehelper.SpriteSheet(sprite_sheet_image)
BG = (50,50,50)
BLACK = (0,0,0)

#create animation list
animation_list = [] #master animation list
animation_steps = [4, 6, 4, 3, 7] #how many frames are in each action (ie, 4 frames of idle, 6 frames of running)
action = 2
last_update = pygame.time.get_ticks()
animation_cooldown = 250 #how fast the frames will change
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:
    screen.fill(BG)
    #show frame image
    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
    #show frame image
    screen.blit(animation_list[action][frame], (0,0)) #72 is the scaled number (24 pixels * scale factor of 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0
    pygame.display.update()
pygame.quit()