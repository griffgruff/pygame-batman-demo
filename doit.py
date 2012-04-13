import pygame
from pygame.locals import *

class App:
    x = 0
    y = 0
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((800,600), pygame.HWSURFACE)
        self._running = True
        self._image_surf_background = pygame.image.load("widescreen_small.jpg").convert()
        self._image_surf = pygame.image.load("Batman.png").convert_alpha()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass
        
    def on_render(self):

        self._display_surf.blit(self._image_surf_background,(0,0))

        self._display_surf.blit(self._image_surf,(self.x,self.y))
        self._display_surf.blit(self._image_surf,(self.x + 2,100))
        self._display_surf.blit(self._image_surf,(self.x + 12,100))
        self._display_surf.blit(self._image_surf,(self.x + 52,100))
        self.x = self.x + 1
        if self.x > 800:
            self.x = 0
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
