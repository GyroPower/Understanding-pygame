import pygame, sys, time 
from objects.Objects import (
    StaticObstacle,
    MovingVerticalObstacle,
    MovingHorizontalObstacle,
    Ball,
    Player
)
from Masks.debug import debug


pygame.init()

screen = pygame.display.set_mode((1280,720))

all_prites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

StaticObstacle((100,300),(100,50),[all_prites,collision_sprites])
StaticObstacle((800,600),(100,200),[all_prites,collision_sprites])
StaticObstacle((900,200),(200,10),[all_prites,collision_sprites])
MovingVerticalObstacle((200,300),(200,60),[all_prites,collision_sprites])
MovingHorizontalObstacle((850,350),(100,100),[all_prites,collision_sprites])
player = Player(all_prites,collision_sprites)
Ball(all_prites,collision_sprites,player)

last_time = time.time()

while True:
    
    dt = time.time() - last_time
    last_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill("black")
    debug(player.pos)
    
    all_prites.update(dt)
    all_prites.draw(screen)
    
    pygame.display.update()

