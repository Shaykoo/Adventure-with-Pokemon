from settings import *

class AllSprites(pygame.sprite.Group): #AllSprites is extending the class pygame.sprite.Group 
    def __init__(self):
        super().__init__() #initilize the parent class which is Group
        self.display_surface = pygame.display.get_surface();
        self.offset = vector();

    def draw(self, player_center):
        self.offset.x = -(player_center[0] - WINDOW_WIDTH/2);
        self.offset.y = -(player_center[1] - WINDOW_HEIGHT/2);

        for sprite in self:  # self here refers to the AllSprites group
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)  #blit() is a method that copies an image (in this case, sprite.image) onto another surface (self.display_surface), which is the game screen.