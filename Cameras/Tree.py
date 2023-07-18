import pygame,sys 
from random import randint


class tree(pygame.sprite.Sprite):
    
    def __init__(self,groups,coordenades):
        super().__init__(groups)
        
        self.image = pygame.image.load("Cameras/graphics/tree.png").convert_alpha()
        self.rect = self.image.get_rect(center=coordenades)