import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, src_rect, num_frames):
        super().__init__()
        self.spritesheet = pygame.image.load(image_path)
        self.src_rect = pygame.Rect(src_rect)
        self.image = self.spritesheet.subsurface(self.src_rect)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Animation variables
        self.frame = 0
        self.num_frames = num_frames
        self.frame_width = self.src_rect.width // num_frames

    def update(self):
        # Handle player movement
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 1
        elif key[pygame.K_d]:
            self.rect.x += 1
        elif key[pygame.K_w]:
            self.rect.y -= 1
        elif key[pygame.K_s]:
            self.rect.y += 1

        # Update animation frame
        self.frame = (self.frame + 1) % self.num_frames
        self.src_rect.x = self.frame * self.frame_width
        self.image = self.spritesheet.subsurface(self.src_rect)

# Specify the path to the player image, the source rectangle, and the number of frames
player_image_path = "vita.png"
player_src_rect = (0, 0, 24, 24)  # Adjust these values based on your spritesheet layout
num_frames = 24  # Adjust based on the number of frames in your spritesheet

# Create an instance of the player with the image
player = Player(300, 250, player_image_path, player_src_rect, num_frames)

# Create a sprite group and add the player to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Initialize the game loop
run = True
while run:
    screen.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update and draw all sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Refresh the screen
    pygame.display.update()

pygame.quit()
