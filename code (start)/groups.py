from settings import *
from support import import_image
from entities import Entity

class AllSprites(pygame.sprite.Group): #AllSprites is extending the class pygame.sprite.Group 
    def __init__(self):
        super().__init__() #initilize the parent class which is Group
        self.display_surface = pygame.display.get_surface();
        self.offset = vector();
        self.shadow_surf = import_image('..', 'graphics', 'other', 'shadow')

    def draw(self, player_center):
        self.offset.x = -(player_center[0] - WINDOW_WIDTH/2);
        self.offset.y = -(player_center[1] - WINDOW_HEIGHT/2);

        #Here, self refers to the instance of AllSprites, which is a custom class
        #derived from pygame.sprite.Group. This group contains all the sprites in
        #the game, so iterating over self is equivalent to iterating over 
        #each sprite currently in AllSprites.
        bg_sprites = [sprite for sprite in self if sprite.z < WORLD_LAYERS['main']];
        main_sprites = sorted([sprite for sprite in self if sprite.z == WORLD_LAYERS['main']], key = lambda sprite: sprite.y_sort) #lambda function named sprite
        fg_sprites = [sprite for sprite in self if sprite.z > WORLD_LAYERS['main']];

        #Drawing the groups in order
        for layer in (bg_sprites, main_sprites, fg_sprites):
            for sprite in layer:  # self here refers to the AllSprites group
                if isinstance(sprite, Entity):
                    self.display_surface.blit(self.shadow_surf, sprite.rect.topleft + self.offset + vector(40, 110))
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)  #blit() is a method that copies an image (in this case, sprite.image) onto another surface (self.display_surface), which is the game screen.