import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.lifetime = 1.25

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
    