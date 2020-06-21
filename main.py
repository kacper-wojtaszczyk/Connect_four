import pygame
import numpy as np
from os import path


class Game():
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Connect four")
        self.running = True
        self.clock = pygame.time.Clock()

    def new_game(self):
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_ESCAPE] and self.playing:
            self.playing = False
            self.running = False
            pass

    def update(self):
        pass

    def draw(self):
        pass

    def start_screen(self):
        pass

    def game_over(self):
        pass


game = Game()
game.start_screen()
while game.running:
    game.new_game()
    game.game_over()

pygame.quit()
