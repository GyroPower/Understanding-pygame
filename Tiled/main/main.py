import pygame,sys 
from settings import * 
from level import Level
from game_data import level_0

class Game:
    
    def __init__(self):
        pygame.init()
        
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGT))
        pygame.display.set_caption("Mario level clone python")
        self.clock = pygame.time.Clock()
        self.level = Level(level_data=level_0)
        
        
    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.display_surf.fill("grey")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FRAME_RATE)
            

if __name__ == "__main__":
    game = Game()
    game.run()