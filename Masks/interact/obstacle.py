from typing import Any
import pygame 


class a(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Masks/graphics/alpha.png").convert_alpha()
        self.rect = self.image.get_rect(center = (680,360))
        self.mask = pygame.mask.from_surface(self.image)
          
            
    def update(self,surf):
        self.outline(surf)
        