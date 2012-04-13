import pygame
from pygame.locals import *

class Batman(object):
    x = 0 
    y = 0

    def __init__(self, screen):
        self.sprite_batman  = pygame.image.load("Batman.png").convert_alpha()
        self.screen = screen

    def draw(self):
        self.x = self.x + 1

        if self.x > 800:
            self.x = 0
        self.screen.blit(self.sprite_batman,(self.x,100))


class App(object):
    x = 0
    y = 0
    def __init__(self):
        self._running = True
        self.screen = None
        self._image_surf = None
 
    def on_init(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,600), pygame.HWSURFACE)
        self._running = True
        self.batman = Batman(self.screen)
        self._image_surf_background = pygame.image.load("widescreen_small.jpg").convert()

 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass
        
    def on_render(self):
        self.screen.blit(self._image_surf_background,(0,0))
        self.batman.draw()

        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()

 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        #game loop here
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()



 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
