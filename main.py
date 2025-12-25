import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    dt = 0 
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    log_state()
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        dt = pygame.time.Clock().tick(60) / 1000

if __name__ == "__main__":

    main()