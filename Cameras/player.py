import pygame

from settings import WINDOW_HEIGHT, WINDOW_WITHD 

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("Cameras/graphics/player.png")
        self.rect = self.image.get_rect(center=(WINDOW_WITHD/2,WINDOW_HEIGHT/2))
        
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 500
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1 
        else:
            self.direction.y = 0 
            
        if keys[pygame.K_d]:
            self.direction.x = 1 
        elif keys[pygame.K_a]:
            self.direction.x = -1 
        else:
            self.direction.x = 0 
            
    def update(self,dt):
        self.input()
        
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
                
        self.pos.x += self.direction.x * self.speed * dt 
        self.rect.x = round(self.pos.x) 
        
        self.pos.y += self.direction.y * self.speed * dt 
        self.rect.y = round(self.pos.y)
        
        
        
        
        