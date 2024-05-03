import pygame
from game import *

BLACK = (0,0,0)
WIDTH = 600
HEIGHT = 850

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock();
    
    exit = False
    
    game = Game(screen,WIDTH/2,HEIGHT)

    while not exit:
        events = pygame.event.get()

        for event in events :
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYUP:
                game.changeShootState(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.gameOver:
                    game = Game(screen,WIDTH/2,HEIGHT)
                elif not game.startGame:
                    game.startGame = True

        if not game.gameOver and game.startGame:
            game.handleInput()
            game.enemyShoot()
            game.moveEnemies()
            game.draw()
        elif not game.startGame:
            game.StartScreen()
        else:
            game.GameOver()

        pygame.display.update()
        screen.fill(BLACK)
        clock.tick(60)


if __name__ == "__main__":
    main()
