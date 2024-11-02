from settings import *   # Importing everything from the settings file
from pytmx.util_pygame import load_pygame  #used to import tmx files[tiled] into pygame
from os.path import join
from sprites import Sprite, AnimatedSprite, MonsterPatchSprite, BorderSprite, CollidableSprite
from entities import Player, Character
from groups import AllSprites
from support import *
# Creating a basic game class
class Game:
    # General 
    def __init__(self):
        pygame.init()
        #instance variable display_surface
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Hunter')
        self.clock = pygame.time.Clock()
        #groups
        # self.all_sprites = pygame.sprite.Group()
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.import_assets();
        self.setup(self.tmx_maps['world'], 'house')


    def import_assets(self):
        self.tmx_maps = {
            'world': load_pygame(join('..', 'data', 'maps', 'world.tmx')),
            'hospital': load_pygame(join('..', 'data', 'maps', 'hospital.tmx'))} 
        
        self.overworld_frames = {
            'water': import_folder('..', 'graphics', 'tilesets', 'water'),
            'coast': coast_importer(24, 12, '..', 'graphics', 'tilesets', 'coast'),
            'characters': all_character_import('..', 'graphics', 'characters')
        }
        

    def setup(self, tmx_map, player_start_pos):
        #Terrain Tiles
        for layer in ['Terrain','Terrain Top']:
            for x,y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x*TILE_SIZE ,y*TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg']);
        
        #Water tiles
        for obj in tmx_map.get_layer_by_name('Water'):
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    AnimatedSprite((x,y), self.overworld_frames['water'], self.all_sprites, WORLD_LAYERS['water'])

        #Coast tiles
        for obj in tmx_map.get_layer_by_name('Coast'):
            terrain = obj.properties['terrain'];
            side = obj.properties['side'];
            AnimatedSprite((obj.x, obj.y), self.overworld_frames['coast'][terrain][side], self.all_sprites,  WORLD_LAYERS['bg'])
        
        #Objects tiles
        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'top':
                Sprite((obj.x, obj.y), obj.image, self.all_sprites, WORLD_LAYERS['top'])
            else:
                CollidableSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        #Grass patches
        for obj in tmx_map.get_layer_by_name('Monsters'):
            MonsterPatchSprite((obj.x, obj.y), obj.image, self.all_sprites, obj.properties['biome'])
    
        #In tiled map of entities we have player and charatcter in the tiled version #Entities Tiles
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['pos'] == player_start_pos:
                    #This new Player object is added to self.all_sprites, a group containing all sprites, allowing it to be managed and drawn by the game engine.
                    self.player = Player(
                        pos = (obj.x, obj.y),
                        frames = self.overworld_frames['characters']['player'], 
                        groups = self.all_sprites,
                        facing_direction = obj.properties['direction'],
                        collision_sprites = self.collision_sprites) #creating instance of the player
            else:
                Character(
                    pos = (obj.x, obj.y),
                    frames = self.overworld_frames['characters'][obj.properties['graphic']], 
                    groups = (self.all_sprites, self.collision_sprites),
                    facing_direction = obj.properties['direction'])
                

        # Collision Objects
        for obj in tmx_map.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)


    #run method starts an infinite loop so the game keeps running
    def run(self):
        while True:
            dt = self.clock.tick(60)/1000; #gives the frame rate, currently it's 60fps
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #Game Logic
            #calling self.all_sprites.update() in the Game class will indeed trigger
            #the update method defined in the Player class (from entities.py), as well
            #as any other update method for other sprites within the all_sprites group.
            self.all_sprites.update(dt);
            self.display_surface.fill('black');
            self.all_sprites.draw(self.player.rect.center);
            pygame.display.update();

#common python construct - A very good defining entry point of your program.
if __name__ == '__main__':
    game = Game()
    game.run()
