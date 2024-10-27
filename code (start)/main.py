from settings import *   # Importing everything from the settings file
from pytmx.util_pygame import load_pygame  #used to import tmx files[tiled] into pygame
from os.path import join
from sprites import Sprite
# Creating a basic game class
class Game:
    # General 
    def __init__(self):
        pygame.init()
        #instance variable display_surface
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Hunter')

        #groups
        self.all_sprites = pygame.sprite.Group()

        self.import_assets();
        self.setup(self.tmx_maps['world'], 'house')


    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('..', 'data', 'maps', 'world.tmx'))} 
        

    def setup(self, tmx_map, player_start_pos):
        for x,y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x*TILE_SIZE ,y*TILE_SIZE), surf, self.all_sprites);

    #run method starts an infinite loop so the game keeps running
    def run(self):
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #Game Logic
            self.all_sprites.draw(self.display_surface);
            pygame.display.update();

#common python construct - A very good defining entry point of your program.
if __name__ == '__main__':
    game = Game()
    game.run()
