from random import randint
import pygame,sys,time 
from settings import *
from player import Player
from Tree import tree 
from cameragroup import CameraGroup

class Game:
    
    def __init__(self):
        
        pygame.init()
        
        self.display_surf = pygame.display.set_mode((WINDOW_WITHD,WINDOW_HEIGHT))
        pygame.display.set_caption("Cameras")
        pygame.event.set_grab(True)
        
        self.clock = pygame.time.Clock()

        self.camera_group = CameraGroup()
        self.player = Player(self.camera_group)
        
        for i in range(20):
            x = randint(1000,2000)
            y = randint(1000,2000)
            tree(self.camera_group,(x,y))
        
    def run(self):
        last_time = time.time()
        
        while True:
            dt = time.time() - last_time
            last_time = time.time()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.MOUSEWHEEL:
                    self.camera_group.zoom_scale += event.y * 0.03
            
            self.display_surf.fill("#71ddee")
            
            self.camera_group.update(dt)
            self.camera_group.custom_draw(self.player,dt)
            
            
            pygame.display.update()
            self.clock.tick(600)