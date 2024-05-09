import pygame
from game import *

BLACK = (0,0,0)
WIDTH = 600.0
HEIGHT = 850.0

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock();
    currentTime = 0
    prevTime = 0
    
    exit = False
    
    game = Game(screen,WIDTH/2,HEIGHT)

    while not exit:
        events = pygame.event.get()

        for event in events :
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.gameOver:
                    game = Game(screen,WIDTH/2,HEIGHT)
                elif not game.startGame:
                    game.startGame = True
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if not game.startGame:
                    if keys[pygame.K_r]:
                        game.gearSelect()
                    
        currentTime = pygame.time.get_ticks() #Staggers firing so it doesnt shoot every frame
        if currentTime - prevTime > game.player.gear.getFireRate():
            prevTime = currentTime
            game.changeShootState(True)

        if not game.gameOver and game.startGame:
            game.handleInput()
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
