from settings import *

class Sprite(pygame.sprite.Sprite):   #pygame.sprite.Sprite gives functionalities provided by Pygame's sprite system
    def __init__(self, pos, surf, groups):
        super().__init__(groups)  #This calls the constructor of the parent class (pygame.sprite.Sprite) # register this sprite in the provided groups,
        self.image = surf;  #self.image is visual representation of the sprite
        self.rect = self.image.get_frect(topleft = pos) #floating point rectangle