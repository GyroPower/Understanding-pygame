import pygame 
from support import import_folder

class Tile(pygame.sprite.Sprite):
    
    def __init__(self,size,x,y):
        super().__init__()
        
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft=(x,y))
        
    def update(self,shift):
        self.rect.x += shift 
        
        
class StaticTile(Tile):
    
    def __init__(self,surface,size,x,y):
        super().__init__(size,x,y)
        
        self.image = surface  


class Crate(StaticTile):
    
    def __init__(self,size,x,y):
        super().__init__(pygame.image.load("Tiled/graphics/level/crate.png").convert_alpha(),size,x,y)
        offset = y + size 
        x = x + (size/2)
        self.rect = self.image.get_rect(midbottom=(x,offset))
        
        
class AnimatedTile(Tile):
    
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y)
        
        self.frames = import_folder(path)
        
        
        self.frame_index = 0 
        self.image = self.frames[self.frame_index]
        
    def animate(self):
        self.frame_index += 0.15 
        
        if self.frame_index >= len(self.frames): self.frame_index = 0
        
        self.image = self.frames[int(self.frame_index)]
        
    def update(self,shift):
        self.rect.x += shift 
        
        self.animate()
        

class Coin(AnimatedTile):
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y,path)
        
        x = x +(size/2)
        y = y +(size/2)
        
        self.rect = self.image.get_rect(center=(x,y))
                
class Palm(AnimatedTile):
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y,path)
        
        x = x +(size/2)
        y = y + size + 12
        
        self.rect = self.image.get_rect(midbottom=(x,y))
        

class BG_Palm(AnimatedTile):
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y,path)
       
        y = y + size + 10
        
        self.rect = self.image.get_rect(bottomleft=(x,y))
        


        
        