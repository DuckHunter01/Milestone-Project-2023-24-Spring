import pygame

win_width = 1000
win_height = 600
win = pygame.display.set_mode((win_width, win_height))

running = True
clock = pygame.time.Clock()

while running:
    for ev in pygame.event.get():
        match ev.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
    
    time = clock.get_time()
    pygame.display.update()
    clock.tick(60)

pygame.quit()