from settings import *   # Importing everything from the settings file
from pytmx.util_pygame import load_pygame  #used to import tmx files[tiled] into pygame
from os.path import join
# Creating a basic game class
class Game:
    # General 
    def __init__(self):
        pygame.init()
        #instance variable display_surface
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Hunter')

        self.import_assets();
        self.setup(self.tmx_maps['world'], 'house')


    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('..', 'data', 'maps', 'world.tmx'))} 
        

    def setup(self, tmx_map, player_start_pos):
        for x,y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            print(x*TILE_SIZE ,y*TILE_SIZE, surf);

    #run method starts an infinite loop so the game keeps running
    def run(self):
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #Game Logic
            pygame.display.update();

#common python construct - A very good defining entry point of your program.
if __name__ == '__main__':
    game = Game()
    game.run()
