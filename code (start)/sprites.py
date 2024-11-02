from settings import *

class Sprite(pygame.sprite.Sprite):   #pygame.sprite.Sprite gives functionalities provided by Pygame's sprite system
    def __init__(self, pos, surf, groups, z = WORLD_LAYERS['main']):
        super().__init__(groups)  #This calls the constructor of the parent class (pygame.sprite.Sprite) # register this sprite in the provided groups,
        self.image = surf;  #self.image is visual representation of the sprite
        self.rect = self.image.get_frect(topleft = pos) #floating point rectangle
        self.z = z;
        self.y_sort = self.rect.centery;
        self.hitbox = self.rect.copy();

class BorderSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups) #No world layer because this border sprtes will not be visible in the UI
        self.hitbox = self.rect.inflate(0, -self.rect.height * 0.6);

class CollidableSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups) #No world layer because this border sprtes will not be visible in the UI
        self.hitbox = self.rect.copy();

class MonsterPatchSprite(Sprite):   #pygame.sprite.Sprite gives functionalities provided by Pygame's sprite system
    def __init__(self, pos, surf, groups, biome):
        self.biome = biome;
        super().__init__(pos, surf, groups, WORLD_LAYERS['main' if biome != 'sand' else 'bg'])
        self.y_sort -= 40;

class AnimatedSprite(Sprite): #Sprite is the parent for this AnimatedSprite
    def __init__(self, pos, frames, groups, z):
        self.frame_index, self.frames = 0, frames;
        super().__init__(pos, frames[self.frame_index], groups, z)

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt;
        self.image = self.frames[int(self.frame_index % len(self.frames))]

    def update(self, dt):
        self.animate(dt)



