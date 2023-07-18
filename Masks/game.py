import pygame,sys,time 
from interact.player import Player
from interact.obstacle import a 

class Game:
    def __init__(self):
        pygame.init()
        
        self.display_surf = pygame.display.set_mode((1280,720))
        
        pygame.display.set_caption("Masks")
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        
        self.obstacle = pygame.sprite.GroupSingle(a())
        self.player = pygame.sprite.GroupSingle(Player(self.obstacle))
        
        
    def run(self):
        last_time = time.time()
        
        while True:
            dt = time.time() - last_time
            last_time = time.time()
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.display_surf.fill("grey")
            
            
            
            self.obstacle.draw(self.display_surf)
            # self.player.draw(self.display_surf)
            
            self.player.update()
            
            
            pygame.display.update()
            self.clock.tick(600)