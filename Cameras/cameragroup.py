import pygame,sys
from debug import debug 

class CameraGroup(pygame.sprite.Group):
    
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        self.ground_surf = pygame.image.load("Cameras/graphics/ground.png").convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0,0))
        
        #camera offset
        self.offset = pygame.math.Vector2(0 ,0)
        self.screen_half_w = self.display_surf.get_size()[0] // 2 
        self.screen_half_h = self.display_surf.get_size()[1] // 2
    
        #box camera setup
        self.camera_borders = {"left":200,"right":200,"top":100,"bottom":100} 
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surf.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surf.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        
        self.camera_rect = pygame.Rect(l,t,w,h)
        
        self.speed = 300
        self.mouse_speed = 0.4
        self.zoom_scale = 1
        
        self.internal_surf_size = (2500,2500)
        self.internal_surf = pygame.Surface(self.internal_surf_size,pygame.SRCALPHA)
        
        self.internal_rect = self.internal_surf.get_rect(center = (self.screen_half_w,self.screen_half_h))
        self.internal_surf_size_vector = pygame.math.Vector2(self.internal_surf_size)
        
        self.internal_offset = pygame.math.Vector2()
        
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.screen_half_w 
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.screen_half_h 
    
    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.screen_w 
        self.offset.y = target.rect.centery - self.screen_h 
    
    def box_camera(self,target):
        
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right 
        
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top 
            
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom
            
        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.y  - self.camera_borders['top']
        
        
    def zoom_keyboard_control(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_q]:
            self.zoom_scale +=0.1    
        if keys[pygame.K_e]:
            self.zoom_scale -=0.1 
        
    def keyword_key_camera(self,dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.camera_rect.y -= round(self.speed * dt)
        if keys[pygame.K_DOWN]:
            self.camera_rect.y += round(self.speed * dt)
        
        if keys[pygame.K_RIGHT]:
            self.camera_rect.x += round(self.speed * dt)
        if keys[pygame.K_LEFT]:
            self.camera_rect.x -= round(self.speed * dt)
        
       
        
    def mouse_camera(self):
        
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_offset_vector = pygame.math.Vector2()
        
        left_border = self.camera_borders['left']
        top_border = self.camera_borders['top']
        right_border = self.display_surf.get_size()[0] - self.camera_borders['right']
        bottom_border = self.display_surf.get_size()[1] - self.camera_borders['bottom']
        
        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
                pygame.mouse.set_pos((left_border,mouse.y))

            if mouse.x> right_border:
                mouse_offset_vector.x = mouse.x - right_border
                pygame.mouse.set_pos((right_border,mouse.y))
                
        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                mouse_offset_vector.y = mouse.y - top_border
                pygame.mouse.set_pos((mouse.x,top_border))
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                pygame.mouse.set_pos((mouse.x,bottom_border))
        
        if left_border> mouse.x and top_border > mouse.y:
            mouse_offset_vector.x = mouse.x - left_border
            mouse_offset_vector.y = mouse.y - top_border
            pygame.mouse.set_pos((left_border,top_border))
        
        if right_border < mouse.x and top_border > mouse.y:
            mouse_offset_vector.x = mouse.x - right_border
            mouse_offset_vector.y = mouse.y - top_border
            pygame.mouse.set_pos((right_border,top_border))
            
        if left_border > mouse.x and bottom_border < mouse.y:
            mouse_offset_vector.x = mouse.x - left_border
            mouse_offset_vector.y = mouse.y - bottom_border
            pygame.mouse.set_pos((left_border,bottom_border))
        
        if right_border < mouse.x and bottom_border < mouse.y:
            mouse_offset_vector.x = mouse.x - right_border
            mouse_offset_vector.y = mouse.y - bottom_border
            pygame.mouse.set_pos((right_border,bottom_border))
        
        self.offset += mouse_offset_vector * self.mouse_speed
        debug(self.offset)
    
    def custom_draw(self,player,dt):
        #self.center_target_camera(player)
        
        self.box_camera(player)
        
        #self.keyword_key_camera(dt)
        
        #self.mouse_camera()
        
        self.internal_surf.fill("#71ddee")
        
        offset_pos = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.ground_surf,offset_pos)
        
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            
            self.internal_surf.blit(sprite.image,offset_pos)
        
        
         
        scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surf_size_vector*self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=(self.screen_half_w,self.screen_half_h))
        
        self.display_surf.blit(scaled_surf,scaled_rect)
        
      