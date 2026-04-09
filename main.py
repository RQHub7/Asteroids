import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
from scoring import ScoreBoard

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.event.set_grab(True)
    pygame.event.set_grab(False)

    state = "MENU"
    
    clock = pygame.time.Clock()
    dt = 0 # delta tick - change in tick - kinda like game's metronome

    # Player containers & instances
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Asteroid containers & instances
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Shots containers & instance setup
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Scoreboard container
    score = pygame.sprite.Group()
    ScoreBoard.containers = (score, drawable)

    # Menu setup 
    menu_font = pygame.font.Font(None, 36)
    screen_rect = screen.get_rect()

    start_button_rect = pygame.Rect(0, 0, 200, 50)
    start_button_rect.center = screen_rect.center
    start_button_rect.y -= 35
    exit_button_rect = pygame.Rect(0, 0, 200, 50)
    exit_button_rect.top = start_button_rect.bottom + 20 
    exit_button_rect.centerx = start_button_rect.centerx

    start_text = menu_font.render("Start Game", True, (0, 0, 0))
    exit_text = menu_font.render("Exit", True, (0, 0, 0))
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)

    title_font = pygame.font.Font(None, 72)
    heading_text = "ASTEROIDS" 
    heading_surface = title_font.render(heading_text, True, (57, 255, 20))
    heading_rect = heading_surface.get_rect(centerx=screen_rect.centerx, y=100)

    last_score_surface = menu_font.render("Welcome!", True, (255, 255, 255))
    last_score_rect = last_score_surface.get_rect(centerx=screen_rect.centerx, top=heading_rect.bottom + 10)

    #game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")   


        if state == "MENU":
            mouse_pos = pygame.mouse.get_pos()
            
            start_color = (200, 200, 200) if start_button_rect.collidepoint(mouse_pos) else (255, 255, 255)
            exit_color = (200, 200, 200) if exit_button_rect.collidepoint(mouse_pos) else (255, 255, 255)

            pygame.draw.rect(screen, start_color, start_button_rect)
            pygame.draw.rect(screen, exit_color, exit_button_rect)

            screen.blit(start_text, start_text_rect)
            screen.blit(exit_text, exit_text_rect)
            screen.blit(heading_surface, heading_rect)
            screen.blit(last_score_surface, last_score_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    sys.exit()
                elif start_button_rect.collidepoint(event.pos):

                    updatable.empty()
                    drawable.empty()
                    asteroids.empty()
                    shots.empty()
                    score.empty()

                    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    score_board = ScoreBoard(10, 10)
                    asteroid_field = AsteroidField()

                    state = "PLAYING"


        if state == "PLAYING":

            for updates in updatable:
                updates.update(dt)
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    print("GAME OVER!")
                    heading_text = "GAME OVER!" 
                    heading_surface = title_font.render(heading_text, True, (255, 0, 0)) 
                    heading_rect = heading_surface.get_rect(centerx=screen_rect.centerx, y=100)

                    current_score = score_board.score
                    last_score_surface = menu_font.render(f"Last Score: {current_score}", True, (255, 255, 255))
                    last_score_rect = last_score_surface.get_rect(centerx=screen_rect.centerx, top=heading_rect.bottom + 10)

                    state = "MENU"
                    pass

                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        score_board.update_score(100)
                        shot.kill()
                        asteroid.split()            

            for draws in drawable:
                draws.draw(screen)

            dt = clock.tick(60) / 1000
            
        pygame.display.flip()



if __name__ == "__main__":
    main()
