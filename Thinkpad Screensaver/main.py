import pygame
from sys import exit

# Textures

thinkpad_logo = pygame.image.load('textures/Thinkpad-Logo.jpg')

WIDTH, HEIGHT = 1280, 720
# Pygame Setup
pygame.init()
image_rect = thinkpad_logo.get_rect()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Screensaver")

clock = pygame.time.Clock()
running = True

image_rect.x, image_rect.y = 100, 100
velocity_x, velocity_y = 5, 5

thinkpad_logo_pos_x = 210

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    image_rect.x += velocity_x
    image_rect.y += velocity_y

    if image_rect.left < 0 or image_rect.right > WIDTH:
        velocity_x = -velocity_x
    if image_rect.top < 0 or image_rect.bottom > HEIGHT:
        velocity_y = -velocity_y

    screen.fill('black')
    Fira_Code_font = pygame.font.Font(None, 45)
    screen.blit(thinkpad_logo, image_rect)

    # Welcome text screen
     # welcome_text = Fira_Code_font.render('Welcome!', False, 'black')
     # screen.blit(welcome_text, (welcome_text_pos_x, 230))

    pygame.display.update()

    clock.tick(60)