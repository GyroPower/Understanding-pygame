import pygame 
from debug import debug

class Player(pygame.sprite.Sprite):
    def __init__(self,obs):
        super().__init__()
    
        self.image = pygame.image.load("Masks/graphics/ship.png")
        
        self.rect = self.image.get_rect(center = (680,360))
        self.obstacle = obs 
        self.mask = pygame.mask.from_surface(self.image)
        
        
    def input(self):
        mouse = pygame.mouse.get_pos()
        self.rect.x,self.rect.y = mouse
        
        
    
    def collision(self,direction=""):
        offset_x = self.obstacle.sprite.rect.x - self.rect.left 
        offset_y = self.obstacle.sprite.rect.y - self.rect.top 
        surf = pygame.display.get_surface()
        surf.blit(self.image,self.rect)
        
        if self.mask.overlap(self.obstacle.sprite.mask,(offset_x,offset_y)):
            self.new_mask = self.mask.overlap_mask(self.obstacle.sprite.mask,(offset_x,offset_y))    
            
            self.new_image = self.new_mask.to_surface()
            self.new_image.set_colorkey((0,0,0))
           
            
            x_size,y_size = self.new_image.get_size()

            for x in range(x_size):
                for y in range(y_size):
            
                    if self.new_image.get_at((x,y))[0] != 0:
                        self.new_image.set_at((x,y),"red")
            
            surf.blit(self.new_image,self.rect)
            
    def update(self):
        
        
        self.input()
        self.collision()
        
        
        
        