from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):  #init acts as a constructor
        super().__init__(groups)
        self.image = pygame.Surface((100, 100));
        self.image.fill('red');
        self.rect = self.image.get_frect(center = pos)

        self.direction = vector()

    #self allows you to encapsulate player-specific behaviors and data,
    #making the Player class reusable and adaptable for different game entities.

    def input(self): #I THINK SELF is for uniqueness for the player who will make instance of this Player class
        keys = pygame.key.get_pressed()
        input_vector = vector();
        if keys[pygame.K_UP]:
            input_vector.y -= 1
        if keys[pygame.K_DOWN]:
            input_vector.y += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        self.direction = input_vector;

    def move(self, dt):
        self.rect.center += self.direction * 250 * dt;

    def update(self, dt):
        self.input()
        self.move(dt)