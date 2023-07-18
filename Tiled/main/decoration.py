import pygame 
from settings import vertical_tile_number,tile_size,WINDOW_WIDTH,WINDOW_HEIGT
from Tiles import AnimatedTile,StaticTile
from support import import_folder
from random import randint,choice

class Sky:
    
    def __init__(self,horizon):
        self.top = pygame.image.load("Tiled/graphics/decoration/sky/sky_top.png").convert()
        self.bottom = pygame.image.load("Tiled/graphics/decoration/sky/sky_bottom.png").convert()
        self.middle = pygame.image.load("Tiled/graphics/decoration/sky/sky_middle.png").convert()
        
        self.horizon = horizon 
        
        self.top = pygame.transform.scale(self.top,(WINDOW_WIDTH,tile_size))
        self.bottom = pygame.transform.scale(self.bottom,(WINDOW_WIDTH,tile_size))
        self.middle = pygame.transform.scale(self.middle,(WINDOW_WIDTH,tile_size))
        
        
    def draw(self):
        surf = pygame.display.get_surface()
        
        for row in range(vertical_tile_number):
            y = row * tile_size
            
            if row == self.horizon:
                surf.blit(self.middle,(0,y))   
                 
            elif row > self.horizon:
                surf.blit(self.bottom,(0,y))
            
            else:
                surf.blit(self.top,(0,y))

class Water:
    
    def __init__(self,top,level_width):
        
        water_start = -WINDOW_WIDTH
        water_tile_width = 192 
        tile_x_amount = int((WINDOW_WIDTH+level_width)/water_tile_width)
        self.water_sprites = pygame.sprite.Group()
        
        for tile in range(tile_x_amount):
                
            x = tile * water_tile_width + water_start
            
            y = top 
            
            sprite = AnimatedTile(192,x,y,"Tiled/graphics/decoration/water")
            self.water_sprites.add(sprite)
            
            
    def draw(self,shift):
        surf = pygame.display.get_surface()
        
        
        self.water_sprites.update(shift)
        self.water_sprites.draw(surf)
        
        
class Cloud:
    
    def __init__(self,level_width,horizon,cloud_number):
        
        clouds_surf_list = import_folder("Tiled/graphics/decoration/clouds")
        min_x = -WINDOW_WIDTH
        max_x = level_width + WINDOW_WIDTH
        
        min_y = 0
        max_y = horizon * tile_size 
        
        self.clouds_sprite = pygame.sprite.Group()
        
        for cloud in range(cloud_number):
            
            cloud = choice(clouds_surf_list)
            x = randint(min_x,max_x)
            y = randint(min_y,max_y)
            
            sprite = StaticTile(cloud,0,x,y)
            self.clouds_sprite.add(sprite)
            
    def draw(self,shift):
        surf = pygame.display.get_surface()
        
        self.clouds_sprite.update(shift)
        self.clouds_sprite.draw(surf)
                