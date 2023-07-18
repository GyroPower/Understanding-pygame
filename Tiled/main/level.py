import pygame 
from support import import_csv_layout,import_cut_graphics
from settings import *
from Tiles import Tile,StaticTile,Crate,Coin,Palm,BG_Palm
from enemy import Enemy
from decoration import Sky,Water,Cloud

class Level:
    
    def __init__(self,level_data):
        
        #displaY_surf
        self.display_surf = pygame.display.get_surface() 
        self.world_shift = 0
        

        #player setup 
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)
        
        
       #terrain_sprite layout
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprite = self.create_tiled_group(terrain_layout,"terrain")
        
        #grass_sprte layout 
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprite = self.create_tiled_group(grass_layout,"grass")
        
        # crates
        crate_layout = import_csv_layout(level_data['crates'])
        self.crates_sprites = self.create_tiled_group(crate_layout,"crate")

        #coins 
        coins_layout = import_csv_layout(level_data['coins'])
        self.coins_sprites = self.create_tiled_group(coins_layout,"coin")
        
        # fg_palms
        fg_palms = import_csv_layout(level_data['fg_palms'])
        self.fg_palms = self.create_tiled_group(fg_palms,"fg_palm")

        #bg palms
        bg_palms = import_csv_layout(level_data['bg_palms'])
        self.bg_palms = self.create_tiled_group(bg_palms,"bg_palm")
     
        #Enemies 
        enemies_layout = import_csv_layout(level_data['enemies'])
        self.enemies = self.create_tiled_group(enemies_layout,'enemies') 
        
        #Constrains
        constrains_layout = import_csv_layout(level_data['constrains'])
        self.constrains = self.create_tiled_group(constrains_layout,"constrain")

        #decoration
        self.sky = Sky(8)
        level_width = len(terrain_layout[0]) * tile_size
        self.water = Water(WINDOW_HEIGT - 40,level_width)
        self.clouds = Cloud(level_width,6,20)
     
     
    def run(self):
       
       self.sky.draw() 
       self.water.draw(self.world_shift)
       self.clouds.draw(self.world_shift)
       self.bg_palms.update(self.world_shift)
       self.bg_palms.draw(self.display_surf)
       
       self.fg_palms.update(self.world_shift)
       self.fg_palms.draw(self.display_surf)
       
       self.terrain_sprite.update(self.world_shift)
       self.terrain_sprite.draw(self.display_surf)
       
       self.enemies.update(self.world_shift)
       self.constrains.update(self.world_shift)
       self.enemies.draw(self.display_surf)
       
       self.crates_sprites.update(self.world_shift)
       self.crates_sprites.draw(self.display_surf)
       
       self.grass_sprite.update(self.world_shift)
       self.grass_sprite.draw(self.display_surf)
       
       self.coins_sprites.update(self.world_shift)
       self.coins_sprites.draw(self.display_surf)
       
       self.goal.update(self.world_shift)
       self.goal.draw(self.display_surf)
       
       self.enemy_col_reverse()
       
       self.move_overworld()   
        
    def create_tiled_group(self,layaout,type):
        
        sprite_group = pygame.sprite.Group()
        
        for row_index,row in enumerate(layaout):
            for col_index, col in enumerate(row):
                
                if col != "-1":
                    x = col_index * tile_size 
                    y = row_index * tile_size
                
                    if type == "terrain":
                        terrain_tiles_list = import_cut_graphics("Tiled/graphics/level/terrain_tiles.png")
                        tile_surf = terrain_tiles_list[int(col)]
                        sprite = StaticTile(tile_surf,tile_size,x,y)
                        
                    if type == "grass":
                        grass_tiles_list = import_cut_graphics("Tiled/graphics/decoration/grass/grass.png")
                        tile_surf = grass_tiles_list[int(col)]
                        sprite = StaticTile(tile_surf,tile_size,x,y)
                    
                    if type == "crate":
                        
                        sprite = Crate(tile_size,x,y)
                    
                    if type == "coin":
                        if col == "0": sprite = Coin(tile_size,x,y,"Tiled/graphics/coins/gold")
                        if col == "1": sprite = Coin(tile_size,x,y,"Tiled/graphics/coins/silver")
                    
                    if type == "fg_palm":
                        if col == "0": sprite = Palm(tile_size,x,y,"Tiled/graphics/level/palm_small")
                        if col == "1": sprite = Palm(tile_size,x,y,"Tiled/graphics/level/palm_large")
                    
                    if type == "bg_palm":
                        sprite = BG_Palm(tile_size,x,y,"Tiled/graphics/level/palm_bg")
                    
                    if type == "enemies":
                        sprite = Enemy(tile_size,x,y)
                    
                    if type == "constrain":
                        sprite = Tile(tile_size,x,y)
                    
                    sprite_group.add(sprite)
          
                    
        return sprite_group
    
    
    def player_setup(self,player_layaout):
        for row_index,row in enumerate(player_layaout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size 
                y = row_index * tile_size
                
                if col == "0":
                    print("player goes here")
                if col == "1":
                    hat_surf = pygame.image.load("Tiled/graphics/character/hat.png")
                    sprite = StaticTile(hat_surf,tile_size,x,y)
                    
                    self.goal.add(sprite)
                    
                    

                
    
    def move_overworld(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.world_shift = 5 
        elif keys[pygame.K_RIGHT]:
            self.world_shift = -5 
        else:
            self.world_shift = 0 
    
    def enemy_col_reverse(self):
        
        for enemy in self.enemies.sprites():
            if pygame.sprite.spritecollide(enemy,self.constrains,False):
                enemy.reverse()
    
    
       